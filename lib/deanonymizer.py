class Deanonymizer:
    def deanonymize(self, text, mappings):
        # Replace anonymized fake values back with the original ones
        for original_email, fake_email in mappings['email_map'].items():
            text = text.replace(fake_email, original_email)
        for original_name, fake_name in mappings['name_map'].items():
            text = text.replace(fake_name, original_name)
        for original_phone, fake_phone in mappings['phone_map'].items():
            text = text.replace(fake_phone, original_phone)

        return text
