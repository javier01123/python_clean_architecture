from pos.domain.value_objects import Rfc

class Empresa:
    razon_social: str
    nombre_comercial: str
    _rfc: Rfc
           
    def __init__(self, razon_social:str, nombre_comercial:str, rfc:str): 
        self.razon_social = razon_social
        self.nombre_comercial = nombre_comercial
        self._rfc = Rfc(rfc)    
