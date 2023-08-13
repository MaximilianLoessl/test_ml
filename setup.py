from setuptools import find_packages, setup
from typing import List #important for recognizing lists

# bei install_requires entweder direkt reinschreiben was req mit:
# install_requires=['pandas', 'numpy', 'seaborn'] oder wie hier als funktion
# indem ich aus dem requirements.txt file die packages raus lese

HYPEN_E_DOT='-e .'
def get_requirements(filepath:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
name='test_ml',
version='0.0.1',
author='Maximilian',
author_email='maximilian.loessl@students.unibe.ch',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)
