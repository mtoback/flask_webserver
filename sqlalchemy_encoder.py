#!/usr/bin/env python

import json

from sqlalchemy.ext.declarative import DeclarativeMeta

'''
special class to convert sqlalchemy objects into json objects
note the simple 'hack' to handle date objects, needed because they
are not serializable. In a future iteration one might need to do more
than just convert to a string
'''
class SQLAlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = str(data)
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)
