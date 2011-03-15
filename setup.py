#!/usr/bin/python2.6

from setuptools import setup

setup(
    name='gisty',
    version='0.1',
    description='Upload your code to gist.github.com based on https://gist.github.com/763188',
    keywords='Gist Github',
    package_dir = {'': 'src'},
    packages = ['gisty', ],
    install_requires = ['mechanize', ],
    entry_points = { 
        'console_scripts': [
            'gisty = gisty:main',
            ]   
        },  
    zip_safe = False,
    )   

