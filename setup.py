import os

import pkg_resources
from setuptools import setup, find_packages

setup(
    name="marian_onnx",
    py_modules=["marian_onnx"],
    version="1.0",
    description="MarianMT performance optimization with ONNX conversion",
    readme="README.md",
    python_requires=">=3.7",
    author="Viva Translate",
    url="https://github.com/Viva-Translate/Marian-ONNX-Converter",
    packages=find_packages(where=".", exclude=["tests"]),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
)
