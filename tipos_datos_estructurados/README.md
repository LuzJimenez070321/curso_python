### TIPOS DE DATOS ESTRUCTURADOS (TDA-TIPOS DE DATOS ABSTRACTOS)
```python

#lista-sus vaalores o elementos se pueden actulizar, eliminar
lista["abel",20,5.2,.5,False,["texto,.2"]]

#tupla-sus valores o elementos no pueden ser modificados o eliminados
tupla=("abel",20,5.2,False,[])

#diccionarios u objetos
#los diccionarios almacenan los datos con clave:valor
diccionario={"nombre":"antonio","edad":15,"sexo":False}
```
-[!TIP]
- **Observacion:** que otros tipos de datos estructurados pueden almacenar en su interior otros tipos de datos estructurados 

```python
lista_alumnos=[
    {
        "nombre":"abel"
        "edad":20
    },{
        "nombre":"ruth"
        "edad":13
        "amigos":["flor","rocio"]
    },{
        "nombre":"jose ma"
        "edad":80
    },{}
        
            
]
```

## Metodos
### 1. Convertir texto a lista
```python
# metodo list
texto="hola"
list(texto)#["h","o","l","a"]

#metodo split
texto="hola como estan, alumnitos lindos"
texto.split(",")

# metodo join 
texto_largo="este es un etxto largho chiquitas y chiquitos"
nuevo_texto=texto_largo.split("")
print(" ".join(nuevo_texto))
```
### 2. Agregar elementos a una lista
```python
# Metodo append - es el metodo que me permite agregar elementos al final de una lista
lista=["hola"]
lista.append("mundo")
print(lista)
#["hola","mundo"]

# Metodo insert - es el metodo que me permite agregar elementos en cualquier ubicacion de mi lista 
lista_nombres=["edith","ruth","luz"]
lista_nombres.insert(0,"anthony")
```

### 3. Eliminar elementos de una lista
```python
#metodo pop- es el metodo que elimina el ultimo elemento de una lista es el contrario de de append.
lista_nombres=["edith","ruth","luz"]
lista_nombres.pop()

# Primera opcion - con el metodo remove - este metodo elimina el por el nombre el elemento que conincida dentro de mi lista.
lista_nombres=["edith","ruth","luz"]
lista_nombre.remove("ruth")

#Segunda opcion - metodo pop - al indicarle por parametro un indice este lo eliminara de la lista
lista_nombres=["edith","ruth","luz"]
lista_nombres.pop(0)
```

### 4. Buscar un elemento en una lista
```python
lista_nombres=["edith","ruth","luz"]
indice=lista_nombres.index("ruth")
print(lista_nombres[indice])

pertenencia="edith" in lista_nombres #true False
```