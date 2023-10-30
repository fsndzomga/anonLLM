import unittest

from pydantic import BaseModel

from anonLLM.llm import OpenaiLanguageModel
from dotenv import load_dotenv

load_dotenv()


class TestOpenaiLanguageModel(unittest.TestCase):
    def setUp(self):
        self.llm = OpenaiLanguageModel()

    def test_generate(self):
        prompt = (
            "My name is Alice Johnson, "
            "email: alice.johnson@example.com, "
            "phone: +1 234-567-8910. "
            "Write an imaginary cover letter for me "
            "as a machine learning engineer."
        )
        response = self.llm.generate(prompt)

        self.assertIsNotNone(response)
        self.assertNotEqual("", response.strip())
        self.assertIn("Alice Johnson", response)

    def test_generate_with_model_output(self):
        class Output(BaseModel):
            person: str
            city: str

        prompt = 'Extract the requested  information from the following sentence: "Alice Johnson is visiting Rome."'
        response = self.llm.generate(prompt, output_format=Output)
        self.assertTrue(isinstance(response, Output))
        self.assertIn("Alice Johnson", response.person)
        self.assertIn("Rome", response.city)

    def test_generate_n_completions(self):
        prompt = (
            "What is the user's favorite color in the following expression?"
            "\nAlice Johnson's favorite color is blue"
        )
        responses = self.llm.generate(prompt, n_completions=2)
        self.assertEqual(len(responses), 2)
        for response in responses:
            self.assertIsNotNone(response)
            self.assertIn("blue", response.lower())

    def test_generate_n_completions_with_model_output(self):
        class Output(BaseModel):
            person: str
            city: str

        prompt = 'Extract the requested  information from the following sentence: "Alice Johnson is visiting Rome."'
        responses = self.llm.generate(prompt, output_format=Output, n_completions=2)
        self.assertEqual(len(responses), 2)
        for response in responses:
            self.assertTrue(isinstance(response, Output))
            self.assertIn("Alice Johnson", response.person)
            self.assertIn("Rome", response.city)



if __name__ == "__main__":
    unittest.main()
