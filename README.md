# anonLLM: Anonymize Personally Identifiable Information (PII) for Language Model APIs

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

anonLLM is a Python package designed to anonymize personally identifiable information (PII) in text data before it's sent to Language Model APIs like GPT-3. The goal is to protect user privacy by ensuring that sensitive data such as names, email addresses, and phone numbers are anonymized.

# Features

Anonymize names
Anonymize email addresses
Anonymize phone numbers
Support for multiple country-specific phone number formats
Reversible anonymization (de-anonymization)
Installation

To install anonLLM, run:

python
pip install anonLLM

# Quick Start

Here's how to get started with anonLLM:

from anonLLM import OpenaiLanguageModel

## Anonymize a text
text = "My name is Alice Johnson, email: alice.johnson@example.com, phone: +1 234-567-8910."

## Anonymization is handled under the hood
llm = OpenaiLanguageModel(api_key="your_openai_api_key_here")
response = llm.generate(text)

print(response)


# Contributing

We welcome contributions!

# License

This project is licensed under the MIT License. See the LICENSE.md file for details.
