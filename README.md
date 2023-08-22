# **Lenguajes Formales y de Programacion**
## *Primera Practica*
### **Segundo Semestre 2023**

```js
Universidad San Carlos De Guatemala
Programador: Harold Benjamin Oxlaj Mangandi
Carne: 202100543
```
---
## Descripción del Proyecto
El siguiente Proyecto consiste en carga masiva en el lenguaje de programacion 
python el cual simula un gestor sencillo de inventarios.
## Partes del Proyecto
**Menu Principal**
El menu principal muestra las 4 distintas opciones que el usuario puede elegir en consola, *Cargar Inventario inicial*, *Cargar Movimientos en el inventario*, *Crear informe del inventario* y *salir*. dicho menu está encerrado en un bucle *while*, en el que saldrá cuando la respuesta del usuario que se guarda en la variable *respuesta_usuario* sea igual a 4; la validacion de la respuesta del usuario se ejecuta por medio de la funcion ***elegir_opcion***
## **Funciones**
### *elegir_opcion*
esta funcion recibe como parametro un arreglo y la respuesta del usuario; esta funcion llama a las demas funciones dependiendo del numero ingresado por el usuario y retornando la respuesta del usuario.
Las funciones ***cargar_inventario*** y ***cargar_movimientos** se ingresa como parametro el nombre de los archivos ingresados por el usuario por medio de la variable *nombre*
### *convertir_numericos*
esta funcion recibe como parametro un arreglo, el cual convierte en *int* los *str* de los precios y cantidades del inventario validando si el arreglo mandado en la funcion es un arreglo con los movimientos o la carga del inventario, arreglando tambien errores en nombres de las bodegas, guardando los datos en variables auxiliares.
### *cargar_inventario*
### *cargar_movimientos*
### *crear_informe*
