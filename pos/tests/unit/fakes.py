from pos.service_layer import unit_of_work
from pos.adapters import repository
from pos.domain import models

class FakeRepository(repository.AbstractRepository):

    def __init__(self, companies):
        self._companies = set(companies)

    def add(self, company):
        self._companies.add(company)

    def get(self, id):
        return next(b for b in self._companies if b.id == id)

    def list(self):
        return list(self._companies)

class FakeUnitOfWork(unit_of_work.AbstractUnitOfWork):

    def __init__(self):
        self.companies = FakeRepository([])
        self.committed = False

    def _commit(self):
        self.committed = True

    def rollback(self):
        pass