from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name = "ML-OPS-Project-2",
    version = "0.1.0",
    author = "Chinmay",
    packages=find_packages(),
    install_requires=requirements,
)