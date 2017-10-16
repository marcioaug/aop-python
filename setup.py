import os
from setuptools import setup, find_packages
from pip.req import parse_requirements


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

install_reqs = parse_requirements('requirements.txt', session=False)
install_requires = [str(ir.req) for ir in install_reqs]

setup(
    name='aop-python',
    version='0.0.0',

    author='Marcio Augusto Guimaraes',
    author_email='masg@ic.ufal.br',

    packages=find_packages(),
    install_requires=install_requires
)
