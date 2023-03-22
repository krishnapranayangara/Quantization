# to scrape through the requirements and install the necessary packages
from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]

    with open('requirements.txt') as f:
        requirements=f.readlines()
        [req.replace('/n',"") for req in requirements]

        if "-e ." in requirements:
            requirements.remove('-e .')
        return requirements
    
setup(
    name="Quantization in ML",
    version='0.0.1',
    author='Krishna Pranay Angara',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)