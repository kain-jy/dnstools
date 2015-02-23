# coding: utf-8

from setuptools import setup


setup(
    name='dnstools',
    entry_points={
        'console_scripts': [
            'dns=dnstools:main'
        ]
    },
    install_requires=[
        'click',
        'dnspython'
    ]
)
