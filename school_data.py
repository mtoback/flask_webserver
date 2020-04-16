class SchoolData():
    def __init__(self):
        pass

    def getSchoolInfo(self, schoolname):
        schoolData = {'name': schoolname,
                      'date': 'not found',
                      'location': 'not found',
                      'degree': 'not found',
                      'description': 'not found'}
        if schoolname == 'rpi':
            schoolData = {'name': 'Rensselaer Polytechnic Institute',
                          'date': '1973-1976',
                          'location': 'Troy, NY',
                          'degree': 'BS BiomedEng',
                          'description': 'Project was an ultrasonic flow measurement device'}
        elif schoolname == 'cmu':
            schoolData = {'name': 'Carnegie-Mellon University',
                          'date': '1976-1978',
                          'location': 'Pittsburgh, PA',
                          'degree': 'MSEE & MSBioEng',
                          'description': 'Masters project was a device to convert eye movements to pulses for communication'}
        return schoolData
