#!/usr/bin/env python

import yaml
'''
Gets the (non-controlled) secret data and incorporates it into the application
This means that a file called 'secrets.yaml' must be created where the application is built 
so that it can be incorporated into the application to get the 'environment variables' that 
need to be defined outside of the codebase for security reasons.
'''
class SecretData():
    def __init__(self):
        f = open('secrets.yml')
        self._data = yaml.load(f.read(), Loader=yaml.CBaseLoader)
    def getValue(self,key):
        return self._data[key]
