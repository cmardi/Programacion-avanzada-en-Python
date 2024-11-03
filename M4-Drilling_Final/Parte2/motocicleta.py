        #-----CARLOS MAMANI-----#
# SISTEMA DE CONTROL DE VEHICULOS #

from dataclasses import dataclass
from Parte2.bicicleta import Bicicleta

@dataclass
class Motocicleta(Bicicleta):
    __nro_radios: int
    __cuadro: str
    __motor: str

    def __init__(self, marca: str, modelo: str, nro_ruedas: int, tipo: str, motor: str, cuadro: str, nro_radios: int):
        super().__init__(marca, modelo, nro_ruedas, tipo)  # Llamar al constructor de Bicicleta
        self.__motor = motor
        self.__cuadro = cuadro
        self.__nro_radios = nro_radios

    @property
    def nro_radios(self):
        return self.__nro_radios

    @property
    def cuadro(self):
        return self.__cuadro

    @property
    def motor(self):
        return self.__motor

    def __str__(self):
        return (f"{super().__str__()}, Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}")
