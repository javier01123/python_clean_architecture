# pylint: disable=broad-except
import pytest
from pos.domain import models, value_objects
from pos.service_layer import services

import fakes

 
 
def test_create_company(): 
    uow = fakes.FakeUnitOfWork()
    services.create_company('fiscal test name','comercial test name', 'XAXX010101000', uow)
    company_created = uow.companies.get(0)
    print(company_created.__dict__)
    assert company_created.rfc == value_objects.Rfc('XAXX010101000')