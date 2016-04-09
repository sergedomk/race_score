#!/usr/bin/python
"""
RaceScore
"""
import io
from setuptools import setup

with io.open('requirements-testing.txt') as fd:
    test_reqs = fd.readlines()
    tests_require = [line for line in test_reqs if not line.startswith('#')]

with io.open('README.rst') as fd:
    long_desc = fd.read()

setup(
    name = 'race-score',
    version = '0.1',
    description = 'Python parser/processor for scoring time based racing events.',
    long_description = long_desc,
    author = 'Serge Domkowski',
    author_email = 'sergedomk@gmail.com',
    url = 'https://github.com/sergedomk/race_score',
    license = 'BSD',
    include_package_data = True,
    packages=['race_score'],
    install_requires = [],
    tests_require = tests_require,
    platforms = ['any'],
    classifiers = [
        'Development Status :: 1 - Planning',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries',
    ],
)
