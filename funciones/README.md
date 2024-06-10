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
