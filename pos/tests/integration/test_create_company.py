# pylint: disable=broad-except
import pytest
from pos.domain import models, value_objects
from pos.service_layer import services
from pos.adapters import orm
 
orm.start_mappers()

def test_create_company(): 
    uow =  services.unit_of_work.SqlAlchemyUnitOfWork()
    services.create_company('fiscal test name','comercial test name', 'XAXX010101000', uow)
    company_created = uow.companies.get(0)
    print(company_created.__dict__)
    assert company_created.rfc == value_objects.Rfc('XAXX010101000')