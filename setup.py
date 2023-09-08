from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="anonLLM",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Anonymizes personally identifiable information for Language Model APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/anonLLM",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/anonLLM/issues",
        "Documentation": "https://yourusername.github.io/anonLLM/",  # Optional
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(where="lib"),
    package_dir={"": "lib"},
    python_requires=">=3.6",
    install_requires=[
        "python-dotenv",  # Assuming you are using python-dotenv for environment variables
        "some_other_dependency",  # Any other dependencies your project needs
    ],
    extras_require={
        "dev": ["pytest", "flake8"],  # Optional: specify extra requirements for development
    },
)
