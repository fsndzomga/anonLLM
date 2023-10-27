import openai
import time
import json
from pydantic import BaseModel, ValidationError, ConfigDict
from typing import Type, Optional
import os
from anonLLM.anonymizer import Anonymizer
from anonLLM.deanonymizer import Deanonymizer


class OpenaiLanguageModel:
    def __init__(self, api_key=None, model="gpt-3.5-turbo", temperature=0.5, anonymize=True):
        self.anonymize = anonymize

        if self.anonymize:
            self.anonymizer = Anonymizer()
            self.deanonymizer = Deanonymizer()

        if api_key is None:
            api_key = os.environ.get('OPENAI_API_KEY')

        if api_key is None:
            raise ValueError("The OPENAI API KEY must be provided either as "
                             "an argument or as an environment variable named 'OPENAI_API_KEY'") # noqa

        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        openai.api_key = self.api_key

    def generate(self, prompt: str, output_format: Optional[Type[BaseModel]] = None,
                 n_completions: int = 1, max_tokens: int = None):
        anonymized_prompt, mappings = (self.anonymizer.anonymize_data(prompt)
                                       if self.anonymize else (prompt, None))

        retry_delay = 0.1
        valid_responses = []

        while len(valid_responses) < n_completions:
            try:
                system_message = "You are a helpful assistant."
                if output_format:
                    system_message += f" Respond in a JSON format that contains the following keys: {self._model_structure_repr(output_format)}" # noqa

                params = {
                    "model": self.model,
                    "messages": [
                        {
                            "role": "system",
                            "content": system_message
                        },
                        {
                            "role": "user",
                            "content": anonymized_prompt
                        }
                    ],
                    "temperature": self.temperature,
                    "n": n_completions
                }

                if max_tokens is not None:
                    params["max_tokens"] = max_tokens

                response = openai.ChatCompletion.create(**params)
                choices = response["choices"]
                responses = [choice["message"]["content"]
                             for choice in choices]

                if output_format:
                    valid_responses.extend(
                        [json.loads(res) for res in responses
                         if self._is_valid_json_for_model(res, output_format)]
                    )
                else:
                    valid_responses.extend(responses)

            except openai.error.RateLimitError:
                print(f"Hit rate limit. Retrying in {retry_delay} seconds.")
                time.sleep(retry_delay)
                retry_delay *= 2
            except Exception as err:
                print(f"Error: {err}")
                break

        def _deanonymize(response):
            if output_format:
                for key, value in response.items():
                    response[key] = self.deanonymizer.deanonymize(value, mappings)
                return output_format.model_validate(response)
            else:
                return self.deanonymizer.deanonymize(response, mappings)

        deanonymized_responses = [_deanonymize(res) if self.anonymize else res
                                  for res in valid_responses]

        if n_completions == 1:
            # if generating a single completion, return it directly
            return deanonymized_responses[0]
        return deanonymized_responses

    def _model_structure_repr(self, model: Type[BaseModel]) -> str:
        fields = model.__annotations__
        return ', '.join(f'{key}: {value}' for key, value in fields.items())


    def _is_valid_json_for_model(self, text: str, model: Type[BaseModel]) -> bool: # noqa
        """
        Check if a text is valid JSON and if it respects the provided BaseModel. # noqa
        """
        model.model_config = ConfigDict(strict=True)

        try:
            parsed_data = json.loads(text)
            model(**parsed_data)
            return True
        except (json.JSONDecodeError, ValidationError):
            return False
