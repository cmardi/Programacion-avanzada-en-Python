from dataclasses import dataclass

@dataclass
class Vehiculo:
    __marca: str
    __modelo: str
    __nro_ruedas: int

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    @property
    def nro_ruedas(self):
        return self.__nro_ruedas

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, {self.nro_ruedas} ruedas"
