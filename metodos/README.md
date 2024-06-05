# Metodos para python
## Numeros
```python
len(154788)
# devueleve la cantidad de digitos
#6
```
## Texto 
```python
len("hola mundo")
#devuelve la cantidad de caracteres 
# el espacion cuenta como un caracter 
#10
```
## Lista 
len (["h","o","l","a"])
# devueleve la cantidad de elementos 
# el espacio cuenta como un caracter 
# 4

## Duplas
```python
# Definir dos listas con elementos
nombres = ["Ana", "Juan", "María"]
edades = [25, 30, 28]

# Utilizar la función zip para emparejar los elementos en duplas
duplas = zip(nombres, edades)

# Mostrar las duplas resultantes
for dupla in duplas:
    print(dupla)
```
## Diccionarios
```python
lista_amigos=["abel","anthony","edith","ruth"]
diccionario={}
for _,v in enumerate(lista_amigos):
    diccionario[v]=len(v)
print(diccionario) 
```