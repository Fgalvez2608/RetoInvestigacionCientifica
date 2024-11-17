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
    pass

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










