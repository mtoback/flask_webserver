#!/usr/bin/env python

import unittest
#from school_data import SchoolData
#from company_data import CompanyData
from db_processing import DBProcessing
'''
unit tests for school and company data retrieval
'''
class TestFlaskDB(unittest.TestCase):
    def test_school_success_rpi(self):
        schoolData = DBProcessing()
        result = schoolData.getSchoolInfo('rpi')
        self.assertTrue(result is not None, "expected a result object")
        self.assertTrue(type(result) == dict, "expected a dictionary")
        self.assertTrue('degree' in result, "expected a degree tag")
        self.assertTrue('description' in result, "expected a description tag")
        self.assertTrue('date' in result, "expected a date tag")
        self.assertTrue('location' in result, "expected a location tag")
        self.assertTrue('name' in result, "expected a name tag")
        self.assertEqual(result['name'] , 'Rensselaer Polytechnic Institute',
                         'expected "Rensselaer Polytechnic Institute" instead got %s'
                         % result['name'])

    def test_school_success_cmu(self):
        schoolData = DBProcessing()
        result = schoolData.getSchoolInfo('cmu')
        self.assertTrue(result is not None, "expected a result object")
        self.assertTrue(type(result) == dict, "expected a dictionary")
        self.assertTrue('degree' in result, "expected a degree tag")
        self.assertTrue('description' in result, "expected a description tag")
        self.assertTrue('date' in result, "expected a date tag")
        self.assertTrue('location' in result, "expected a location tag")
        self.assertTrue('name' in result, "expected a name tag")
        self.assertEqual(result['name'] , 'Carnegie-Mellon University',
                         'expected "Carnegie-Mellon University" instead got %s'
                         % result['name'])

    def test_school_fail(self):
        schoolData = DBProcessing()
        result = schoolData.getSchoolInfo('ineverwentthere')
        self.assertTrue(result is not None, "expected a result object")
        self.assertTrue(type(result) == dict, "expected a dictionary")
        self.assertTrue('degree' in result, "expected a degree tag")
        self.assertTrue('description' in result, "expected a description tag")
        self.assertTrue('date' in result, "expected a date tag")
        self.assertTrue('location' in result, "expected a location tag")
        self.assertTrue('name' in result, "expected a name tag")
        self.assertEqual(result['name'] , 'ineverwentthere',
                         'expected "ineverwentthere" instead got %s'
                         % result['name'])

    def test_company_success_chordiant(self):
        companyData = DBProcessing()
        result = companyData.getCompanyInfo('chordiant')
        self.assertTrue(result is not None, "expected a result object")
        self.assertTrue(type(result) == dict, "expected a dictionary")
        self.assertTrue('business' in result, "expected a business tag")
        self.assertTrue('description' in result, "expected a description tag")
        self.assertTrue('date' in result, "expected a date tag")
        self.assertTrue('location' in result, "expected a location tag")
        self.assertTrue('name' in result, "expected a name tag")
        self.assertEqual(result['name'] , 'Chordiant (Now Pegasystems)',
                         'expected "Chordiant (Now Pegasystems)" instead got %s'
                         % result['name'])

    def test_company_success_llnl(self):
        companyData = DBProcessing()
        result = companyData.getCompanyInfo('llnl')
        self.assertTrue(result is not None, "expected a result object")
        self.assertTrue(type(result) == dict, "expected a dictionary")
        self.assertTrue('business' in result, "expected a business tag")
        self.assertTrue('description' in result, "expected a description tag")
        self.assertTrue('date' in result, "expected a date tag")
        self.assertTrue('location' in result, "expected a location tag")
        self.assertTrue('name' in result, "expected a name tag")
        self.assertEqual(result['name'] , 'Lawrence Livermore National Laboratory',
                         'expected "Lawrence Livermore National Laboratory" instead got %s'
                         % result['name'])

    def test_company_success_vmware(self):
        companyData = DBProcessing()
        result = companyData.getCompanyInfo('vmware')
        self.assertTrue(result is not None, "expected a result object")
        self.assertTrue(type(result) == dict, "expected a dictionary")
        self.assertTrue('business' in result, "expected a business tag")
        self.assertTrue('description' in result, "expected a description tag")
        self.assertTrue('date' in result, "expected a date tag")
        self.assertTrue('location' in result, "expected a location tag")
        self.assertTrue('name' in result, "expected a name tag")
        self.assertEqual(result['name'] , 'VMWare',
                         'expected "VMWare" instead got %s'
                         % result['name'])

    def test_company_success_gte(self):
        companyData = DBProcessing()
        result = companyData.getCompanyInfo('gte')
        self.assertTrue(result is not None, "expected a result object")
        self.assertTrue(type(result) == dict, "expected a dictionary")
        self.assertTrue('business' in result, "expected a business tag")
        self.assertTrue('description' in result, "expected a description tag")
        self.assertTrue('date' in result, "expected a date tag")
        self.assertTrue('location' in result, "expected a location tag")
        self.assertTrue('name' in result, "expected a name tag")
        self.assertEqual(result['name'] , 'GTE Government Systems',
                         'expected "GTE Government Systems" instead got %s'
                         % result['name'])
    def test_company_success_oceania(self):
        companyData = DBProcessing()
        result = companyData.getCompanyInfo('oceania')
        self.assertTrue(result is not None, "expected a result object")
        self.assertTrue(type(result) == dict, "expected a dictionary")
        self.assertTrue('business' in result, "expected a business tag")
        self.assertTrue('description' in result, "expected a description tag")
        self.assertTrue('date' in result, "expected a date tag")
        self.assertTrue('location' in result, "expected a location tag")
        self.assertTrue('name' in result, "expected a name tag")
        self.assertEqual(result['name'] , 'Oceania',
                         'expected "Oceania" instead got %s'
                         % result['name'])

    def test_company_success_niosh(self):
        companyData = DBProcessing()
        result = companyData.getCompanyInfo('niosh')
        self.assertTrue(result is not None, "expected a result object")
        self.assertTrue(type(result) == dict, "expected a dictionary")
        self.assertTrue('business' in result, "expected a business tag")
        self.assertTrue('description' in result, "expected a description tag")
        self.assertTrue('date' in result, "expected a date tag")
        self.assertTrue('location' in result, "expected a location tag")
        self.assertTrue('name' in result, "expected a name tag")
        self.assertEqual(result['name'] , 'National Institute of Occupational Safety and Health',
                         'expected "National Institute of Occupational Safety and Health" instead got %s'
                         % result['name'])

    def test_company_success_attorney(self):
        companyData = DBProcessing()
        result = companyData.getCompanyInfo('attorney')
        self.assertTrue(result is not None, "expected a result object")
        self.assertTrue(type(result) == dict, "expected a dictionary")
        self.assertTrue('business' in result, "expected a business tag")
        self.assertTrue('description' in result, "expected a description tag")
        self.assertTrue('date' in result, "expected a date tag")
        self.assertTrue('location' in result, "expected a location tag")
        self.assertTrue('name' in result, "expected a name tag")
        self.assertEqual(result['name'] , 'Attorney At Law',
                         'expected "Attorney At Law" instead got %s'
                         % result['name'])

    def test_company_fail(self):
        companyData = DBProcessing()
        result = companyData.getCompanyInfo('neverworkedthere')
        self.assertTrue(result is not None, "expected a result object")
        self.assertTrue(type(result) == dict, "expected a dictionary")
        self.assertTrue('business' in result, "expected a business tag")
        self.assertTrue('description' in result, "expected a description tag")
        self.assertTrue('date' in result, "expected a date tag")
        self.assertTrue('location' in result, "expected a location tag")
        self.assertTrue('name' in result, "expected a name tag")
        self.assertEqual(result['name'] , 'neverworkedthere',
                         'expected "neverworkedthere instead got %s'
                         % result['name'])

if __name__ == '__main__':
    unittest.main()
