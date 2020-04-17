
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
base = declarative_base()

class Company (base):
    __tablename__ = 'company'

    key_name = Column(String, primary_key=True)
    name = Column(String)
    location = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    business = Column(String)
