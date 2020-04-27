#!/usr/bin/env python

import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_tables import Company, School
from secret_data import SecretData
from sqlalchemy_encoder import SQLAlchemyEncoder

'''
initial database processing class
contains the interface to sqlalchemy via ORM queries
'''
class DBProcessing():
    '''
    initialize the class by opening a session to the database,
    getting the database string from the secrets file
    '''
    def __init__(self):
        secretData = SecretData()
        db_string = secretData.getValue('db_string')
        _db = create_engine(db_string)
        self._Session = sessionmaker(_db)
        self._Session.configure(bind=_db)

    def getCompanyInfo(self, company_name):
        companyValuesDict = {'name': company_name,
                       'date': 'not found',
                       'location': 'not found',
                       'business': 'not found',
                       'description': 'not found'}
        session = self._Session()
        query = session.query(Company).filter(Company.key_name == company_name)
        companyData = query.first()
        if companyData:
            companyValues = json.dumps(companyData, cls=SQLAlchemyEncoder)
            companyValuesDict = json.loads(companyValues)
            companyValuesDict['date'] = companyValuesDict['start_date'] + ' - ' + companyValuesDict['end_date']
        return companyValuesDict

    def getSchoolInfo(self, schoolName):
        schoolValuesDict = {'name': schoolName,
                         'date': 'not found',
                         'location': 'not found',
                         'degree': 'not found',
                         'description': 'not found'}
        session = self._Session()
        schoolData = session.query(School).filter(School.key_name == schoolName).first()
        if schoolData:
            schoolValues = json.dumps(schoolData, cls=SQLAlchemyEncoder)
            schoolValuesDict = json.loads(schoolValues)
            schoolValuesDict['date'] = schoolValuesDict['start_date'] + ' - ' + schoolValuesDict['end_date']
        return schoolValuesDict

if __name__ == "__main__":
    dbProc = DBProcessing()
    print(dbProc.get_school('neverwentthere'))
    print(dbProc.get_school('rpi'))
    print(dbProc.get_school('cmu'))
    print(dbProc.get_company('notreal'))
    print(dbProc.get_company('llnl'))
    print(dbProc.get_company('gte'))
    print(dbProc.get_company('chordiant'))
    print(dbProc.get_company('vmware'))
    print(dbProc.get_company('intrexon'))
    print(dbProc.get_company('niosh'))
    print(dbProc.get_company('attorney'))


