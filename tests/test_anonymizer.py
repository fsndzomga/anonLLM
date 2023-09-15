import unittest
from anonLLM.anonymizer import Anonymizer
import re


class TestAnonymizer(unittest.TestCase):

    def setUp(self):
        self.anonymizer = Anonymizer()

    def extract_info(self, text):
        name_pattern = r"My name is ([\w\s]+),"
        email_pattern = r"email: ([\w\.-]+@[\w\.-]+),"
        phone_pattern = r"phone: ([\+\d\s\-]+)\."

        name = re.search(name_pattern, text).group(1)
        email = re.search(email_pattern, text).group(1)
        phone = re.search(phone_pattern, text).group(1)

        return name, email, phone

    def test_anonymize_data(self):
        # Test with 10 different examples that include name, email, and phone numbers # noqa
        test_examples = [
            "My name is Alice Ela Johnson, email: alice.johnson@example.com, "
            "phone: +1 234-567-8910.",

            "My name is Bob Smith, email: bob_smith@example.com, "
            "phone: +33 1 23 45 67 89.",

            "My name is Charlie Brown, email: charlie.brown@example.com, "
            "phone: +237 6 1234 5678.",

            "My name is David Wang, email: david.wang@example.com, "
            "phone: +1 987-654-3210.",

            "My name is Eve Adams, email: eve.adams@example.com, "
            "phone: +33 9 87 65 43 21.",

            "My name is Frank Lee, email: frank.lee@example.com, "
            "phone: +237 6 8765 4321.",

            "My name is Grace Kim, email: grace.kim@example.com, "
            "phone: +1 555-444-3333.",

            "My name is Harry Johnson, email: harry.johnson@example.com, "
            "phone: +33 4 56 78 90 12.",

            "My name is Irene Williams, email: irene.williams@example.com, "
            "phone: +237 6 7890 1234.",

            "My name is John Doe, email: john.doe@example.com, "
            "phone: +1 111-222-3333."
        ]

        for example in test_examples:
            anonymized_text, _ = self.anonymizer.anonymize_data(example)

            name, email, phone = self.extract_info(example)

            self.assertNotIn(name, anonymized_text)
            self.assertNotIn(email, anonymized_text)
            self.assertNotIn(phone, anonymized_text)


if __name__ == "__main__":
    unittest.main()
