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

        prompt = 'Extract the requested  information from the following sentence: "John Hanson is visiting Rome."'
        response = self.llm.generate(prompt, output_format=Output)
        self.assertTrue(isinstance(response, Output))
        self.assertIn("John Hanson", response.person)
        self.assertIn("Rome", response.city)



if __name__ == "__main__":
    unittest.main()
