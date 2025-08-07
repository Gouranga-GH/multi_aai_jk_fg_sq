from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="AGENTIC-AI-PROJECT",
    version="0.1",
    author="Gouranga",
    description="Agentic AI System with Smart Single-Tool Selection",
    packages=find_packages(),
    install_requires = requirements,
)
