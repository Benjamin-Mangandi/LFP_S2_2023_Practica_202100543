inventario_final = []

# Funcion Cargar Inventario

def convertir_numericos(datos_inventario):
    if datos_inventario[0][0] != "agregar_stock" and datos_inventario[0][0] != "vender_producto":
        for bodega in range(len(datos_inventario)):
            nombre_error = datos_inventario[bodega][3]
            nombre_sin_error = nombre_error.replace("\n", "")
            datos_inventario[bodega][3] = nombre_sin_error
        for bodega in range(len(datos_inventario)):
            cantidad = datos_inventario[bodega][1]
            cantidad_numerica = int(cantidad)
            datos_inventario[bodega][1] = cantidad_numerica
        for bodega in range(len(datos_inventario)):
            precio = datos_inventario[bodega][2]
            precio_numerico = float(precio)
            datos_inventario[bodega][2] = precio_numerico
    else:
        for bodega in range(len(datos_inventario)):
            nombre_error = datos_inventario[bodega][3]
            nombre_sin_error = nombre_error.replace("\n", "")
            datos_inventario[bodega][3] = nombre_sin_error
        for bodega in range(len(datos_inventario)):
            cantidad = datos_inventario[bodega][2]
            cantidad_numerica = int(cantidad)
            datos_inventario[bodega][2] = cantidad_numerica


def cargar_inventario(datos_inventario, nombre_archivo):
    inventario = open(nombre_archivo, 'r')
    for linea in inventario:
        aux_separar_lineas = linea.split(" ")
        aux_separar_datos = aux_separar_lineas[1]
        aux_datos_finales = aux_separar_datos.split(";")
        datos_inventario.append(aux_datos_finales)
    convertir_numericos(datos_inventario)
    print("¡Datos cargados con exito!")
    print(datos_inventario)
    return


def cargar_movimientos(datos_inventario, nombre_archivo):
    inventario = open(nombre_archivo, 'r')
    materiales_agregar = []
    for linea in inventario:
        aux_separar_lineas = linea.split(" ")
        instruccion = aux_separar_lineas[0]
        aux_separar_datos = aux_separar_lineas[1]
        aux_datos_finales = aux_separar_datos.split(";")
        aux_datos_finales.insert(0, instruccion)
        materiales_agregar.append(aux_datos_finales)
    convertir_numericos(materiales_agregar)
    print(materiales_agregar)
    for materiales in range(len(materiales_agregar)):
        for Bodegas in range(len(datos_inventario)):
            if materiales_agregar[materiales][0] == "agregar_stock":
                if datos_inventario[Bodegas][3] == materiales_agregar[materiales][3]:
                    if datos_inventario[Bodegas][0] == materiales_agregar[materiales][1]:
                        nueva_cantidad = datos_inventario[Bodegas][1] + \
                            materiales_agregar[materiales][2]
                        datos_inventario[Bodegas][1] = nueva_cantidad
                    else:
                        print("Lo sentimos, pero el producto: " + materiales_agregar[materiales][1] +
                              "No existe en: " + datos_inventario[Bodegas][3])
            else:
                if datos_inventario[Bodegas][3] == materiales_agregar[materiales][3]:
                    if datos_inventario[Bodegas][0] == materiales_agregar[materiales][1]:
                        nueva_cantidad = datos_inventario[Bodegas][1] - \
                            materiales_agregar[materiales][2]
                        if nueva_cantidad < 0:
                            print("La venta sobrepasa los productos existentes")
                        else:
                            datos_inventario[Bodegas][1] = nueva_cantidad
                    else:
                        print("Lo sentimos, pero el producto: " + materiales_agregar[materiales][1] +
                              " No existe en: " + datos_inventario[Bodegas][3])

    print("Inventario actualizado con exito")
    return

# Funcion para hacer el archivo txt

def crear_informe(datos_inventario):
    archivo_inventario = open("Inventario Final.txt", "w+")
    archivo_inventario.write("-"*110+"\n")
    archivo_inventario.write("Informe de Productos del inventario: \n")
    archivo_inventario.write("\nProducto    ------    Cantidad    ------    Precio Unitario    "
                             "------    Valor Total    ------    Ubicacion\n")
    archivo_inventario.write("*"*110+"\n")
    for bodegas in range(len(datos_inventario)):
        valor_total = datos_inventario[bodegas][1] * datos_inventario[bodegas][2]
        valor_total_cuatro_decimales = "{:.4f}".format(valor_total)
        archivo_inventario.write(datos_inventario[bodegas][0].ljust(12) + "------".ljust(13) +
                                 str(datos_inventario[bodegas][1]).ljust(9) + "------".ljust(15) +
                                 "Q"+ str(datos_inventario[bodegas][2]).ljust(13) + "------".ljust(12) +
                                 "Q"+ str(valor_total_cuatro_decimales).ljust(12) +
                                 "------".ljust(11) +
                                 str(datos_inventario[bodegas][3]) + "\n")
    print("\n¡Informe Creado con exito!")
    return


# Funcion para elegir las opciones

def elegir_opcion(respuesta_usuario, inventario):
    if respuesta_usuario == 1:
        nombre = input("Ingrese el Nombre del archivo con su extensión: ")
        cargar_inventario(inventario, nombre)
        return respuesta_usuario
    elif respuesta_usuario == 2:
        nombre = input("Ingrese el Nombre del archivo con su extensión: ")
        cargar_movimientos(inventario, nombre)
        return respuesta_usuario
    elif respuesta_usuario == 3:
        crear_informe(inventario)
        return respuesta_usuario
    elif respuesta_usuario == 4:
        print("\n¡Hasta Luego!")
        return respuesta_usuario


# Inicio de la ejecución

respuesta_usuario = 0
while respuesta_usuario != 4:
    print("\n--------Practica 1 Lenguajes formales y de programación-------")
    print("Sistema de Inventario:")
    print("Para Acceder a cada opcion, ingrese el numero correspondiente.")
    print("1. Cargar Inventario Inicial")
    print("2. Cargar instrucciones de movimientos")
    print("3. Crear informe de inventario")
    print("4. Salir")
    respuesta_usuario = int(input("Ingresa a una opción: "))
    elegir_opcion(respuesta_usuario, inventario_final)