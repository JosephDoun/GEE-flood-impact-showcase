from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='Joseph Doundoulakis EO Code Sample',
    version='0.1',
    author='Joseph Doundoulakis',
    email='iosif.doundoulakis@outlook.com',
    description='Technical demonstration packaged for Lobelia // Code sample',
    install_requires=requirements,
)


