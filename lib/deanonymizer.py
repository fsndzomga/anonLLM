class Deanonymizer:
    def deanonymize(self, text, mappings):
        # Replace anonymized values back with the original ones
        for encrypted_val, fake_val in mappings['email_map'].items():
            text = text.replace(fake_val, encrypted_val)
        for encrypted_val, fake_val in mappings['name_map'].items():
            text = text.replace(fake_val, encrypted_val)
        for encrypted_val, fake_val in mappings['phone_map'].items():
            text = text.replace(fake_val, encrypted_val)

        return text
