import os
from setuptools import setup, find_packages
from multicrane import version as __version__

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
        README = f.read()

requires = [
    'pyyaml',
    'sh',
    'termcolor',
    ]

setup(name='multicrane',
        version=__version__,
        description='A utility for managing multiple crane files and hosts in parallel',
        long_description=README,
        author='Bradley Cicenas',
        author_email='bradley.cicenas@gmail.com',
        keywords='docker, crane, deployment, orchestration',
        packages=find_packages(),
        include_package_data=True,
        install_requires=requires,
        tests_require=requires,
        entry_points = {
        'console_scripts' : ['multicrane = multicrane.multicrane:main']
        }
)
