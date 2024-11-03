from Parte1.automovil import Automovil
from Parte1.vehiculo import Vehiculo
from Parte2.particular import Particular
from Parte2.carga import Carga
from Parte2.bicicleta import Bicicleta
from Parte2.motocicleta import Motocicleta
from Parte3.manejo_datos import ManejoDatos

if __name__ == "__main__":
    print(f"Parte 1:\n")
    def solicitar_datos_automovil(num):
        print(f"\nDatos del automóvil {num}")
        while True:
            try:
                marca = input("Inserte la marca del automóvil: ")
                modelo = input("Inserte el modelo: ")
                nro_ruedas = int(input("Inserte el número de ruedas: "))
                velocidad = int(input("Inserte la velocidad en km/h: "))
                cilindrada = int(input("Inserte el cilindraje en cc: "))
                return marca, modelo, nro_ruedas, velocidad, cilindrada
            except ValueError as e:
                print(f"Error de entrada: {e}. Por favor ingrese datos válidos.")

    # Proceso 1: Solicitar datos para tres automóviles
    while True:
        try:
            cantidad = int(input("¿Cuántos vehículos desea insertar? "))
            break
        except ValueError as e:
            print(f"Error de entrada: {e}. Por favor ingrese un número válido.")
    vehiculos = []
    for i in range(1, cantidad + 1):
        marca, modelo, nro_ruedas, velocidad, cilindrada = solicitar_datos_automovil(i)
        vehiculo = Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada)
        vehiculos.append(vehiculo)
            
    # Imprimir los vehículos ingresados
    print("\nImprimiendo por pantalla los Vehículos:\n")
    for i, vehiculo in enumerate(vehiculos, 1):
        print(f"Datos del automóvil {i} : {vehiculo}")
        
    # Proceso 2:
    print(f"\nParte 2:") 
    try:
        # Crear instancias de vehículos adicionales
        particular = Particular("Ford", "Fiesta", 4, 180, 500, 5)
        carga = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000)
        bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
        motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

        # Mostrar por pantalla
        print(f"\nMarca {particular.marca}, Modelo {particular.modelo}, {particular.nro_ruedas} ruedas, {particular.velocidad} Km/h, {particular.cilindrada} cc, Puestos: {particular.nro_puestos}")
        print(f"Marca {carga.marca}, Modelo {carga.modelo}, {carga.nro_ruedas} ruedas, {carga.velocidad} Km/h, {carga.cilindrada} cc, Carga: {carga.peso_carga} Kg")
        print(f"Marca {bicicleta.marca}, Modelo {bicicleta.modelo}, {bicicleta.nro_ruedas} ruedas, Tipo: {bicicleta.tipo}")
        print(f"Marca {motocicleta.marca}, Modelo {motocicleta.modelo}, {motocicleta.nro_ruedas} ruedas, Tipo: {motocicleta.tipo}, Motor: {motocicleta.motor}, Cuadro: {motocicleta.cuadro}, Nro Radios: {motocicleta.nro_radios}")
    
    except Exception as e:
        print(f"Error al crear instancias de vehículos: {e}")
    
    try:    
        # Verificar relaciones
        print("\nVerificando relaciones de la instancia motocicleta:\n")
        print(f"Motocicleta es instancia con relación a Vehículo: {isinstance(motocicleta, Vehiculo)}")
        print(f"Motocicleta es instancia con relación a Automóvil: {isinstance(motocicleta, Automovil)}")
        print(f"Motocicleta es instancia con relación a Particular: {isinstance(motocicleta, Particular)}")
        print(f"Motocicleta es instancia con relación a Carga: {isinstance(motocicleta, Carga)}")
        print(f"Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta, Bicicleta)}")
        print(f"Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta, Motocicleta)}")

    except Exception as e:
        print(f"Error al verificar relaciones de instancias: {e}")

    # Proceso 3: 
    print(f"\nParte 3:")
    try:
        # Guardar vehículos en CSV
        manejo_datos = ManejoDatos()
        manejo_datos.guardar_datos_csv([particular, carga, bicicleta, motocicleta])

        print("\nLista de Vehículos desde el archivo CSV:\n")
        # Leer los datos desde el archivo CSV
        manejo_datos.leer_datos_csv()
        print()
        
    except Exception as e:
        print(f"Error al guardar o leer datos del CSV: {e}")