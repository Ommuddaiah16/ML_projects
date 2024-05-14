from setuptools import find_packages,setup
from typing import List

hyphen_e_dot = '-e .'

def get_requirements(file_path:str)->list[str]:# returns the list of reuirements
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readline()
        [req.replace("\n","") for req in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)

    return requirements

setup (
 name='Ml_ops Project',
 version = '0.0.1',
 author = 'Omprakash',
 author_email= 'igomprakash@gmail.com',
 packages= find_packages(),
 install_requires = get_requirements('requirements.txt')

)