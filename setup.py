#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='camel_and_snake',
    description=(
        'camelCase to snake_case or snake_case to camelCase for Python dict object'
    ),
    version='0.1.0',
    author='Cphayim',
    author_email='admin@cphayim.me',
    maintainer='',
    maintainer_email='',
    license='MIT License',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/Cphayim/camel-and-snake',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)
