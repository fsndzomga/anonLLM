from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="anonLLM",
    version="0.1.9",
    author="FS Ndzomga",
    author_email="ndzomgafs@gmail.com",
    description="Anonymizes personally identifiable information for "
    "Large Language Model APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fsndzomga/anonLLM",
    project_urls={
        "Bug Tracker": "https://github.com/fsndzomga/anonLLM/issues"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "Faker",
        "openai",
        "pydantic>=2",
        "spacy>=3",
    ],
    extras_require={
        "dev": ["pytest", "flake8"],
    },
)
