from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT= '-e .'
def get_requirements(file_path:str)-> List[str]:
    """This function returns a list of requirements from a given file path."""
    requirements=[]
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements= [req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='1.0.0',
    author='Chetan',
    author_email='chetanpawar2002official@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)