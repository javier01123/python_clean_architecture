from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date, ForeignKey,
    event,
)
from sqlalchemy.orm import mapper, relationship
from pos.domain import models

metadata = MetaData()

companies = Table(
    'companies', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('fiscal_name', String(255)),
    Column('comercial_name', String(255)),
    Column('Rfc', String(13)),
)
 
def start_mappers():
    mapper(models.Company, companies)    
 