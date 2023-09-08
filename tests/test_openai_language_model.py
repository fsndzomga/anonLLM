import unittest
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


if __name__ == "__main__":
    unittest.main()
