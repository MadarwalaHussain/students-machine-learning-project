from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [requirement.replace("\n", "") for requirement in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements  # Missing return statement


setup(  
    name="mlproject",
    version='0.0.1',
    author='Hussain',
    author_email='hussainmadar4@gmail.com',  
    description='A machine learning project',  
    packages=find_packages(),  
    install_requires=get_requirements('requirements.txt')
)
