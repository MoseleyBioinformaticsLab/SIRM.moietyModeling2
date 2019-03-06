#!/usr/bin/python3

import re
from setuptools import setup, find_packages


def find_version():
    with open('mwtab/__init__.py', 'r') as fd:
        version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                            fd.read(), re.MULTILINE).group(1)
    if not version:
        raise RuntimeError('Cannot find version information')
    return version


setup(

    name='moiety_modeling',
    version=find_version(),
    packages=find_packages(),
    license="The Clear BSD License",
    author_email="hji236@g.uky.edu",
    description="",
    keywords="",
    install_requires=[],
    url="",
    long_description=open('README.rst').read(),
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: The Clear BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',

    ],


)