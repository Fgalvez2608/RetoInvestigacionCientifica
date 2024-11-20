from datetime import datetime
import statistics

class Experimento:  # Clase que representa un experimento.

    def __init__(self, nombre, fechaRealizacion, categoria):  # Constructor de la clase Experimento.
        self.nombre = nombre  # Atributo que representa el nombre del experimento.
        self.fechaRealizacion = fechaRealizacion  # Atributo que representa la fecha de realización del experimento.
        self.categoria = categoria  # Atributo que representa la categoría del experimento.
        self.resultados = []  # Atributo que representa la lista de resultados del experimento.


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


def visualizarResultados(listaExperimentos):  # Función para visualizar resultados de los experimentos
    if not listaExperimentos:  # Verificar si la lista de experimentos está vacía.
        print('No hay experimentos registrados.')
        return

    for i, experimento in enumerate(listaExperimentos, start=1):  # Iterar sobre la lista de experimentos y mostrar los resultados.
        print(f'\n Experimento {i}:')
        print(f' Nombre: {experimento.nombre}')  # Muestra nombre de experimento
        print(f' Fecha de realización: {experimento.fechaRealizacion.strftime("%d/%m/%Y")}')  # Muestra fecha de realización
        print(f' Categoría: {experimento.categoria}')  # Muestra la categoría del experimento
        print(f' Resultados: {experimento.resultados}')  # Muestra la lista de resultados


def eliminarExperimento(listaExperimentos):  # Función para eliminar experimento
    if not listaExperimentos:  # Verificar si la lista de experimentos está vacía.
        print('No hay experimentos registrados.')
        return

    nombreExperimento = input('Ingrese el nombre del experimento a eliminar: ')  # Variable que almacena el nombre del experimento ingresado.

    for experimento in listaExperimentos:  # Iterar sobre la lista de experimentos y verificar si el nombre coincide.
        if experimento.nombre.lower() == nombreExperimento.lower():  # Verificar si el nombre del experimento coincide.
            listaExperimentos.remove(experimento)  # Eliminar el experimento de la lista.
            print(f'El experimento {nombreExperimento} ha sido eliminado.')
            return

    print(f'No se encontró el experimento {nombreExperimento}.')  # Mostrar un mensaje en caso de que no se encuentre el experimento.


def analisisResultados(listaExperimentos):  # Función para cálculo estadístico básico (PROMEDIO - VALOR MÁXIMO - VALOR MÍNIMO).
    if not listaExperimentos:  # Verificar si la lista de experimentos está vacía.
        print('No hay experimentos registrados.')
        return

    fechas = [experimento.fechaRealizacion for experimento in listaExperimentos]  # Crear una lista de fechas de realización de los experimentos

    promedio = statistics.mean([fecha.timestamp() for fecha in fechas])  # Calcular el promedio de las fechas de realización

    maximo = max(fechas)  # Calcular la fecha de realización máxima

    minimo = min(fechas)  # Calcular la fecha de realización mínima

    print(f'\nPromedio de fechas de realización: {datetime.fromtimestamp(promedio).strftime("%d/%m/%Y")}')  # Imprimir el promedio de fechas de realización en formato DD/MM/AAAA

    print(f'Fecha de realización máxima: {maximo.strftime("%d/%m/%Y")}')  # Imprimir la fecha de realización máxima en formato DD/MM/AAAA

    print(f'Fecha de realización mínima: {minimo.strftime("%d/%m/%Y")}')  # Imprimir la fecha de realización mínima en formato DD/MM/AAAA


def compararExperimentos(listaExperimentos):  # Función para comparar los resultados de 2 o más experimentos
    if len(listaExperimentos) < 2:  # Verificar si hay al menos 2 experimentos
        print('Se necesitan al menos 2 experimentos para comparar.')
        return

    nombre1 = input('Ingrese el nombre del primer experimento a comparar: ')  # Pedir el nombre del primer experimento a comparar

    nombre2 = input('Ingrese el nombre del segundo experimento a comparar: ')  # Pedir el nombre del segundo experimento a comparar

    experimento1 = next((exp for exp in listaExperimentos if exp.nombre.lower() == nombre1.lower()), None)  # Buscar el primer experimento en la lista

    experimento2 = next((exp for exp in listaExperimentos if exp.nombre.lower() == nombre2.lower()), None)  # Buscar el segundo experimento en la lista

    if not experimento1 or not experimento2:  # Verificar si se encontraron ambos experimentos
        print('Uno o ambos experimentos no fueron encontrados.')
        return

    resultados1 = experimento1.resultados  # Obtener los resultados del primer experimento

    resultados2 = experimento2.resultados  # Obtener los resultados del segundo experimento

    # Calcular el promedio de los resultados de cada experimento
    promedio1 = statistics.mean(resultados1)
    promedio2 = statistics.mean(resultados2)

    # Verificar si el promedio de los resultados es mayor en el primer experimento o en el segundo
    if promedio1 > promedio2:
        print(f'El experimento {experimento1.nombre} tiene los mejores resultados con un promedio de {promedio1}')
    elif promedio1 < promedio2:
        print(f'El experimento {experimento2.nombre} tiene los mejores resultados con un promedio de {promedio2}')
    else:
        print(f'Los experimentos {experimento1.nombre} y {experimento2.nombre} tienen los mismos resultados con un promedio de {promedio1}')


def generarReporte(listaExperimentos):  # Función para generar reporte con un archivo txt
    if not listaExperimentos:  # Verificar si la lista de experimentos está vacía.
        print('No hay experimentos registrados.')
        return

    with open('reporte.txt', 'w') as archivo:  # Abrir un archivo llamado 'reporte.txt' en modo escritura.
        for experimento in listaExperimentos:  # Iterar sobre cada experimento en la lista.
            archivo.write(f'Experimento: {experimento.nombre}\n')  # Escribir el nombre del experimento en el archivo.
            archivo.write(f'Fecha de realización: {experimento.fechaRealizacion.strftime("%d/%m/%Y")}\n')  # Escribir la fecha de realización del experimento en el archivo.
            archivo.write(f'Categoría: {experimento.categoria}\n')  # Escribir la categoría del experimento en el archivo.
            archivo.write(f'Resultados: {experimento.resultados}\n')  # Escribir los resultados del experimento en el archivo.
            archivo.write('\n')  # Escribir una línea en blanco para separar los experimentos.

    print('Informe generado en el archivo "reporte.txt" exitosamente')


def menu(listaExperimentos):  # Función para el menú principal
    while True:
        print("\nMenu de opciones:")
        print("1. Agregar un experimento")
        print("2. Ver experimentos registrados")
        print("3. Eliminar un experimento")
        print("4. Realizar un análisis de los experimentos")
        print("5. Comparar 2 o más experimentos")
        print("6. Generar informe de experimentos")
        print("7. Salir")

        opcion = int(input("Ingrese una opción (entre 1 y 7): "))

        if opcion < 1 or opcion > 7:
            print("Opción no válida, ingrese un número entre 1 y 7")
        elif opcion == 1:
            registrarExperimento(listaExperimentos)
        elif opcion == 2:
            visualizarResultados(listaExperimentos)
        elif opcion == 3:
            eliminarExperimento(listaExperimentos)
        elif opcion == 4:
            analisisResultados(listaExperimentos)
        elif opcion == 5:
            compararExperimentos(listaExperimentos)
        elif opcion == 6:
            generarReporte(listaExperimentos)
        elif opcion == 7:
            print("¡Gracias por utilizar el programa!")
            break

if __name__ == "__main__":
    listaExperimentos = []
    menu(listaExperimentos)
