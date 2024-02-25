from setuptools import find_packages,setup
from typing import List
def get_requirement(file_path:str)->list[str]:
    """
    this function require the list of requirements
    """
    repruirements=[]
    with open(file_path) as file_obj:
        repruirements = file_obj.readlines()
        repruirements =[req.replace("\n", "")for req in repruirements]
        if HYPEN_E_DOT in repruirements:
            repruirements.remove(HYPEN_E_DOT)
    
    return repruirements


setup(
name='Machine-Learning-Project1',
version="0.0.1",
author='Godd',
author_email="lcd000111@gmail.com",
packages=find_packages,
install_requires = get_requirement('requirements.txt')

)