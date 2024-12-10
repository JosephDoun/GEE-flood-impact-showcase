from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='Joseph Doundoulakis GEE Flood Impact Showcase',
    version='0.1',
    author='Joseph Doundoulakis',
    email='iosif.doundoulakis@outlook.com',
    description='GEE Flood Impact Showcase',
    install_requires=requirements,
)


