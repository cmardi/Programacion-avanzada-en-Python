            #-----CARLOS MAMANI-----#
#           HERENCIA MÚLTIPLE            #
from dataclasses import dataclass

@dataclass
class Persona:
        nombre: str
        apellido:str
        año: int

@dataclass
class Departamento:
        nombre_dpto: str
        nombre_corto_dpto: str

@dataclass
class Trabajador(Persona, Departamento):
        salario: float

trabajador = Trabajador("Juan", "Pérez", 2005, "Ingeniería de software", "IS", 20000)

print(trabajador.__dict__)
print("Es trabajador instancia de Persona:", isinstance(trabajador, Persona))
print("Es trabajador instancia de Departamento:", isinstance(trabajador, Departamento))
print("Es trabajador instancia de Trabajador:", isinstance(trabajador, Trabajador))