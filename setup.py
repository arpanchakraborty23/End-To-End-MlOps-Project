from setuptools import setup,find_packages
from typing import List

Hypen_e_dot='-e .'

def get_requirements(file_path:str)->[List]:
    requirements=[]
    with open(file_path,'r') as f:
        requirements=f.readlines()
        requirements=[req.replace('/n',' ') for req in requirements]

        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)

    return requirements

__version__='0.1'
author='ArpanChakraborty23'
author_email='arpanchakraborty500@gmail.com'

setup(
    name='Data-Science-Project',
    version=__version__,
    author=author,
    author_email=author,
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()

)