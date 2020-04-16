from test_flask import TestFlask
import unittest
def run_tests():
    test_classes_to_run = [TestFlask]

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

