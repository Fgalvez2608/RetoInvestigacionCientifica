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
    print(" ------ VISUALIZAR EXPERIMENTOS ------")
    if not listaExperimentos: #linea de codigo que verifica si la lista experimentos esta vacia
        print("No hay experimentos registrados.")
        return
    tablaExperimentos = PrettyTable() #Variable de tipo PrettyTable para almacenar los datos de cada experimento registrado por el usuario 
    tablaExperimentos.field_names = ["NOMBRE", "FECHA", "CATEGORIA", "DATOS"] #columnas de la tabla
    for experimento in listaExperimentos: #bucle para recorrer la lista experimentos
        tablaExperimentos.add_row([experimento.nombre, experimento.fecha.strftime("%d/%m/%Y"), experimento.categoria, experimento.resultados], divider=True) #linea de codigo que agrega los datos de cada experimento a la tabla en sus respectivas columnas
    print(tablaExperimentos) #muestra la tabla en la consola
    print("")

# 3. Funcion para eliminar experimento
def eliminarExperimento(listaExperimentos):
    print(" ------ ELIMINAR EXPERIMENTO ------")
    if not listaExperimentos: #linea de codigo que verifica si la lista experimentos esta vacia
        print("No hay experimentos registrados.")
        return
    nombre = input("Ingrese el nombre del experimento que desea eliminar: ") #Variable que almacena el nombre del experimento que desea eliminar
    for experimento in listaExperimentos: #bucle para recorrer la lista experimentos
        if experimento.nombre == nombre: #linea de codigo que verifica si el nombre del experimento que desea eliminar es igual al nombre de un experimento registrado
            listaExperimentos.remove(experimento) #linea de codigo que elimina el experimento de la lista experimentos
            print("Experimento eliminado exitosamente.")
            print("")
            return
    print("Experimento no encontrado.")
    print("")

# 4. Funcion para calculo estadistico basico (PROMEDIO - VALOR MAXIMO - VALOR MINIMO).
def analisisResultados(listaExperimentos):
    print(" ------ ANALISIS EXPERIMENTOS ------")
    if not listaExperimentos:
        print("No hay experimentos registrados.")
        return
    
    tablaAnalisis = PrettyTable() #Variable de tipo PrettyTable para almacenar los datos de cada experimento registrado por el usuario
    tablaAnalisis.field_names = ["NOMBRE", "FECHA", "CATEGORIA", "PROMEDIO", "DATO MAXIMO", "DATO MINIMO"] #columnas de la tabla
    for experimento in listaExperimentos: #bucle para recorrer la lista experimentos
        promedio = statistics.mean(experimento.resultados) # se usa la funcion mean de la libreria statistics para calcular el promedio de los datos del experimento
        maximo = max(experimento.resultados) # se usa la funcion max de la libreria statistics para calcular el valor maximo de los datos del experimento
        minimo = min(experimento.resultados) # se usa la funcion min de la libreria statistics para calcular el valor minimo de los datos del experimento
        tablaAnalisis.add_row([experimento.nombre, experimento.fecha.strftime("%d/%m/%Y"), experimento.categoria, promedio, maximo, minimo], divider=True) # se usa la funcion add_row de la libreria prettytable para agregar los datos del experimento a la tabla

    print(tablaAnalisis) # se muestra la tabla "tablaAnalisis" en la consola HAHAHAHH
    print("")

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










