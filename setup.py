#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from setuptools import setup, find_packages


# Settings
PACKAGE_NAME = 'fdma'
USER_NAME = 'Olalaye'
REPO_NAME = 'fdma'
FILE = Path(__file__).resolve()
PARENT = FILE.parent  # root directory

about = {}
exec((PARENT / PACKAGE_NAME / '__version__.py').read_text(encoding='utf-8'), about)
DESCRIPTION = 'File Description Management Assistant'
README = (PARENT / 'README.md').read_text(encoding='utf-8')
REQUIREMENTS = (PARENT / 'requirements.txt').read_text(encoding='utf-8').splitlines()

setup(
    name=PACKAGE_NAME,
    version=about['__version__'],
    author=USER_NAME,
    url=f'https://github.com/{USER_NAME}/{REPO_NAME}',
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    license='MIT',
    install_requires=REQUIREMENTS,

    entry_points={
        'console_scripts': [
            'FDMA=fdma.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
