#Funcion Cargar Inventario
def cargar_inventario():
    inventario = open("Prueba.INV", 'r')
    datos = inventario.read()
    inventario.close()
    print (datos)
    return

def cargar_movimientos():
    print("segundo")
    return

def crear_informe():
    print("Tercero")
    return


#Funcion Para elegir las opciones
def elegir_opcion(numero):
    if numero == 1:
        cargar_inventario()
        return
    elif numero == 2:
        cargar_movimientos()
        return numero
    elif numero == 3:
        crear_informe()
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
    elegir_opcion(respuesta)
