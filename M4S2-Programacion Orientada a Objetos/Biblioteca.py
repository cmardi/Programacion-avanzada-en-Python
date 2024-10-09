from tabulate import tabulate

class Libro:
    def __init__(self, id, titulo, autor):
        self.__id = id
        self.__titulo = titulo
        self.__autor = autor
        self.__disponible = True

    # Getters
    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def esta_disponible(self):    
        return self.__disponible

    # Setters
    def set_disponible(self, disponible):
        self.__disponible = disponible

    def prestar(self):
        if self.__disponible:
            self.set_disponible(False)
            return True
        return False

    def devolver(self):
        self.set_disponible(True)

    def obtener_info(self):
        return f"ID: {self.__id}, Título: {self.__titulo}, Autor: {self.__autor}"


class Usuario:
    def __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre
        self.__prestamos = []

    # Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def solicitar_prestamo(self, libro):
        if libro.prestar():
            self.__prestamos.append(libro)
            return True
        return False

    def devolver_libro(self, libro):
        if libro in self.__prestamos:
            libro.devolver()
            self.__prestamos.remove(libro)
            return True
        return False

    def obtener_prestamos(self):
        return [libro.obtener_info() for libro in self.__prestamos]


class Prestamo:
    def __init__(self, usuario, libro):
        self.__usuario = usuario
        self.__libro = libro

    def obtener_detalle(self):
        return f"Usuario: {self.__usuario.get_nombre()}, Libro: {self.__libro.obtener_info()}"


# Lista de Libros
libros = [
    Libro(1, "Cien Años de Soledad", "Gabriel García Márquez"),
    Libro(2, "Don Quijote de la Mancha", "Miguel de Cervantes"),
    Libro(3, "1984", "George Orwell"),
    Libro(4, "Crimen y Castigo", "Fiódor Dostoyevski"),
    Libro(5, "Matar a un Ruiseñor", "Harper Lee"),
    Libro(6, "El Amor en los Tiempos del Cólera", "Gabriel García Márquez"),
    Libro(7, "Rayuela", "Julio Cortázar"),
    Libro(8, "Orgullo y Prejuicio", "Jane Austen"),
    Libro(9, "La Odisea", "Homero"),
    Libro(10, "El Gran Gatsby", "F. Scott Fitzgerald")
]

# Lista de Usuarios
usuarios = [
    Usuario(1, "Juan Pérez"),
    Usuario(2, "Juan Silva"),
    Usuario(3, "Carlos Mamani"),
    Usuario(4, "Diego Aedo"),
    Usuario(5, "Genesis Marcano")
]

def obtener_id_valido(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Entrada no válida. Por favor, ingrese un número entero.")

def mostrar_libros():
    """Muestra la lista de libros en formato de tabla."""
    tabla = []
    for libro in libros:
        tabla.append([libro.get_id(), libro.get_titulo(), libro.get_autor(), "Disponible" if libro.esta_disponible() else "No disponible"])
    
    print(tabulate(tabla, headers=["ID", "Título", "Autor", "Disponibilidad"], tablefmt="grid"))

def menu():
    while True:
        print("\nBienvenido al sistema de administración de biblioteca")
        print("Selecciona una de las opciones:")
        print("1. Solicitar préstamo de libros")
        print("2. Devolver libros")
        print("3. Ver lista de libros")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id_libro = obtener_id_valido("Ingresa el ID del libro que deseas pedir prestado: ")
            id_usuario = obtener_id_valido("Ingresa tu ID de usuario: ")

            libro_seleccionado = next((libro for libro in libros if libro.get_id() == id_libro), None)
            usuario_seleccionado = next((usuario for usuario in usuarios if usuario.get_id() == id_usuario), None)

            if libro_seleccionado and usuario_seleccionado:
                if usuario_seleccionado.solicitar_prestamo(libro_seleccionado):
                    print(f"Préstamo realizado: {libro_seleccionado.obtener_info()} a {usuario_seleccionado.get_nombre()}.")
                else:
                    print("El libro no está disponible para préstamo.")
            else:
                print("Libro o usuario no encontrado.")

        elif opcion == '2':
            id_libro = obtener_id_valido("Ingresa el ID del libro que deseas devolver: ")
            id_usuario = obtener_id_valido("Ingresa tu ID de usuario: ")

            libro_seleccionado = next((libro for libro in libros if libro.get_id() == id_libro), None)
            usuario_seleccionado = next((usuario for usuario in usuarios if usuario.get_id() == id_usuario), None)

            if libro_seleccionado and usuario_seleccionado:
                if usuario_seleccionado.devolver_libro(libro_seleccionado):
                    print(f"Devolución realizada: {libro_seleccionado.obtener_info()} por {usuario_seleccionado.get_nombre()}.")
                else:
                    print("El libro no estaba prestado a este usuario.")
            else:
                print("Libro o usuario no encontrado.")

        elif opcion == '3':
            mostrar_libros()

        elif opcion == '4':
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción no válida. Por favor, ingrese un número para seleccionar una opción.")

# Ejecución del menú
menu()

