import csv
import ast
from Parte2.particular import Particular
from Parte2.carga import Carga
from Parte2.bicicleta import Bicicleta
from Parte2.motocicleta import Motocicleta

class ManejoDatos:

    def guardar_datos_csv(self, vehiculos):
        try:
            with open('vehiculos.csv', 'w', newline='') as archivo_csv:
                writer = csv.writer(archivo_csv)
                writer.writerow(["Clase", "Datos"])
                for vehiculo in vehiculos:
                    clase = type(vehiculo).__name__
                    datos = {}
                    if isinstance(vehiculo, Particular):
                        datos = {
                            "marca": vehiculo.marca,
                            "modelo": vehiculo.modelo,
                            "nro_ruedas": str(vehiculo.nro_ruedas),
                            "velocidad": str(vehiculo.velocidad),
                            "cilindrada": str(vehiculo.cilindrada),
                            "nro_puestos": str(vehiculo.nro_puestos)
                        }
                    elif isinstance(vehiculo, Carga):
                        datos = {
                            "marca": vehiculo.marca,
                            "modelo": vehiculo.modelo,
                            "nro_ruedas": str(vehiculo.nro_ruedas),
                            "velocidad": str(vehiculo.velocidad),
                            "cilindrada": str(vehiculo.cilindrada),
                            "peso_carga": str(vehiculo.peso_carga)
                        }
                    elif isinstance(vehiculo, Bicicleta):
                        datos = {
                            "marca": vehiculo.marca,
                            "modelo": vehiculo.modelo,
                            "nro_ruedas": str(vehiculo.nro_ruedas),
                            "tipo": vehiculo.tipo
                        }
                    elif isinstance(vehiculo, Motocicleta):
                        datos = {
                            "marca": vehiculo.marca,
                            "modelo": vehiculo.modelo,
                            "nro_ruedas": str(vehiculo.nro_ruedas),
                            "tipo": vehiculo.tipo,
                            "motor": vehiculo.motor,
                            "cuadro": vehiculo.cuadro,
                            "nro_radios": str(vehiculo.nro_radios)
                        }
                    datos_str = str(datos).replace("'", '"')
                    writer.writerow([f"<class 'Vehiculo.{clase}'>", datos_str])
        except Exception as e:
            print(f"Error al guardar datos en CSV: {e}")
            
 
    def leer_datos_csv(self):
        try:
            with open('vehiculos.csv', 'r') as archivo_csv:
                reader = csv.reader(archivo_csv)
                next(reader)  # Skip header row
                vehiculos = {
                    'Particular': [],
                    'Carga': [],
                    'Bicicleta': [],
                    'Motocicleta': []
                }
                for row in reader:
                    clase, datos_str = row
                    datos = ast.literal_eval(datos_str)  # Usar ast.literal_eval() en lugar de eval()
                    print(f"Leído {clase}: {datos}") 
                    
                    if 'nro_puestos' in datos:
                        vehiculos['Particular'].append(datos)
                    elif 'peso_carga' in datos:
                        vehiculos['Carga'].append(datos)
                    elif 'tipo' in datos and all(key in datos for key in ['nro_ruedas']):
                        vehiculos['Bicicleta'].append(datos)
                    elif all(key in datos for key in ['tipo', 'motor', 'cuadro', 'nro_radios']):
                        vehiculos['Motocicleta'].append(datos)

                for tipo, lista_vehiculos in vehiculos.items():
                    print(f"Lista de Vehiculos {tipo}:")
                    for vehiculo in lista_vehiculos:
                        print(f" {vehiculo}")
        except Exception as e:
            print(f"Error al leer datos del CSV: {e}")

















    # def leer_datos_csv(self):
    #     try:
    #         with open('vehiculos.csv', 'r') as archivo_csv:
    #             reader = csv.reader(archivo_csv)
    #             next(reader)
    #             vehiculos = {
    #                 'Particular': [],
    #                 'Carga': [],
    #                 'Bicicleta': [],
    #                 'Motocicleta': []
    #             }
    #             for row in reader:
    #                 clase, datos_str = row
    #                 datos = ast.literal_eval(datos_str)  # Usar ast.literal_eval() en lugar de eval()
    #                 print(f"Leído {clase}: {datos}") 
                    
    #                 if 'nro_puestos' in datos:
    #                     vehiculos['Particular'].append(datos)
    #                 elif 'peso_carga' in datos:
    #                     vehiculos['Carga'].append(datos)
    #                 elif 'tipo' in datos and all(key in datos for key in ['nro_ruedas']):
    #                 #elif 'tipo' in datos:
    #                     vehiculos['Bicicleta'].append(datos)
    #                 elif all(key in datos for key in ['tipo', 'motor', 'cuadro', 'nro_radios']):
    #                     vehiculos['Motocicleta'].append(datos)
                    

    #             for tipo, lista_vehiculos in vehiculos.items():
    #                 print(f"Lista de Vehiculos {tipo}:")
    #                 for vehiculo in lista_vehiculos:
    #                     print(f" {vehiculo}")
    #     except Exception as e:
    #         print(f"Error al leer datos del CSV: {e}")