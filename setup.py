from setuptools import find_packages,setup 
from typing import List

hypen_e_dot="-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    this fucntion will return a list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    return requirements

setup(
name="MLProject",
version="0.0.1",
author="Arindam",
author_email="bhattacharjee.arindam95@gmail.com",
packages=find_packages(), ## a src folder has been created, now this function will go into such folders which has __init__.py and simeltaneously isntyall it as a package which eventually can be used as several other packages
install_requires=get_requirements('requirements.txt')
)