from flask import Flask, render_template
from markupsafe import escape
from flask_cors import CORS, cross_origin
app = Flask(__name__, static_folder='templates', static_url_path='/')
from run_test import run_tests
CORS(app)

from school_data import SchoolData
from company_data import CompanyData

# Use the route() decorator to bind a function to a URL.
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tests')
def getTestResults():
    return run_tests()

@app.route('/api/school/<schoolname>')
def getSchoolInfo(schoolname):
    schoolData = SchoolData()
    return schoolData.getSchoolInfo(schoolname)

@app.route('/api/company/<companyname>')
def getCompanyInfo(companyname):
    companyData = CompanyData()
    return companyData.getCompanyInfo(companyname)

if __name__ == '__main__':
    app.run()

