from dataclasses import dataclass
from Parte1.automovil import Automovil

@dataclass
class Carga(Automovil):
    __peso_carga: int

    @property
    def peso_carga(self):
        return self.__peso_carga

    def __str__(self):
        return f"{super().__str__()}, Carga: {self.peso_carga} Kg"
