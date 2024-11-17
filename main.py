from datetime import datetime # importar la libreria datetime para darle formato a las fechas
import statistics # importar la libreria statistics para usar la funcion media
from prettytable import PrettyTable # importar la libreria prettytable para trabajar con tablas


class Experimento:  #funcion de inicializacion o metodo constructor, para recibir toda la informacion que se quiera almacenar
    def __init__(self, nombre, fecha, categoria, resultados):
        self.nombre = nombre
        self.fecha = fecha
        self.categoria = categoria
        self.resultados = resultados

# 1. Funcion para registrar experimento
def registrarExperimento(listaExperimentos):
    nombre = input("Ingrese el nombre del experimento: ").lower() #Variable que almacena el nombre del experimento y la funcion lower() lo convierte a minusculas
    while nombre == "": #bucle para validar que el nombre no este vacio 
        print("El nombre del experimento no puede estar vacio.")#mensaje de error
        nombre = input("Ingrese el nombre del experimento: ").lower()
    while True: #bucle para validar la fecha
        fecha_str = input("Ingrese la fecha del experimento (DD/MM/AAAA): ") #Variable que almacena la fecha del experimento en el formato DD/MM/AAAA ingresada por el usuario de tipo string
        try: #try y except para validar el formato de la fecha
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y") #Variable que almacena la fecha del experimento en el formato DD/MM/AAAA ingresada por el usuario de tipo datetime
            break
        except ValueError: #mensaje de error
            print("Formato de fecha incorrecto. Por favor, ingrese una fecha válida en el formato DD/MM/AAAA.")
    categoria = input("Ingrese la categoría del experimento: ").lower() #Variable que almacena la categoria del experimento y la funcion lower() lo convierte a minusculas
    while categoria == "": #bucle para validar que la categoria no este vacio
        print("ERROR!!! El campo de categoria no puede estar vacio.")#mensaje de error
        categoria = input("Ingrese la categoría del experimento: ").lower()
    resultados_str = input("Ingrese los resultados del experimento, un dato de otro separado por una coma ej (1,2,3,4): ") #Variable que almacena los resultados del experimento ingresados por el usuario de tipo string
    while resultados_str == "": #bucle para validar que los resultados no esten vacio
        print("ERROR!!! El campos resultados no puede estar vacio.")#mensaje de error
        resultados_str = input("Ingrese los resultados del experimento, un dato de otro separado por una coma ej (1,2,3,4): ")
        try: #try y except para validar el formato de los datos
                resultados = list(map(float, resultados_str.split(","))) #Variable que almacena los resultados del experimento ingresados por el usuario de tipo float, list para transformar el string en una lista de datos separados por coma ayudado por la funcion split y map para transformar los datos de la lista en float
        except ValueError:
            print("Formato de datos incorrecto. Por favor, ingrese una lista de números separados por comas.")
            return
    experimento = Experimento(nombre, fecha, categoria, resultados) #Variable que almacena los datos del experimento
    listaExperimentos.append(experimento) #linea de codigo que agrega los datos del experimento a la lista experimentos
    print("Experimento registrado exitosamente.")
    print("")

# 2. Funcion para visualizar resultados de los experimentos
def visualizarResultados(listaExperimentos):
    pass

# 3. Funcion para eliminar experimento
def eliminarExperimento(listaExperimentos):
    pass

# 4. Funcion para calculo estadistico basico (PROMEDIO - VALOR MAXIMO - VALOR MINIMO).
def analisisResultados(listaExperimentos):
    pass

# 5. Funcion para comprar 2 o mas experimentos
def compradorExperimentos(listaExperimentos):
    pass

# 6. Funcion para generar reporte con un archivo txt
def generarReporte(listaExperimentos):
    pass

# 7. Funcion para menu principal
def menuPrincipal():
    pass

if __name__ == "__main__": # linea de codigo que ejecuta la funcion principal
    menuPrincipal()










