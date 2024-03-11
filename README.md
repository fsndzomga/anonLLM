# anonLLM: Anonymize Personally Identifiable Information (PII) for Large Language Model APIs

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

```bash
pip install anonLLM
```

# Quick Start

Here's how to get started with anonLLM:

```python
from anonLLM.llm import OpenaiLanguageModel
from dotenv import load_dotenv

load_dotenv()

# Anonymize a text
text = "Write a CV for me: My name is Alice Johnson, "\
    "email: alice.johnson@example.com, phone: +1 234-567-8910."\
    "I am a machine learning engineer."

# Anonymization is handled under the hood
llm = OpenaiLanguageModel()

response = llm.generate(text)

print(response)
```
In this example, the response will contain the correct name provided.
At the same time, no PII will be sent to OpenAI.

You can also use anonLLM to generate structured outputs in a JSON format.
You just have to define a pydantic model for your output, and use the output_format argument like this:

```python
from pydantic import BaseModel
from anonLLM.llm import OpenaiLanguageModel
from dotenv import load_dotenv

load_dotenv()

llm = OpenaiLanguageModel(anonymize=False, temperature=1)


class Person(BaseModel):
    name: str
    sex: str
    age: int
    email: str


response = llm.generate(
    prompt="Generate a person",
    output_format=Person
)

print(response)

# Returns: {'name': 'Alex', 'sex': 'Male', 'age': 32, 'email': 'alex@example.com'}

```



# Contributing

We welcome contributions!

# License

This project is licensed under the MIT License.
