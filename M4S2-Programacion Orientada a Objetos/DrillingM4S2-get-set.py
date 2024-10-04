class Persona:
    def __init__(self, nombre, apellido, sexo, edad, estatura, peso ):
        self._nombre = nombre
        self._apellido = apellido
        self._sexo = sexo
        self._edad = edad 
        self._estatura = estatura
        self._peso = peso

    def set_nombre(self, nombre):
        self._nombre = nombre
    def set_apellido(self, apellido):
        self._apellido = apellido
    def set_sexo(self, sexo):
        self._sexo = sexo
    def set_edad(self, edad):
        self._edad = edad
    def set_estatura(self, estatura):
        self._estatura = estatura
    def set_peso(self, peso):
        self._peso = peso
    def get_edad(self):
        return self._edad
    def get_apellido(self):
        return self._apellido

    def __str__(self):
        return (f"Nombre: {self._nombre} {self._apellido}\n"
                f"Sexo: {self._sexo}\n"
                f"Edad: {self._edad}\n"
                f"Estatura: {self._estatura}\n"
                f"Peso: {self._peso}")

persona_1 = Persona("Pedro", "Vivas", "Masculino", "20 años", "1.78 mts", "68 Kg.")
persona_2 = Persona("Juan", "Camargo", "Masculino", "18 años", "1.8 mts", "75 Kg.\n")

print("\nAntes de las modificaciones:")
print(persona_1)
print()
print(persona_2)

persona_1.set_edad("21 años")
persona_2.set_apellido("Santiago")

print("Después de las modificaciones:")
print(persona_1)
print()
print(persona_2)
    