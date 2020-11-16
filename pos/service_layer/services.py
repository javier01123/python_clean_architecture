
from pos.domain import models
from pos.service_layer import unit_of_work

def create_company(fiscal_name: str,comercial_name:str,rfc:str,uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        company = models.Company(fiscal_name, comercial_name, rfc)
        uow.companies.add(company)
        uow.commit()

