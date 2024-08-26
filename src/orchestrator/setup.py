# Copyright 2023 Reply S.p.A. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from setuptools import setup, find_packages

setup(
    name='orchestrator',
    version='1.0.0',
    packages=find_packages(),  # Automatically discover and include all packages
    entry_points={
        'console_scripts': [
            'orchestrator-cli = orchestrator.cli:main',
        ],
    },
    author='Reply S.p.A.',
    description='Simple orchestrator that has the same structure used to control SPOT Robot.'
)
