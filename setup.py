"""
This module contains the setup script for see-algo, as well as
specifications for the package name, version, and installation
requirements.
"""

from setuptools import setup

setup(
    name='see-algo',
    version='1.0',
    description='''A Python library to visualize a
                data structure as it changes throughout a function''',
    packages=['see-algo'],
    install_requires=['graphviz'],
)
