# coding: utf-8

from setuptools import setup


setup(
    name='dnstools',
    version='0.0.0',
    author='kain',
    author_email='me@kain-jy.com',
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
