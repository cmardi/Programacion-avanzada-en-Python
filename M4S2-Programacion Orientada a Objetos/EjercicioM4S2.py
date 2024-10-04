class Animal:
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
    def __str__(self):
        return f"{self.nombre} es un {self.raza} de {self.edad} y pesa {self.peso}"
        
caballo = Animal("Zeus", "Pura sangre", "5 años", "450 kg.")
leon = Animal("Boulder", "Atlas", "10 años", "130 kg.")

print(caballo)
print(leon)