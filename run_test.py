#!/usr/bin/env python

from test_flask import TestFlaskDB
import unittest


'''
wrapper function to execute test suite and return statistics as a json object
which can then be sent over the internet.

The only change one must make is to add new test classes 
to the test_classes_to_run variable
'''
def run_tests():
    test_classes_to_run = [TestFlaskDB]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    result = runner.run(big_suite)
    result_obj = {'test_run': result.testsRun,
                  'tests_failed': [fail[1] for fail in result.failures],
                  'test_errors': [err[1] for err in result.errors]}
    return result_obj

if __name__ == "__main__":
    run_tests()

