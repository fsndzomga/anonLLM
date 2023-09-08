import unittest
from lib.llm import OpenaiLanguageModel
from dotenv import load_dotenv

load_dotenv()


class TestOpenaiLanguageModel(unittest.TestCase):
    def setUp(self):
        self.llm = OpenaiLanguageModel()

    def test_generate(self):
        prompt = "Tell me a joke."
        response = self.llm.generate(prompt)

        self.assertIsNotNone(response)
        self.assertNotEqual("", response.strip())


if __name__ == "__main__":
    unittest.main()
