           # -----CARLOS MAMANI-----#
    #         HERENCIA MÚLTIPLE            #

class A:
    def __init__(self):
        pass        
        #print("Pertenezco a la clase A")
    def metodo_a(self):
        print("Método heredado de A")

class B:
    def __init__(self):
        print("Clase B")
    def metodo_b(self):
        print("Método heredado de B")

class C(B,A):
    def __init__(self):
        B.__init__(self)
        A.__init__(self)
    def metodo_c(self):
        print("Método de la clase C")

objeto_c = C()

objeto_c.metodo_a() 
objeto_c.metodo_b()
objeto_c.metodo_c()

