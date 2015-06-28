#!/usr/bin/env python

from setuptools import setup, find_packages

version = '0.1'

setup(
    name='praw-oauth2util',
    version=version,
    author='Benjamin Schmid',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/SmBe19/praw-OAuth2Util/',
    license='MIT',
    description='OAuth2 wrapper for PRAW',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)