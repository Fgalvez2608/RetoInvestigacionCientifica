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
    categoria = input("Ingrese la categoría del experimento (ej 'fisica', 'quimica', 'biologia'): ").lower() #Variable que almacena la categoria del experimento y la funcion lower() lo convierte a minusculas
    while categoria == "": #bucle para validar que la categoria no este vacio
        print("ERROR!!! El campo de categoria no puede estar vacio.")#mensaje de error
        categoria = input("Ingrese la categoría del experimento: ").lower()
    resultados_str = input("Ingrese los resultados del experimento, un dato de otro separado por una coma ej (1,2,3,4): ") #Variable que almacena los resultados del experimento ingresados por el usuario de tipo string
    while resultados_str == "": #bucle para validar que los resultados no esten vacio
        print("ERROR!!! El campos resultados no puede estar vacio.")#mensaje de error
        resultados_str = input("Ingrese los resultados del experimento, un dato de otro separado por una coma ej (1,2,3,4): ")
    try: #try y except para validar el formato de los datos
        resultados = list(map(float, resultados_str.split(","))) #Variable que almacena los resultados del experimento ingresados por el usuario de tipo float, list para transformar el string en una lista de datos separados por coma ayudado por la funcion split y map para transformar los datos de la lista en float
        while len(resultados) < 3: #bucle para validar que la cantidad de datos ingresados sea mayor o igual a 3
            print("ERROR!!! La cantidad de datos ingresados debe ser mayor o igual a 3 para que se puedan analizar.")
            resultados_str = input("Ingrese los resultados del experimento, un dato de otro separado por una coma ej (1,2,3,4): ")
            try:
                resultados = list(map(float, resultados_str.split(",")))
            except ValueError:
                print("Formato de datos incorrecto. Por favor, ingrese una lista de números separados por comas.")
                return
    except ValueError:
        print("Formato de datos incorrecto. Por favor, ingrese una lista de números separados por comas.")
        return
    experimento = Experimento(nombre, fecha, categoria, resultados) #Variable que almacena los datos del experimento
    listaExperimentos.append(experimento) #linea de codigo que agrega los datos del experimento a la lista experimentos
    print("Experimento registrado exitosamente.")
    print("")

# 2. Funcion para visualizar resultados de los experimentos
def visualizarResultados(listaExperimentos):
    print("          ------ VISUALIZAR EXPERIMENTOS ------")
    if not listaExperimentos: #linea de codigo que verifica si la lista experimentos esta vacia
        print("No hay experimentos registrados.")
        return
    tablaExperimentos = PrettyTable() #Variable de tipo PrettyTable para almacenar los datos de cada experimento registrado por el usuario 
    tablaExperimentos.field_names = ["NOMBRE", "FECHA", "CATEGORIA", "DATOS"] #columnas de la tabla
    for experimento in listaExperimentos: #bucle para recorrer la lista experimentos y llena la tabla con los datos
        tablaExperimentos.add_row([experimento.nombre, experimento.fecha.strftime("%d/%m/%Y"), experimento.categoria, experimento.resultados], divider=True) #linea de codigo que agrega los datos de cada experimento a la tabla en sus respectivas columnas
    print(tablaExperimentos) #muestra la tabla en la consola
    print("")

# 3. Funcion para eliminar experimento
def eliminarExperimento(listaExperimentos):
    print(" ------ ELIMINAR EXPERIMENTO ------")
    if not listaExperimentos: #linea de codigo que verifica si la lista experimentos esta vacia
        print("No hay experimentos registrados.")
        return
    nombre = input("Ingrese el nombre del experimento que desea eliminar: ").lower() #Variable que almacena el nombre del experimento que desea eliminar
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
    print(" ------ COMPARADOR DE DATOS ------")
    if not listaExperimentos:
        print("No hay experimentos registrados.")
        return
    
    for experimento in listaExperimentos: #linea de codigo que recorre la lista experimentos e imprime el nombre de cada experimento
        print(f"{experimento.nombre}")
    cantidadExperimentos = int(input("Ingrese la cantidad de experimentos que desea comparar: ")) #Variable que almacena la cantidad de experimentos que desea comparar
    while cantidadExperimentos < 2: #bucle para validar que la cantidad de experimentos que desea comparar sea mayor o igual a 2
        print("ERROR!!! La cantidad de experimentos que desea comparar debe ser mayor o igual a 2.")#mensaje de error
        cantidadExperimentos = int(input("Ingrese la cantidad de experimentos que desea comparar: "))
    if cantidadExperimentos > len(listaExperimentos): #linea de codigo que verifica si la cantidad de experimentos que desea comparar es mayor a la cantidad de experimentos registrados
        print("ERROR!!! La cantidad de experimentos que deseas comparar sobrepasa la cantidad de experimentos registrados.")
        return

    experimentosComparar = [] #Variable que almacena los experimentos que desea comparar
    for i in range(cantidadExperimentos): #bucle para recorrer la cantidad de experimentos que desea comparar
        experimento = input(f"Ingrese el nombre del experimento {i + 1}: ") #Variable que almacena el nombre del experimento que desea comparar
        for exp in listaExperimentos: #bucle para recorrer la lista experimentos
            if exp.nombre == experimento: #linea de codigo que verifica si el nombre del experimento que desea comparar es igual al nombre de un experimento registrado
                experimentosComparar.append(exp) #linea de codigo que agrega el experimento a la lista experimentosComparar
                break
        else:
            print("Experimento no encontrado.")
            return
    # se calcula el promedio, el valor maximo y el valor minimo de los datos de cada experimento
    promediosComparar = [] #Variable que almacena los promedios de los experimentos que desea comparar
    maximosComparar = [] #Variable que almacena los valores maximos de los experimentos que desea comparar
    minimosComparar = [] #Variable que almacena los valores minimos de los experimentos que desea comparar
    for experimento in experimentosComparar: #bucle para recorrer la lista experimentosComparar
        promedio = statistics.mean(experimento.resultados) # se usa la funcion mean de la libreria statistics para calcular el promedio de los datos del experimento
        valorMaximo = max(experimento.resultados) # se usa la funcion max de la libreria statistics para calcular el valor maximo de los datos del experimento
        valorMinimo = min(experimento.resultados) # se usa la funcion min de la libreria statistics para calcular el valor minimo de los datos del experimento
        maximosComparar.append(valorMaximo) # se agrega el valor maximo a la lista maximosComparar
        minimosComparar.append(valorMinimo) # se agrega el valor minimo a la lista minimosComparar
        promediosComparar.append(promedio) # se agrega el promedio a la lista promediosComparar

    tablaComparar = PrettyTable() #Variable de tipo PrettyTable para almacenar los datos de cada experimento registrado por el usuario 
    tablaComparar.field_names = ["NOMBRE", "PROMEDIO", "MAXIMO", "MINIMO"] #columnas de la tabla
    for i in range(cantidadExperimentos): #bucle para recorrer la cantidad de experimentos que desea comparar
        tablaComparar.add_row([experimentosComparar[i].nombre, promediosComparar[i], maximosComparar[i], minimosComparar[i]], divider=True) #linea de codigo que agrega los datos de cada experimento a la tabla en sus respectivas columnas
    print(tablaComparar) #muestra la tabla en la consola
    print("")
    

# 6. Funcion para generar reporte con un archivo txt
def generarReporte(listaExperimentos):
    print(" ------ GENERAR REPORTE ------")
    if not listaExperimentos:
        print("No hay experimentos registrados.")
        print("")
        return
    
    #abrir un archivo txt
    with open("informeExperimentos.txt", "w") as archivo: #linea de codigo que abre el archivo "informeExperimentos.txt" en modo escritura
        for experimento in listaExperimentos:
            #escribir los detalles de cada experimento en el archivo
            archivo.write(f"Nombre del experimento: {experimento.nombre}\n") # se escribe en el archivo el nombre del experimento
            archivo.write(f"Fecha Ingresada: {experimento.fecha.strftime('%d/%m/%Y')}\n") # se escribe en el archivo la fecha del experimento
            archivo.write(f"Categoria: {experimento.categoria}\n") # se escribe en el archivo la categoria del experimento
            archivo.write(f"Datos: {experimento.resultados}\n") # se escribe en el archivo los resultados del experimento
            archivo.write(f"Promedio de los datos ingresados: {statistics.mean(experimento.resultados)}\n") # se escribe en el archivo el promedio del experimento
            archivo.write(f"Valor Maximo de los datos ingresados: {max(experimento.resultados)}\n") # se escribe en el archivo el valor maximo del experimento
            archivo.write(f"Valor Minimo de los datos ingresados: {min(experimento.resultados)}\n") # se escribe en el archivo el valor minimo del experimento
            archivo.write("\n") # se escribe en el archivo un espacio en blanco

    print("Reporte generado exitosamente, como 'informeExperimentos.txt'.")#mensaje de confirmacion de que el reporte se genero correctamente
    print("")

# 7. Funcion para menu principal
def menuPrincipal():
    listaExperimentos = [ # Variable de tipo lista que almacena experimentos
        Experimento("Experimento 1", datetime(2023, 10, 1), "Fisica", [10, 20, 30]),
        Experimento("Experimento 2", datetime(2023, 10, 2), "Quimica", [15, 25, 35]),
        Experimento("Experimento 3", datetime(2023, 10, 3), "Biologia", [12, 22, 32]),
        Experimento("Experimento 4", datetime(2023, 10, 4), "Matematicas", [18, 28, 38])
    ]
    
    while True: #bucle para repetir el menu principal
    
        try:
            print(" ------ MENU DE INVESTIGACION CIENTIFICA ------")
            print("1. GESTION DE EXPERIMENTOS")
            print("2. ANALISIS DE DATOS")
            print("3. GENERAR INFORME")
            print("4. CERRAR EL PROGRAMA")
            print("")

            opcionMenuPrincipal = input("Seleccione una opcion: ")#Variable que almacena la opcion que elija el usuario en el menu principal

            if opcionMenuPrincipal == "1":
                
                while True: #bucle para repetir el menu de gestion de experimentos
                    
                    try:
                        print(" ------ GESTION DE EXPERIMENTOS ------")
                        print("1. REGISTRAR EXPERIMENTO")
                        print("2. VISUALIZAR EXPERIMENTOS")
                        print("3. ELIMINAR EXPERIMENTO")
                        print("4. RETORNO AL MENU PRINCIPAL")
                        print("")

                        opcionMenuExperimento = input("Seleccione una opcion: ") #Variable que almacena la opcion que elija el usuario en el menu de gestion de experimentos

                        if opcionMenuExperimento == "1":
                            registrarExperimento(listaExperimentos)
                        elif opcionMenuExperimento == "2":
                            visualizarResultados(listaExperimentos)
                        elif opcionMenuExperimento == "3":  
                            eliminarExperimento(listaExperimentos)
                        elif opcionMenuExperimento == "4":
                            print("SALIENDO DEL MENU DE GESTION DE EXPERIMENTOS...")
                            print("")
                            break
                        else:
                            print("OPCION NO VALIDA")
                            print("POR FAVOR ELIJA UNA OPCION ENTRE 1 A 3")
                            print("")
                    except ValueError:
                        print("ERROR: OPCION NO VALIDA")
                        return

            elif opcionMenuPrincipal == "2":
                
                while True: #bucle para repetir el menu de gestion de experimentos
                    print(" ------ ANALIS DE DATOS ------")
                    print("1. CALCULO ESTADISTICO BASICO")
                    print("2. COMPARACION DE EXPERIMENTOS")
                    print("3. RETORNO AL MENU PRINCIPAL")
                    print("")

                    opcionMenuAnalisisDatos = input("Seleccione una opcion: ") #Variable que almacena la opcion que elija el usuario en el menu de gestion de experimentos

                    if opcionMenuAnalisisDatos == "1":
                        analisisResultados(listaExperimentos)
                    elif opcionMenuAnalisisDatos == "2":
                        compradorExperimentos(listaExperimentos)
                    elif opcionMenuAnalisisDatos == "3":
                        print("SALIENDO DEL MENU DE ANALISIS DE DATOS...")
                        break
                    else:
                        print("OPCION NO VALIDA")
                        print("POR FAVOR ELIJA UNA OPCION ENTRE 1 A 4")
                        print("")

            elif opcionMenuPrincipal == "3":
                generarReporte(listaExperimentos)
                
            elif opcionMenuPrincipal == "4":
                print("\nSALIENDO DEL PROGRAMA...")
                break

        except ValueError:
            print("ERROR!!!")
            return

if __name__ == "__main__": # linea de codigo que ejecuta la funcion principal
    menuPrincipal()










