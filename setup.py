#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.6,<7.0',
]

test_requirements = [
]

setup(
    name='pgdie',
    version='0.1.0',
    description="PostgreSQL import and export commandline tool",
    long_description=readme + '\n\n' + history,
    author="Henning Kage",
    author_email='henning.kage@gmail.com',
    url='https://github.com/hkage/pgdie',
    packages=[
        'pgdie',
    ],
    package_dir={'pgdie':
                 'pgdie'},
    entry_points={
        'console_scripts': [
            'pgdie=pgdie.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='pgdie',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
