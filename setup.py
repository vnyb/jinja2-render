#!/usr/bin/env python3

"""
Setup jinja2-render
"""

from os import path
from setuptools import setup

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.rst'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='jinja2-render',

    version='0.0.1',

    description='Load variables from YAML-formatted files to render a jinja2 template',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/vnyb/jinja2-render',

    author='Vianney Bajart',
    author_email='vianney.bajart@redmintnetwork.fr',

    license='GNU General Public License v3',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: GNU General Public License v3',

        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='yaml jinja2 template',

    py_modules=[
        'jinja2_render',
    ],

    install_requires=[
        'jinja2',
        'pyaml',
    ],

    extras_require={
    },

    package_data={
    },

    data_files=[
    ],

    entry_points={
        'console_scripts': [
            'jinja2-render=jinja2_render:main',
        ],
    },
)
