'''
Test script for the modeval.py

AUTHOR: Christopher Bonham
DATE:   28th February 2023

This test script is called automatically when the code is pushed to the
remote repo https://github.com/ChrisB831/crbutils

To run all test scripts
1) Go to the project root
2) python -m pytest -vv

To run this script in isolation
1) Go to the project root
2) python -m pytest .\tests\test_modeval.py -vv
'''


def test_always_pass():
    '''Dummy test that always passes
    Useful for testing the CI functionality

    Inputs:
        none
    Outputs:
        none
    '''
    assert True


# def test_always_fail():
#     '''Dummy test that always fails
#     Useful for testing the CI functionality
#
#     Inputs:
#         none
#     Outputs:
#         none
#     '''
#     assert False
