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
    while True:
        nombre = input('Ingrese el nombre del experimento: ')  # Variable que almacena el nombre del experimento ingresado
        fecha_realizacion = input('Ingrese la fecha de realización del experimento (DD-MM-AAAA): ')  # Variable que almacena la fecha de realización del experimento ingresada

        try:  # Manejo de error en caso de que la fecha ingresada no sea válida.
            fechaRealizacion = datetime.strptime(fecha_realizacion, '%d-%m-%Y')
            break
        except ValueError:
            print('La fecha ingresada no es válida. Por favor, ingrese una fecha válida en el formato DD/MM/AAAA.')
            continue

    categoria = input('Ingrese la categoría del experimento (ejemplo: "Química", "Biología" o "Física"): ')  # Variable que almacena la categoría del experimento ingresada

    resultados = []  # Variable que almacena la lista de resultados numéricos
    num_resultados = int(input('Ingrese el número de resultados numéricos del experimento: '))

    for i in range(num_resultados):  # Iterar sobre el número de resultados numéricos ingresados y pedir al usuario que ingrese cada resultado.
        while True:
            try:
                resultado = float(input(f'Ingrese el resultado numérico {i+1}: '))
                break
            except ValueError:
                print('El resultado ingresado no es un n ́umero. Por favor, ingrese un n ́umero.')
        resultados.append(resultado)  # Los resultados se almacenan en una lista.

    experimento = Experimento(nombre, fechaRealizacion, categoria)  # Creación de un objeto de la clase Experimento
    experimento.resultados = resultados  # Asignar los resultados al objeto experimento
    listaExperimentos.append(experimento)  # Agregar el objeto a la lista de experimentos

    print(f'\nEl experimento {nombre} ha sido registrado.')


# 2. Funcion para visualizar resultados de los experimentos
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


# 3. Funcion para eliminar experimento
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


# 4. Funcion para calculo estadistico basico (PROMEDIO - VALOR MAXIMO - VALOR MINIMO).
def analisisResultados(listaExperimentos):  # Función para cálculo estadístico básico (PROMEDIO - VALOR MÁXIMO - VALOR MÍNIMO) de los resultados numéricos.
    if not listaExperimentos:  # Verificar si la lista de experimentos está vacía.
        print('No hay experimentos registrados.')
        return

    resultados = [resultado for experimento in listaExperimentos for resultado in experimento.resultados]  # Crear una lista de resultados

    promedio = statistics.mean(resultados)  # Calcular el promedio de los resultados

    maximo = max(resultados)  # Calcular el resultado numérico máximo

    minimo = min(resultados)  # Calcular el resultado numérico mínimo

    print(f'\nPromedio de resultados numéricos: {promedio:.2f}')  # Imprimir el promedio de resultados numéricos con 2 decimales

    print(f'Resultado numérico máximo: {maximo:.2f}')  # Imprimir el resultado numérico máximo con 2 decimales

    print(f'Resultado numérico mínimo: {minimo:.2f}')  # Imprimir el resultado numérico mínimo con 2 decimales


# 5. Funcion para comprar 2 o mas experimentos
def compradorExperimentos(listaExperimentos):
    # lista para almacenar los experimentos seleccionados para comparar
    experimentos_a_comparar = []
    while True:
        # mostrar el menú de comparación de experimentos
        print("\nSubmenú de comparación de experimentos")
        print("1. Seleccionar experimento para comparar")
        print("2. Ver experimentos seleccionados")
        print("3. Comparar experimentos seleccionados")
        print("4. Salir")
        
        # pedir al usuario que ingrese la opción deseada
        try:
            opcion = int(input("Ingrese la opción(entre 1 y 4): "))
        except ValueError:
            print("Opción no válida, ingrese un número entre 1 y 4")
            continue
        
        if opcion == 1:
            # mostrar la lista de experimentos registrados
            print("\nLista de experimentos:")
            for i, experimento in enumerate(listaExperimentos, start=1):
                print(f"{i}. {experimento.nombre}")
                
            # pedir al usuario que seleccione un experimento
            try:
                seleccion = int(input("Ingrese el número del experimento a seleccionar: "))
                if seleccion < 1 or seleccion > len(listaExperimentos):
                    raise ValueError
            except ValueError:
                print("Selección no válida, ingrese un número de la lista")
                continue
            
            # agregar el experimento seleccionado a la lista de experimentos a comparar
            experimentos_a_comparar.append(listaExperimentos[seleccion - 1])
            print(f"Experimento '{listaExperimentos[seleccion - 1].nombre}' seleccionado para comparar")
            
        elif opcion == 2:
            if not experimentos_a_comparar: # verificar si hay experimentos seleccionados para comparar
                print("No hay experimentos seleccionados para comparar")
            else:
                print("\nExperimentos seleccionados para comparar:") # mostrar los experimentos seleccionados para comparar
                for i, experimento in enumerate(experimentos_a_comparar, start=1):
                    print(f"Experimento {i}: {experimento.nombre}")
            
        elif opcion == 3:
            if len(experimentos_a_comparar) < 2: # verificar si hay al menos dos experimentos seleccionados para comparar
                print("Debe seleccionar al menos dos experimentos para comparar")
            else:
                print("\nComparación de experimentos: ") # mostrar la comparación de los experimentos seleccionados
                resultados = [] # crear una lista para almacenar los resultados de cada experimento
                for experimento in experimentos_a_comparar:
                    resultados.append(statistics.mean(experimento.resultados)) # calcular el promedio de los resultados de cada experimento
                print(f"Promedio de resultados de los experimentos seleccionados: {statistics.mean(resultados):.2f}") # mostrar el promedio de los resultados de los experimentos seleccionados
        elif opcion == 4:
            # salir del menú de comparación de experimentos
            break
        else:
            # mostrar un mensaje en caso de que la opción ingresada sea inválida
            print("Opción inválida. Por favor, ingrese una opción válida.")


# 6. Funcion para generar reporte con un archivo txt
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


# 7. Funcion para menu principal
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
            compradorExperimentos(listaExperimentos)
        elif opcion == 6:
            generarReporte(listaExperimentos)
        elif opcion == 7:
            print("¡Gracias por utilizar el programa!")
            break

if __name__ == "__main__":
    listaExperimentos = []
    menu(listaExperimentos)











