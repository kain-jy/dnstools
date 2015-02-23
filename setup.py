# coding: utf-8

from setuptools import setup, find_packages


setup(
    name='dnstools',
    version='0.0.1',
    packages=['dnstools'],
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
