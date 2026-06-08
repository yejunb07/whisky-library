from setuptools import setup, find_packages

setup(
    name="whisky_library",
    version="1.0.0",
    author="김예준",
    author_email="firebird0301@gmail.com",
    description="A Python package for managing whisky collections.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)