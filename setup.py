from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
   
    Parameters
    ----------
    file_path : str
        DESCRIPTION.

    Returns
    -------
    List[str]
        DESCRIPTION.
        
    This function will return list of requirements

    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements
        
        
setup(
name = 'genericMLProjectStructure',
version = '0.0.1',
author = 'Gayathri',
author_email = 'gayathri_g21@yahoo.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)