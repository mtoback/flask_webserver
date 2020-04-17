import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_tables import Company
from secret_data import SecretData
from sqlalchemy_encoder import SQLAlchemyEncoder


class DBProcessing():
    def __init__(self):
        secretData = SecretData()
        db_string = secretData.getValue('db_string')
        _db = create_engine(db_string)
        self._Session = sessionmaker(_db)
        self._Session.configure(bind=_db)
    def get_company(self, companyName):

        session = self._Session()
        companyData = session.query(Company).filter(Company.key_name == companyName).first()
        return json.dumps(companyData, cls=SQLAlchemyEncoder)
        # return self._db.execute(f"SELECT name,location,business,start_date,end_date,description FROM company where key_name='{companyName}'" ).first()
if __name__ == "__main__":
    dbProc = DBProcessing()
    print(dbProc.get_company('llnl'))


