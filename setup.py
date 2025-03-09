from setuptools import setup, find_packages

setup(
    name='port_scanner',
    version='0.1.0',
    description='A lightweight port scanning tool',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'concurrent.futures==3.1.1',
        'json==2.0.9',
        'socket==0.1.6',
        'os==0.1.1',
    ],
)