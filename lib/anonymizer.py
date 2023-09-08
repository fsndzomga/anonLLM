import re
from faker import Faker
import spacy


class Anonymizer:
    def __init__(self):
        self.fake = Faker()
        self.load_spacy_model()

    def load_spacy_model(self):
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except:  # noqa
            print("Model not found. Downloading en_core_web_sm...")
            spacy.cli.download("en_core_web_sm")
            self.nlp = spacy.load("en_core_web_sm")

    def anonymize_data(self, sentence):
        email_map = {}
        name_map = {}
        phone_map = {}
        anon_sentence = sentence
        phone_pattern = r"\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}"  # noqa

        doc = self.nlp(sentence)

        for ent in doc.ents:
            if ent.label_ == "PERSON":
                fake_name = self.fake.name()
                name_map[ent.text] = fake_name
                anon_sentence = anon_sentence.replace(ent.text, fake_name)

        for phone in re.findall(phone_pattern, sentence):
            fake_phone = self.fake.phone_number()
            phone_map[phone] = fake_phone
            anon_sentence = anon_sentence.replace(phone, fake_phone)

        for email in re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', sentence):  # noqa
            fake_email = self.fake.email()
            email_map[email] = fake_email
            anon_sentence = anon_sentence.replace(email, fake_email)

        mappings = {
            'email_map': email_map,
            'name_map': name_map,
            'phone_map': phone_map
        }

        return anon_sentence, mappings
