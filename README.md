# **Lenguajes Formales y de Programación**
## *Primera Practica*
### **Segundo Semestre 2023**

```js
Universidad San Carlos De Guatemala
Programador: Harold Benjamin Oxlaj Mangandi
Carne: 202100543
Lenguaje: Python
Bibliotecas usadas: os
```
---
## Descripción del Proyecto
El siguiente Proyecto consiste en carga masiva en el lenguaje de programación 
python el cual simula un gestor sencillo de inventarios en el cual se podrá cargar un archivo *.inv* con el inventario inicial, y archivos *.mov* con los movimientos, ya sean ventas o agregar productos, por ultimo es posible agregar los datos del inventario a un archivo txt con el nombre *Inventario Final.txt* en forma tabular para mejor visualizacion.
## Partes del Proyecto
El arreglo en el que se trabaja el inventario inicial, y sus movimientos es: *inventario_final* y esta declaro al inicio del codigo.
## **Menu Principal**
El menu principal muestra las 4 distintas opciones que el usuario puede elegir en consola, **Cargar Inventario inicial**, **Cargar Movimientos en el inventario**, **Crear informe del inventario** y **salir**. dicho menu está encerrado en un bucle *while*, en el que saldrá cuando la respuesta del usuario que se guarda en la variable *respuesta_usuario* sea igual a 4; la validacion de la respuesta del usuario se ejecuta por medio de la funcion ***elegir_opcion***.
## **Funciones**
### *elegir_opcion*
esta funcion recibe como parametro un arreglo y la respuesta del usuario; esta funcion llama a las demas funciones dependiendo del numero ingresado por el usuario y retornando la respuesta del usuario.
Las funciones ***cargar_inventario*** y ***cargar_movimientos*** se ingresa como parametro el nombre de los archivos ingresados por el usuario por medio de la variable *nombre*.
### *convertir_numericos*
esta funcion recibe como parametro un arreglo, se valida si el arreglo mandado en la funcion es un arreglo con los movimientos o la carga del inventario; convierte en **int** y **float** los **str** de las cantidades y precios respectivamente por medio de un ciclo *for* el cual tiene como rango la longitud del arreglo; corrige los nombres de las bodegas que tienen "\n" al final de su nombre y guarda los datos en variables auxiliares antes de mandarlo al arreglo original.
### *cargar_inventario*
esta funcion recibe como parametro un arreglo y el nombre del archivo para leer los datos por medio del modo de acceso *"r"* se valida por medio de la biblioteca de Python *os* si el archivo existe en el directorio y si está con la extension *.inv*.
Se lee linea por linea, por medio de un ciclo *for* y separando los datos de las lineas que contengan";" por medio de la funcion *split()* y guardando los datos en variables auxiliares antes de agregarlo al arreglo, luego de que sean agregados se llama la funcion ***convertir_numericos***.
### *cargar_movimientos*
esta funcion recibe como parametro un arreglo y el nombre del archivo para leer los datos por medio del modo de acceso *"r"*, se lee linea por linea, por medio de un ciclo *for* y separando los datos de las lineas que contengan";" por medio de la funcion *split()* y guardando los datos en variables auxiliares, luego se llama la funcion ***convertir_numericos***.
Por medio de dos ciclos *for* uno con rango la longitud del arreglo de movimiento y otro con rango de la longitud del inventario ya cargado; se valida si se agregan producto o es una venta *"agregar_stock"* y *"vender_producto"* respectivamente; se recorren los arreglos validando primero, si la bodega existe, luego, si existe el producto en esa bodega,si existe, se realiza la operacion correspondiente en caso de que no exista se imprime un mensaje de error, al igual si el producto existente es menor que la venta.
Se ejecuta un **Break** al final de cada validacion.
### *crear_informe*
esta funcion recibe como parametro un arreglo, se crea un archivo txt en la carpeta principal, por el modo de acceso "w+", se escribe en este archivo por medio de un ciclo *for* teniendo como rango la longitud del arreglo; Se recorre todo el arreglo justificando cada dato para que se vea en forma tabular y concatenandolos, limitando el valor total de los productos a 4 decimales.
