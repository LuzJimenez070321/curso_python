# primer ejemplo if estructurado 
edad:int(input("escribe tu edad: "))
if:edad>=18:
    print("eres menor")
else:
    print("eres nemor de edad")

#segundo ejemplo if almacendado en variable 

edad_dos:int=int(input("escribe tu edad: "))
respuesta:str="eres mator" if edad_dos>=18 else "eres menor"
print(respuesta)       


def contar_comas(cadena):
    indices=
    contador=0
    for i in 
range(len(cadena)):
     if cadena[i]==[',']
        contador +=1
        indices.appendi(i)
    return contador , indices
# pedir al usuario una cadena de texto 
texto = input("ingresa una cadena de texto: ")
#obten la cantidad de comas y sus indices
cantidad , indices =
contar_comas(texto)
#mostrar los resultados 
    print("la cantidad de comas es:", cantidad)
    print("los indices de las comas son :", indices)