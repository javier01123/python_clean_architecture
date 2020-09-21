
class Rfc:
    __create_key = object()
    __value = ""

    def __init__(self, create_key, rfc:str):
        assert(create_key == Rfc.__create_key), \
            "Los objetos [Rfc] deben ser creados a traves del método [create]"       
        self.__value = rfc

    @classmethod
    def create(cls, rfc:str):
        return Rfc(cls.__create_key, rfc)

