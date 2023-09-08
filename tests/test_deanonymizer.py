import unittest
from lib.deanonymizer import Deanonymizer
from lib.anonymizer import Anonymizer


class TestDeanonymizer(unittest.TestCase):
    def setUp(self):
        self.deanonymizer = Deanonymizer()
        self.anonymizer = Anonymizer()

    def test_deanonymize(self):
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
            deanonymized_text = self.deanonymizer.deanonymize(anonymized_text,
                                                              mapping)
            self.assertIn('Alice Johnson', deanonymized_text)
            self.assertIn('alice.johnson@example.com', deanonymized_text)


if __name__ == "__main__":
    unittest.main()
