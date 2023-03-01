'''
Test the project version in pyproject.toml matches that in the __init__.py
file in the package root. Poetry version bumping upates the former but
not the latter. This ensures crbutils.__version__ matches that held by PyPi

AUTHOR: Christopher Bonham
DATE:   1st Match 2023

This test script is called automatically when the code is pushed to the
remote repo https://github.com/ChrisB831/crbutils

To run all test scripts
1) Go to the project root
2) python -m pytest -vv

To run this script in isolation
1) Go to the project root
2) python -m pytest .\tests\test_version_match.py -vv
'''
import toml
import src.crbutils as crbutils


def test_versions_are_in_sync():
    '''Test the project version in pyproject.toml matches that in the
     __init__.py file in the package root.

    Inputs:
        none
    Outputs:
        none
    '''
    # Get the version from the pyproject.toml file
    pyproject_dump = toml.loads(open(r".\pyproject.toml").read())
    pyproject_version = pyproject_dump["tool"]["poetry"]["version"]
    print(pyproject_version)

    # Get the version from the package file
    package_init_version = crbutils.__version__

    assert package_init_version == pyproject_version
