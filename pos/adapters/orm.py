from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date, ForeignKey,
    event
)
from sqlalchemy.orm import mapper, relationship,relation
from pos.domain import models, value_objects

metadata = MetaData()

companies = Table(
    'companies', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('fiscal_name', String(255)),
    Column('comercial_name', String(255)),
    Column('rfc', String(15)),
)
 
def start_mappers():
    # mapper(models.Company, companies, properties={'rfc':relation(value_objects.Rfc)})    
    mapper(models.Company, companies)
 
