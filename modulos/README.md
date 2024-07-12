# averiguar sobre  modulos y paquetes en python 

Los módulos y los paquetes en Python son librerías adicionales al código base de Python que contienen funciones. Los módulos hacen referencia a archivos de Python que pueden contener una o varias funciones. El uso de módulos nos permite mantener el orden. Por otra parte, los paquetes son carpetas que contienen módulos y a su vez nos permiten mantener en orden proyectos que pueden ser demasiado grandes. En Python los paquetes deben contener un archivo de inicialización conocido como init. A lo que conocemos como librerías de Python son paquetes que han sido desarrollados por la comunidad para diferentes aplicaciones. Por ejemplo, paquetes como pandas que han sido desarrollados para la manipulación de datos.

# deferencia entre modulos y paquetes 

Los módulos hacen referencia a archivos de Python que pueden contener una o varias funciones. El uso de módulos nos permite mantener el orden. Por otra parte, los paquetes son carpetas que contienen módulos y a su vez nos permiten mantener en orden proyectos que pueden ser demasiado grandes
## ejemplos de MODULOS
Un módulo es un archivo de Python cuyos objetos (funciones, clases, excepciones, etc.) pueden ser accedidos desde otro archivo. Se trata simplemente de una forma de organizar grandes códigos.

```python
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b
```
## ejemplos de Paquetes 

Un paquete es una carpeta que contiene varios módulos. Siguiendo el ejemplo anterior, podemos diseñar un paquete matematica creando una carpeta con la siguiente estructura.

matematica/
    |-- __init__.py
    |-- aritmetica.py
    |-- geometria.py

# Debe contener siempre un archivo __init__.py (por el momento vacío) para que Python entienda que se trata de un paquete y no de una simple carpeta. Así, podemos acceder a alguno de los módulos del paquete de la siguiente manera.

import matematica.aritmetica

print(matematica.aritmetica.sumar(7, 5))

 # O bien de la siguiente.

from matematica import aritmetica

print(aritmetica.sumar(7, 5))

# También, esta otra:

from matematica.aritmetica import sumar

print(sumar(7, 5))