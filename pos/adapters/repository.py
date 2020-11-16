from typing import Set, Protocol
from pos.domain import models



class AbstractRepository(Protocol):

    def add(self, company: models.Company):
        ...

    def get(self, id) -> models.Company:
        ...



class CompanyRepository:

    def __init__(self, repo: AbstractRepository): 
        self._repo = repo

    def add(self, company: models.Company):
        self._repo.add(company)        

    def get(self, id) -> models.Company:
        company = self._repo.get(id) 
        return company



class SqlAlchemyRepository:

    def __init__(self, session):
        self.session = session

    def add(self, company):
        self.session.add(company)

    def get(self, id):
        return self.session.query(models.Company).filter_by(id=id).first()