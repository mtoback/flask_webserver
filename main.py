from flask import Flask, render_template
from json import dumps
from markupsafe import escape
from flask_cors import CORS, cross_origin
app = Flask(__name__, static_folder='templates', static_url_path='/')
from run_test import run_tests
CORS(app)

from school_data import SchoolData
from company_data import CompanyData
from db_processing import DBProcessing
# Use the route() decorator to bind a function to a URL.
@app.route('/api/python/tests')
def getTestResults():
    return run_tests()

@app.route('/api/python/school/<schoolname>')
def getSchoolInfo(schoolname):
    schoolData = DBProcessing()
    return dumps(schoolData.getSchoolInfo(schoolname))

@app.route('/api/python/company/<companyname>')
def getCompanyInfo(companyname):
    companyData = DBProcessing()
    return dumps(companyData.getCompanyInfo(companyname))

if __name__ == '__main__':
    app.run()

