        #-----CARLOS MAMANI-----#
# SISTEMA DE CONTROL DE VEHICULOS #

from dataclasses import dataclass
from Parte1.vehiculo import Vehiculo

@dataclass
class Automovil(Vehiculo):
    __velocidad: int
    __cilindrada: int

    @property
    def velocidad(self):
        return self.__velocidad

    @property
    def cilindrada(self):
        return self.__cilindrada

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, Velocidad: {self.velocidad} km/h, Cilindrada: {self.cilindrada} cc"
