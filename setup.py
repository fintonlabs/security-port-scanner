from setuptools import setup, find_packages

setup(
    name='PortScanner',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'socket',
        'os',
        'sys',
        'json',
        'csv',
        'datetime',
        'typing'
    ],
    entry_points={
        'console_scripts': [
            'portscanner=portscanner:main',
        ],
    },
)