from dataclasses import dataclass
from Parte1.vehiculo import Vehiculo

@dataclass
class Bicicleta(Vehiculo):
    __tipo: str

    @property
    def tipo(self):
        return self.__tipo

    def __str__(self):
        return f"{super().__str__()}, Tipo: {self.tipo}"
