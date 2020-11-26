# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in meeting/__init__.py
from meeting import __version__ as version

setup(
	name='meeting',
	version=version,
<<<<<<< HEAD
	description='App to manage meetings',
	author='Manale',
	author_email='meeting@info.com',
=======
	description='meeting management app',
	author='Manale',
	author_email='meetings@gmail.com',
>>>>>>> 9fb53e762bb1c96f5a4dfb993f8b001ff7b87770
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
