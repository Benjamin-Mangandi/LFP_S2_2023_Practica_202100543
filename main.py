#Funcion Cargar Inventario
materiales = []
def cargar_inventario(datos_inventario):
    inventario = open("Prueba.INV", 'r')
    for linea in inventario:
        aux_separar_lineas = linea.split(" ")
        aux_separar_datos = aux_separar_lineas[1]
        aux_datos_finales = aux_separar_datos.split(";")
        datos_inventario.append(aux_datos_finales)
    print(datos_inventario)    
    return

def cargar_movimientos(datos_inventario):
    inventario = open("Prueba.mov", 'r')
    materiales_agregar = []
    for linea in inventario:
        aux_separar_lineas = linea.split(" ")
        aux_separar_datos = aux_separar_lineas[1]
        aux_datos_finales = aux_separar_datos.split(";")
        materiales_agregar.append(aux_datos_finales)
    print(materiales_agregar)
    for materiales in range(len(materiales_agregar)):
            for Bodegas in range(len(datos_inventario)):
                if datos_inventario[Bodegas][3] == materiales_agregar[materiales][2]:
                    print("true")
    return

def crear_informe(datos_inventario):
    for lista in range(len(datos_inventario)):
        print(datos_inventario[lista][1])
    return


#Funcion Para elegir las opciones
def elegir_opcion(numero, datos):
    if numero == 1:
        cargar_inventario(datos)
        return
    elif numero == 2:
        cargar_movimientos(datos)
        return numero
    elif numero == 3:
        crear_informe(datos)
        return numero
    elif numero == 4:
        print("¡Hasta Luego!")
        return numero

#Inicio de la ejecución
respuesta = 0
while respuesta != 4:
    print("  ")
    print("--------Practica 1 Lenguajes Formales y de programación-------")
    print("Sistema de Inventario:")
    print("Para Acceder a cada una, ingrese el numero correspondiente.")
    print("1. Cargar Inventario Inicial")
    print("2. Cargar instrucciones de movimientos")
    print("3. Crear informe de inventario")
    print("4. Salir")
    respuesta = int(input("Ingresa a una opción: "))
    elegir_opcion(respuesta, materiales)
