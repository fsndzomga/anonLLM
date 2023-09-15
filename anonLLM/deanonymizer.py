class Deanonymizer:
    def deanonymize(self, text, mappings):
        # Loop through each pattern mapping and replace the anonymized values
        # back to the original ones
        for _, pattern_map in mappings.items():
            for original_value, fake_value in pattern_map.items():
                text = text.replace(fake_value, original_value)
        return text
