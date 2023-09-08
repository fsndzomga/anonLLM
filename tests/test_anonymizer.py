import unittest
from lib.anonymizer import Anonymizer


class TestAnonymizer(unittest.TestCase):

    def setUp(self):
        self.anonymizer = Anonymizer()

    def test_anonymize_data(self):
        # Test with 10 different examples that include name, email, and phone numbers # noqa
        test_examples = [
            "My name is Alice Johnson, email: alice.johnson@example.com, "
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
            anonymized_text, mapping = self.anonymizer.anonymize_data(example)
            self.assertNotIn('Alice Johnson', anonymized_text)
            self.assertNotIn('alice.johnson@example.com', anonymized_text)


if __name__ == "__main__":
    unittest.main()
