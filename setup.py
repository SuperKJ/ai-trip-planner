from os import name
from setuptools import setup, find_packages
from typing import List

def get_requirements():
    """
    This function will return list of requirements
    """

    list_of_requirements = []

    try:
        with open("requirements.txt", 'r') as f:
            requirements = f.readlines()

            for requirement in requirements:
                if requirement.strip() and requirement.strip()!="-e .":
                    list_of_requirements.append(requirement.strip())
    
    except FileNotFoundError:
        print("requiremetns file not found.")

    return list_of_requirements

print(get_requirements())
setup(
    name='ai-trip-planner',
    version='0.0.1',
    author="superkj",
    packages=find_packages(),
    install_requires=get_requirements()
)