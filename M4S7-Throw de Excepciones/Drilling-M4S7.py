#---------------------CARLOS MAMANI-----------------------#
#--------------M4S7THROW de Excepciones-------------------#

class RangoSalarioError(Exception):
    def __init__(self, salario, mensaje="Salario no está definido en el rango (1000 a 2000)"):
        self.salario = salario
        self.mensaje = f"{salario} -> {mensaje}"
        super().__init__(self.mensaje)

def ingresar_salario():
    try:
        salario = int(input("Ingrese el salario: "))
        if salario < 1000 or salario > 2000:
            raise RangoSalarioError(salario)
        print(f"Salario ingresado: {salario}")
    except RangoSalarioError as error:
        print(f"Traceback (most recent call last):")
        print(f"  File \"drilling-CUE07.py\", line 20, in <module>")
        print(f"    raise RangoSalarioError({salario})")
        print(f"__main__.RangoSalarioError: {error}")

ingresar_salario()
