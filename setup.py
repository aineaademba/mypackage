from setuptools import setup, find_packages

setup(
    name = 'mypackage',
    version = '0.1',
    packages = find_packages(exclude=['tests']),
    license = 'MIT',
    description = "EDSA example python package",
    install_requirements = ['numpy'],
    url = 'https://github.com/<aineaademba>/<mypackage>',
    author="Ainea Ademba",
    author_email = 'aineaademba@gmail.com'
)