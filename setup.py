import os, sys

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

# full path appears to be required for old (0.6.x?) versions of setuptools
root_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(root_dir, 'doc/description.rst')) as f:
    long_description = f.read()

pkg_dir = 'lib/python'
setup(
    author = 'InVitae Keyboard Monkeys',
    author_email='reece+uta@invitae.com',
    description='Universal Transcript Archive',
    license = 'MIT',
    long_description = long_description,
    name = "uta",
    package_dir = {'': pkg_dir},
    packages = find_packages(pkg_dir),
    url = 'https://bitbucket.org/invitae/uta',
    use_hg_version = True,
    zip_safe = True,

    install_requires = [
        'docopt',
        'nose',
        'psycopg2',
        'sphinx',
        'sphinx-pypi-upload',
        'sqlalchemy',
        ],

    setup_requires = [
        'hgtools',
        ]
)
