
from ddd_architecture.domain.value_objects.rfc import Rfc

class Empresa:
    __create_key = object()
    __razon_social = ""
    __nombre_comercial = ""
    __rfc = None

    def __str__(self):
        print(self.__razon_social)
       
    def __init__(self,create_key, razon_social:str, nombre_comercial:str, rfc:str):
        assert(create_key == Empresa.__create_key), \
            "Los objetos [Empresa] deben ser creados a traves del método [create]"
        self.__razon_social = razon_social
        self.__nombre_comercial = nombre_comercial
        self.__rfc = Rfc.create(rfc)

    @classmethod
    def create(cls, razon_social:str, nombre_comercial:str, rfc:str):
        return Empresa(cls.__create_key, razon_social, nombre_comercial, rfc)