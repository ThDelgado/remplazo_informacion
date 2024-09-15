import time
import csv
import os



class Nota:  
    def __init__(self,  texto):
        self.texto = texto

    def guardar(self):
        nombre_archivo = "notas.txt"

        print(f"Guardando datos en {nombre_archivo}")
        try:
            with open (nombre_archivo, "a",  newline="\n") as documento: 
                writer = csv.writer(documento, delimiter=";") 
                writer.writerow([self.texto])
                time.sleep(1)
                print(f"Nota guardada correctamente en: {nombre_archivo}")
    
        except FileNotFoundError: 
            print(f"No se encuentra el archivo {nombre_archivo}") 
        except Exception as error: 
            print('Se ha generado un error no previsto', type(error).__name__)  
    
    @staticmethod
    def remplazar_dato(texto_viejo, texto_nuevo):  
        nombre_archivo = "notas.txt"
        try: 
            with open(nombre_archivo, 'r') as archivo:
                lineas = archivo.readlines()
           
            cantidad = 0
            with open(nombre_archivo, "w") as archivo:
                for index, linea in enumerate(lineas): 
                    nueva_linea = linea.replace(texto_viejo, texto_nuevo) 
                    archivo.write(nueva_linea)
                    if texto_viejo in linea:
                        cantidad += 1
            print(f"Se han realizado {cantidad} cambios en el texto ")


            #archivo_remplazo = open('Notas.txt', 'w') 
            #archivo_remplazo.write(remplazo) 
            #archivo_remplazo.close() 
        except FileNotFoundError: 
            print(f"No se encuentra el archivo {nombre_archivo}") 
        except Exception as error: 
            print('Se ha generado un error no previsto', type(error).__name__)     
        finally: 
            print("Se ha remplazado satisfactoriamente") 
    

    




texto1 = Nota("Hola Mundo" ) 
texto2 = Nota("Este en una nueva línea en el archivo" )
texto3 = Nota("agregando la segunda línea del archivo" )
texto4 = Nota("finalizando la línea agregada")
texto5 = Nota("Datos de informacion en la línea 1")
texto6 = Nota("Datos de informacion en la línea 2 ")
texto7 = Nota("Datos de informacion en la línea 3 ")
texto8 = Nota("Datos de informacion en la línea 4 ")
texto9 = Nota("Datos de informacion en la línea 5 ")



texto1.guardar()
texto2.guardar()
texto3.guardar()
texto4.guardar()
texto5.guardar()
texto6.guardar()
texto7.guardar()
texto8.guardar()
texto9.guardar()


Nota.remplazar_dato("informacion", "procedimiento")