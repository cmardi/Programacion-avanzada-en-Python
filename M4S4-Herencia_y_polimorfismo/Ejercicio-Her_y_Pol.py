            #-----CARLOS MAMANI-----#
# CONSTRUCCIÓN DE CLASES Y HERENCIA MÚLTIPLE #

class Libro:
    #Asigna autor y título a los atributos del objeto
    def __init__(self, autor, titulo, ann_de_publicacion=None):
        #Renombra los atributos
        self.autor = autor
        self.titulo = titulo
        
        # Asigna year_of_publishment si se proporciona un valor
        if ann_de_publicacion is not None:
            self.year_of_publishment = ann_de_publicacion
        
# Se generan instancias de la clase Libro
libro_1 = Libro(autor='Dan Brown', titulo='Infierno') # Se crea libro_1 sin year_of_publishment
libro_2 = Libro(autor='Dan Brown', titulo='El Código Da Vinci', ann_de_publicacion=2003) # Se crea libro_2 con year_of_publishment
        
# Imprimir los atributos
print(libro_1.__dict__)
print(libro_2.__dict__)



