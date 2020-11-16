# pylint: disable=broad-except
import pytest
from pos.domain import models
from pos.service_layer import unit_of_work, services

 
 
# def test_create_company(session_factory): 
#     uow = unit_of_work.SqlAlchemyUnitOfWork(session_factory)
#     services.create_company('fiscal test name','comercial test name', 'XAXX010101000', uow)
#     assert