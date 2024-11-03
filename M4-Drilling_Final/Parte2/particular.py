from dataclasses import dataclass
from Parte1.automovil import Automovil

@dataclass
class Particular(Automovil):
    __nro_puestos: int

    @property
    def nro_puestos(self):
        return self.__nro_puestos

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, Puestos: {self.nro_puestos}"
