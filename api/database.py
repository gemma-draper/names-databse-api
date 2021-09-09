#%%
from sqlalchemy import Column, Integer, String, DateTime, create_engine, update, delete
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.sql.selectable import Values
from sqlalchemy import Column, Integer, String, DateTime, create_engine, update, delete
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import os
import pandas as pd

def get_config_csv(filename):
    filepath = os.path.join(os.path.expanduser('~'), 'api-deployment', filename)
    return pd.read_csv(filepath)

def get_credentials(filename):

    credentials = get_config_csv(filename)
    username = credentials.iloc[0][0]
    password = credentials.iloc[0][1]
    return username, password

def get_rds_connection_details(filename):
    credentials = credentials = get_config_csv(filename)
    host = credentials.iloc[0][0]
    port = credentials.iloc[0][1]
    table = credentials.iloc[0][2]
        
    return host, port, table

rds_user, rds_password = get_credentials('sql_account_details.csv')
host, port, table = get_rds_connection_details('rds_connection.csv')

SQLALCHEMY_DATABASE_URI = f"postgresql://{rds_user}:{rds_password}@{host}:{port}/{table}"

class crud_helper():

    def __init__(self) -> None:
        
        self.engine = create_engine(self.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True, echo=False)
        self.rds_db = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=self.engine))

    class Name(declarative_base(bind=create_engine(SQLALCHEMY_DATABASE_URI, pool_pre_ping=True, echo=False))):
                """The `names`-table"""
                __tablename__ = "names"
                __table_args__ = {"schema": "public"}

                id = Column(Integer, primary_key=True, nullable=False)
                first_name = Column(String(64), nullable=False)
                last_name = Column(String(64), nullable=False)

    def read_record(self, first_name, last_name):
        name_query = self.rds_db.query(crud_helper.Name).with_entities(
            crud_helper.Name.id,crud_helper.Name.first_name,crud_helper.Name.last_name).filter(crud_helper.Name.id==id)   
        results_pd = pd.read_sql(name_query.statement, name_query.session.bind)
        return results_pd['id'],results_pd['first_name'], results_pd['last_name']

    def create_record(self, first_name, last_name):
        new_name = Name()
        new_name.first_name= first_name
        new_name.last_name= last_name
        self.rds_db.add(new_name)
        self.rds_db.commit()

    def delete_record(self, id):
        name_query = self.rds_db.delete(crud_helper.Name).with_entities(
            crud_helper.Name.id,crud_helper.Name.first_name,crud_helper.Name.last_name).filter(crud_helper.Name.id==id)   
        self.rds_db.flush()


# %%
