from pos.domain.value_objects import Rfc

class Company:
    id: int
    fiscal_name: str
    comercial_name: str
    rfc: Rfc
           
    def __init__(self, fiscal_name:str, comercial_name:str, rfc:str): 
        self.id = 0
        self.fiscal_name = fiscal_name
        self.comercial_name = comercial_name
        self.rfc = Rfc(rfc)    
