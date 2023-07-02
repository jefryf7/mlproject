from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'


def get_requermeints(file_path:str) ->list[str]:
    '''
    this function will retrun the list of requermeint
    '''
    requermeints = list()
    
    with open(file_path,'r') as file_obj:
        requermeints = file_obj.readlines()
        requermeints = [req.replace('\n','') for req in requermeints]

        if HYPEN_E_DOT in requermeints:
            requermeints.remove(HYPEN_E_DOT)
    return requermeints

setup(
    name='mlproject',
    version='0.0.1',
    author= 'Jefry Fredi',
    author_email= 'jefryfredi07@gmail.com',
    packages=find_packages(),
    install_requres = get_requermeints('requermeint.txt')
)