#!/usr/bin/env python

'''
hardcoded company info data used before database was built
'''
class CompanyData:
    def __init__(self):
        pass

    def getCompanyInfo(self, companyName):
        companyData = {'name': companyName,
                       'date': 'not found',
                       'location': 'not found',
                       'business': 'not found',
                       'description': 'not found'}
        if companyName == 'intrexon':
            companyData = {'name': 'Intrexon, Inc (Now Precigen)',
                           'location': 'South San Francisco, Ca',
                           'date': '2017-05-15 - 2020-04-15',
                           'business': 'biotech',
                           'description': 'The MBP Titan division was trying to build a platform for creating chemicals from bacteria. '
                                          'My job was to work with the scientists who were performing screening on the bacteria and help them manage their workflow'}
        elif companyName == 'chordiant':
            companyData = {'name': 'Chordiant (Now Pegasystems)',
                           'date': '1999-03-01 - 2010-02-01',
                           'location': 'Cupertino, Ca',
                           'business': 'B2C software',
                           'description': 'Our team designed and maintained a customer service application framework using J2EE.'
                                          'My job included working with IBM to understand and improve their J2EE software, scrum master to several international teams,'
                                          'and work on the scalability of the product'}
        elif companyName == 'vmware':
            companyData = {'name': 'VMWare',
                           'date': '2010-04-01 - 2017-03-15',
                           'location': 'Palo Alto, Ca',
                           'business': 'Infrastructure Software',
                           'description': 'I worked on two teams there. First was the tools team. We built a variety of products'
                                          ' using Python, Django, Oracle, and MongoDB to allow product managers to better manage their processes. '
                                          'I was also responsible for the maintenance of our vCenter and Jenkins servers.  '
                                          'I also worked as a programmer and tester on the VxRail product.'}
        elif companyName == 'oceania':
            companyData = {'name': 'Oceania',
                           'date': '2010-2017',
                           'location': 'Palo Alto, Ca',
                           'business': 'Medical Software',
                           'description': 'Development of an Electronic Medical Record using C/C++. Worked closely with the'
                                          'doctors and product managers to define requirements and design to those requirements'}
        elif companyName == 'gte':
            companyData = {'name': 'GTE Government Systems',
                           'date': '1984-03-01 - 1996-02-01',
                           'location': 'Mountain View, Ca',
                           'business': 'Digital Signal Processing Software for the Government',
                           'description': 'I developed software to control and monitor DSP systems in Ada, which was a new programming language at the time. '
                                          'I also taught courses to the software engineers in MIL-STD-2167 and Digital Signal Processing'}
        elif companyName == 'llnl':
            companyData = {'name': 'Lawrence Livermore National Laboratory',
                           'date': '1978-07-01 - 1984-02-28',
                           'location': 'Livermore, Ca',
                           'business': 'R&D in Energy, Medicine, and Weapons Systems',
                           'description': 'I worked on a variety of projects, including a dual laser cell sorter, spent fuel '
                                          'repository monitoring system, and environmental testing of weapons'}
        elif companyName == 'niosh':
            companyData = {'name': 'National Institute of Occupational Safety and Health',
                           'date': '1976-06-01 - 1976-08-15',
                           'location': 'Cincinnati, OH',
                           'business': 'Medical Research into Industrial Hearing Problems  (internship)',
                           'description': 'Developed a signal amplifier for an otology lab. Also worked on an industrial hearing '
                                          'study and helped with data analysis'}
        elif companyName == 'attorney':
            companyData = {'name': 'Attorney At Law',
                           'date': '2007-06-01 - 2019-02-15',
                           'location': 'San Jose, CA',
                           'business': 'Family and Patent Law (retired)',
                           'description': 'Helped small companies file patents, volunteer Family Law Attorney at the Pro Bono Project'}
        return companyData

