#Funcion Cargar Inventario
materiales = []
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

def cargar_inventario(datos_inventario,nombre_archivo):
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
        aux_datos_finales.insert(0,instruccion)
        materiales_agregar.append(aux_datos_finales)
    convertir_numericos(materiales_agregar)
    print(materiales_agregar)
    for materiales in range(len(materiales_agregar)):
            for Bodegas in range(len(datos_inventario)):
                if materiales_agregar[materiales][0] == "agregar_stock":
                    if datos_inventario[Bodegas][3] == materiales_agregar[materiales][3]:
                        if datos_inventario[Bodegas][0] == materiales_agregar[materiales][1]:
                            nueva_cantidad = datos_inventario[Bodegas][1]+materiales_agregar[materiales][2]
                            datos_inventario[Bodegas][1] = nueva_cantidad
                        else:
                            print("Lo sentimos, pero el producto: "+ materiales_agregar[materiales][1]+ 
                                  "No existe en: "+ datos_inventario[Bodegas][3]) 
                else:
                    if datos_inventario[Bodegas][3] == materiales_agregar[materiales][3]:
                        if datos_inventario[Bodegas][0] == materiales_agregar[materiales][1]:
                            nueva_cantidad = datos_inventario[Bodegas][1]- materiales_agregar[materiales][2]
                            if nueva_cantidad<0:
                                print("La venta sobrepasa los productos existentes")
                            else:
                                datos_inventario[Bodegas][1] = nueva_cantidad
                        else:
                            print("Lo sentimos, pero el producto: "+ materiales_agregar[materiales][1]+ 
                                  " No existe en: "+ datos_inventario[Bodegas][3]) 

    print("Inventario actualizado con exito")
    return

def crear_informe(datos_inventario):
    archivo_inventario = open("Inventario Final.txt", "w+")
    archivo_inventario.write("-"*80+"\n")
    archivo_inventario.write("Informe de Productos del inventario: \n")
    archivo_inventario.write("Producto  ----  Cantidad  ----  Precio Unitario  "
           "----  Valor Total  ----  Ubicacion\n")
    archivo_inventario.write("*"*80+"\n")
    for bodegas in range(len(datos_inventario)):
        archivo_inventario.write(datos_inventario[bodegas][0].ljust(10) + "----".ljust(8)+
              str(datos_inventario[bodegas][1]).ljust(8)+ "----".ljust(11)+
              str(datos_inventario[bodegas][2]).ljust(12)+ "----".ljust(9)+
              str(datos_inventario[bodegas][1]*datos_inventario[bodegas][2]).ljust(10) + 
              "----".ljust(7)+
              str(datos_inventario[bodegas][3])+ "\n")
    return


#Funcion Para elegir las opciones
def elegir_opcion(numero, datos):
    if numero == 1:
        nombre = input("Ingrese el Nombre del archivo con su extensión: ")
        cargar_inventario(datos, nombre)
        return
    elif numero == 2:
        nombre = input("Ingrese el Nombre del archivo con su extensión: ")
        cargar_movimientos(datos, nombre)
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
