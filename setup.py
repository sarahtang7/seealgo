"""
This module contains the setup script for seealgo, as well as
specifications for the package name, version, and installation
requirements.
"""

from setuptools import setup

setup(
    name='seealgo',
    version='0.2.0',
    description='''A Python library to visualize a
                data structure as it changes throughout a function''',
    packages=['seealgo'],
    install_requires=['graphviz'],
)
