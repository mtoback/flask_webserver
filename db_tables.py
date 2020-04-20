#!/usr/bin/env python

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
'''
SQLAlchemy table definitions
'''
base = declarative_base()

class Company (base):
    __tablename__ = 'company'
    key_name = Column(String, primary_key=True)
    name = Column(String)
    location = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    description = Column(String)
    business = Column(String)

class School (base):
    __tablename__ = 'school'
    key_name = Column(String, primary_key=True)
    name = Column(String)
    location = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    description = Column(String)
    degree = Column(String)
