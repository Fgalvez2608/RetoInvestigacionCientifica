from datetime import datetime
import statistics

class Experimento:  # Clase que representa un experimento.

    def __init__(self, nombre, fechaRealizacion, categoria):  # Constructor de la clase Experimento.
        self.nombre = nombre  # Atributo que representa el nombre del experimento.
        self.fechaRealizacion = fechaRealizacion  # Atributo que representa la fecha de realización del experimento.
        self.categoria = categoria  # Atributo que representa la categoría del experimento.
        self.resultados = []  # Atributo que representa la lista de resultados del experimento.

# 1. Funcion para registrar experimento
def registrarExperimento(listaExperimentos):  # Función que permite registrar un experimento en la lista de experimentos.
    nombre = input('Ingrese el nombre del experimento: ')  # Variable que almacena el nombre del experimento ingresado
    fecha_realizacion = input('Ingrese la fecha de realización del experimento (DD/MM/AAAA): ')  # Variable que almacena la fecha de realización del experimento ingresada

    try:  # Manejo de error en caso de que la fecha ingresada no sea válida.
        fechaRealizacion = datetime.strptime(fecha_realizacion, '%d/%m/%Y')
    except ValueError:
        print('La fecha ingresada no es válida. Por favor, ingrese una fecha válida en el formato DD/MM/AAAA.')
        return

    categoria = input('Ingrese la categoría del experimento (ejemplo: "Química", "Biología" o "Física"): ')  # Variable que almacena la categoría del experimento ingresada

    resultados = []  # Variable que almacena la lista de resultados numéricos
    num_resultados = int(input('Ingrese el número de resultados numéricos del experimento: '))

    for i in range(num_resultados):  # Iterar sobre el número de resultados numéricos ingresados y pedir al usuario que ingrese cada resultado.
        resultado = float(input(f'Ingrese el resultado numérico {i+1}: '))
        resultados.append(resultado)  # Los resultados se almacenan en una lista.

    experimento = Experimento(nombre, fechaRealizacion, categoria)  # Creación de un objeto de la clase Experimento
    experimento.resultados = resultados  # Asignar los resultados al objeto experimento
    listaExperimentos.append(experimento)  # Agregar el objeto a la lista de experimentos

    print(f'\nEl experimento {nombre} ha sido registrado.')


# 2. Funcion para visualizar resultados de los experimentos
def visualizarResultados(listaExperimentos):
    #trabajando
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










