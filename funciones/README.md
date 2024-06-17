# FUNCIONES
## Concepto
matematicamnete una funcion es una operacion que toma una o mas valores llamados `argumento` y prodcuce un valor denominado `resultado`
>[¡NOTA]
>Todos los lenguajes tienen programacion tiene funciones incorporadas por el, usuario (`funciones internas`), y funciones creadas por el usuario 
(`funciones externas`)

en programacion una funcion es un subprograma, es una estructura que nos permite agrupar codigo y sus principales obejetivos son:
-`NO REPETIR` fragmentos de codigos
-`REUTILIZAR` el codigo en distintos escenarios

## Estructura de una funcion
Una funcion viene `definida` por un `nombre` sus `parametros` y sus valor de `retorno` una vez creada la funcion podemos solicitar su ejecucion inbocando la funcion por su `nombre` 

## Definir una funcion en python
Para defenir una funcion en python primero utilizaremos la prlabra reservada `def` seguida por el `nombre` de la funcion. A continuacion especificaremos los `parametros`con `()` si es una funcion con sin parametros, `(a)` si es una funcion con parametros, si tuviera mas de un parametro iran separados por `,`, finalizaremos con `:` ,  en la siguiente linea sin olvidar el identado, comenzara el cuerpo de la funcion (micro programa) que puede contener 1 o mas centencias, finalmente debera `retornar` un resultadoo con la palabra revervada `return`.
>[!TIP]
> com retorno tambien se puede utilizar la `funcion interna` , `print()`, para la duparacion de codigo no es recomendable usarlo en produccion 
> `print` dentro de una funcion es una herramienta para comparar si una funcion este haciendo un buen trabajo
**EJEMPLO:**
```python
def saludo():
    saludo="hola chivo"
    saludo_dos="como estas"
    return saludo+saludo_dos
```
## Invocar una funcion
Para invocar una funcion o llamar, ejecutar una funcion solo tendremos que scribir el `nombre` de la funcion seguido por `()` parentesis,
```python
def saludo().
print("hola")
#invocando la funcion
saludo()
``` 
## Retornar un valor
Las funciones pueden retornar o devolver un valor.
```python
def uno():
    return
uno()
```
>[!WARNING]
>NO CONFUNDIR `print()`  con   `return` el valor retornado por `return` no s permite usarlo de su contexto, y `print()` solo mostrara el literal por terminal

**Ejmplo:**
*en el archivo `lecture.py`

## Retornando multples valores 
El secreto es hacerlo mediente un tipo de dato estructurado 
```python
def varios():
    return 2,3,4
varios()
# retorna 8(2,3,4)
def lista():
    return ["hola",45]
# retorna["hola",45]
def dicc():
    return{"nombre":"jose","edad",45}  
    dicc()
# retorna {"nombre":"jose","edad",45}  
```
## Parametros y Arguementos
si una funcion n dispociera de valores de ntreda estaria limitada en su actuacion.
es por ello que los `parametros` no permiten variar los datos mque consume una
 funcion para obtener distintos resultados 
 **Ejemplo**
 *crear una funcion que recibe una valor numerico y devuelve su raiz cuadrada*
 ```python
 def sqrt(valor):
    return valor**(1/2)
# NOTA: en este caso , el  valor 4 es un argumento de la funcion 
sqrt(4)
 ```

 cuando llamamos a una funcion con `argumento`, los valores de estos argumentos se copian 
 en los correspondiente `parametros`, dentro de la funcion.
 
 ```python
 def ejem(a,b,c):
    return a+b+c
   ejem(4,5,6) 
 ```
 ### Arguementos Nominales
 En esta aproximacion lops arguemntos no son copiados en un orden si no que **que se asignan por nombre a cada parametro**
 Ellos nos permiten evitar en problema de conocer cual es el orden de los paramtros en la difinicion de la funcion.
 Para utilizarlo , basta con realizar una asignacion de cada argumento de la llamada de la funcion.
 **Ejemplo** 
 ```python
 def build_cpu(familia,num_core,frecuencia):
    print(f"""
    la cpu es de la familia{familia},
    con {num_core} cores y con una 
    frecuencia de {fecuencia}
    """)
# haciendo uso de argumentos dominales
build_cpu(num_core=4,familia="intel",frecuencia=2,7)    
 ```
 
### Argumentos Posicionales
los argumentos son copiados en un orden especifico, en este caso debemos conocer 
o recordar cual es el orden de los parametros
**Ejemplo**
```python
def build_cpu(familia,num_core,frecuencia):
    print(f"""
    la cpu es de la familia{familia},
    con {num_core} cores y con una 
    frecuencia de {fecuencia}
    """)
# haciendo uso de arguemnetos posicionales
build_cpu("inte",4,2,7)
```
## Parametros por defecto 
es posible especificar **valores por defecto** en los parametros de una funcion , en 
el caso de que no proporcione un valor al argumento en la llamada a la funcion, el parametro
correspondiente tomara el valor definido por defecto.
**Ejemplo**
```python
def alumnos(nom,app,estado="aprobado"):

alumnos("ruth","castillo") 
alumno("anthony","cruces","desaprobado")  
```

## Desenpaquetado/Empaquettado de argumentos(Tarea)
Python nos ofrece la posibilidad de empaquetar y desempaquetar argumentos cuando estamos invocando a una función, tanto para argumentos posicionales como para argumentos nominales.

Y de esto se deriva el hecho de que podamos utilizar un número variable de argumentos en una función, algo que puede ser muy interesante según el caso de uso que tengamos.

 # Empaquetar/Desempaquetar argumentos posicionales
Si utilizamos el operador * delante del nombre de un parámetro posicional, estaremos indicando que los argumentos pasados a la función se empaqueten en una tupla.

Veamos un ejemplo en el que vamos a implementar una función para sumar un número variable de valores. La función que tenemos disponible en Python no cubre este caso:
```python
sum(4, 3, 2, 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sum() takes at most 2 arguments (4 given)

# para superar esta «limitación» vamos a hacer uso del * para empaquetar los argumentos posicionales:

def _sum(*values):
    print(f'{values=}')
    result = 0
    for value in values:  # values es una tupla
        result += value
    return result


_sum(4, 3, 2, 1)
values=(4, 3, 2, 1)
10

Existe la posibilidad de usar el asterisco * en la llamada a la función para desempaquetar los argumentos posicionales:

values = (4, 3, 2, 1)

_sum(values)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in _sum
TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'

# Desempaquetado: _sum(4, 3, 2, 1)
_sum(*values)
values=(4, 3, 2, 1)
10
```
### Argumentos sólo posicionales

Para ello, en la definición de los parámetros de la función, tendremos que incluir un parámetro especial / que delimitará el tipo de parámetros. Así, todos los parámetros a la izquierda del delimitador estarán obligados a ser posicionales:
**Ejemplo**
```python
def sum_power(a, b, /, power=False):
    if power:
        a **= 2
        b **= 2
    return a + b


sum_power(3, 4)
7

sum_power(3, 4, True)
25

sum_power(3, 4, power=True)
25

sum_power(a=3, b=4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sum_power() got some positional-only arguments passed as keyword arguments: 'a, b'
```


### Empaquetar/Desempaquetar argumentos nominales
Si utilizamos el operador ** delante del nombre de un parámetro nominal, estaremos indicando que los argumentos pasados a la función se empaqueten en un diccionario.

Supongamos un ejemplo en el que queremos encontrar la persona con mayor calificación de un examen. Haremos uso del ** para empaquetar los argumentos nominales:
```python
def best_student(**marks):
    print(f'{marks=}')
    max_mark = -1
    for student, mark in marks.items():  # marks es un diccionario
        if mark > max_mark:
            max_mark = mark
            best_student = student
    return best_student


best_student(ana=8, antonio=6, inma=9, javier=7)
marks={'ana': 8, 'antonio': 6, 'inma': 9, 'javier': 7}
'inma'
# Al igual que veíamos previamente, existe la posibilidad de usar doble asterisco ** en la llamada a la función para desempaquetar los argumentos nominales:
marks = dict(ana=8, antonio=6, inma=9, javier=7)

best_student(marks)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: best_student() takes 0 positional arguments but 1 was given

# Desempaquetado: best_student(ana=8, antonio=6, inma=9, javier=7)
best_student(**marks)
marks={'ana': 8, 'antonio': 6, 'inma': 9, 'javier': 7}
'inma'
```
### Argumentos sólo nominales

Para ello, en la definición de los parámetros de la función, tendremos que incluir un parámetro especial * que delimitará el tipo de parámetros. Así, todos los parámetros a la derecha del separador estarán obligados a ser nominales:
```python
def sum_power(a, b, *, power=False):
    if power:
        a **= 2
        b **= 2
    return a + b


sum_power(3, 4)
7

sum_power(a=3, b=4)
7

sum_power(3, 4, power=True)
25

sum_power(3, 4, True)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sum_power() takes 2 positional arguments but 3 were given
```

## Funciones Ineternas de python(Tarea)
Cuando hablamos de funciones internas nos referimos a las funciones basicas que estan incorporadas dentro del lenguaje y no necesitan ser importadas desde una libreria, si quieren saber cuales son las disponibles utilizaremos la funcion `dir` y el argumento __builtins__, esto nos devolvera solamente el listado con los nombres 

>`bin()`-> Funcion convierte un numero en una cadena binaria

>`bool()`-> funcion convierte un numero en valor booleano

>`divmod()`->Funcion devuelve un valor tuple con la division y el resto de la division

>`filter()`->Su funcion nos permite construir un objeto interador

>`float()`->Funcion convierte un numero en tipo flotante

>`getattr()`-> Funcion nos devuelve un valor del atributo informado

>`id()`-> Funcion devuelve el bloque de memoria donde esta el objeto

>`len()`-> Funcion devuelve el tamaño del objeto informado

>`list`-> Funcion genera una lista con el iterador o los valores informados

>`print`-> Funcion muestra el objeto pasado en pantalla

>`type()`-> Funcion nos devuelve el tipo de objeto

>`zip()`-> Funcion nos permite crear objetos de tipo clave-valor, en base a los tuples informados.


## Tipos de Funciones
### Funciones Anominas (Funciones lambda)
### Funciones Closure
### Funciones Callback

### Programacion Funcional 