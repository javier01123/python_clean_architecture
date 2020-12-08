from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date, ForeignKey,
    event, Numeric
)
from sqlalchemy.orm import mapper, relationship, composite
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
import sqlalchemy.types as types
from pos.domain import models, value_objects

# Base = declarative_base()

# class CompanyTable(models.Company, Base):
#     __tablename__ = 'companies'
        
#     id = Column(Integer, primary_key=True, autoincrement=True),
#     fiscal_name = Column(String(255)),
#     comercial_name = Column(String(255)),    
    # _rfc = Column('rfc',String(15))

    # @hybrid_property
    # def rfc(self) -> value_objects.Rfc:
    #     return value_objects.Rfc(self._rfc)

    # @rfc.setter
    # def rfc(self, rfc: value_objects.Rfc) -> None:
    #     self._rfc = rfc.value
 
# def start_mappers():     
#     mapper(models.Company, CompanyTable.__table__)
 

class UnaryValueObjectType(types.TypeDecorator):
    impl = Numeric

    def __init__(self, class_of_value_object, type):
        self.class_of_value_object = class_of_value_object
        self.type = type
        super(UnaryValueObjectType, self).__init__()

    def load_dialect_impl(self, dialect):
        return dialect.type_descriptor(self.type)

    def process_bind_param(self, value_object, dialect):
        if isinstance(value_object, self.class_of_value_object) and value_object is not None:
            value = value_object.value
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value_object = self.class_of_value_object(value)
        return value_object

metadata = MetaData()

companies = Table(
    'companies', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('fiscal_name', String(255)),
    Column('comercial_name', String(255)),    
    Column('rfc',  UnaryValueObjectType(value_objects.Rfc,String(15))),    
)

def start_mappers(): 
    mapper(models.Company, companies)
