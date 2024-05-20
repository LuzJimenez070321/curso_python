# # primer ejemplo if estructurado 
# edad:int(input("escribe tu edad: "))
# if:edad>=18:
#     print("eres menor")
# else:
#     print("eres nemor de edad")
--
# #segundo ejemplo if almacendado en variable 

# edad_dos:int=int(input("escribe tu edad: "))
# respuesta:str="eres mator" if edad_dos>=18 else "eres menor"
# print(respuesta)       


# def contar_comas(cadena):
#     indices=
#     contador=0
#     for i in 
# range(len(cadena)):
#      if cadena[i]==[',']
#         contador +=1
#         indices.appendi(i)
#     return contador , indices
# # pedir al usuario una cadena de texto 
# texto = input("ingresa una cadena de texto: ")
# #obten la cantidad de comas y sus indices
# cantidad , indices =
# contar_comas(texto)
# #mostrar los resultados 
#     print("la cantidad de comas es:", cantidad)
#     print("los indices de las comas son :", indices)



# condicion=True
# while condicion:
#     input=("desea continuar [S/N]:")
#     if eval=="S":
#         print("continuas en el bucle")
#         continue
#     else:
#         print("se termino el programa")
#         break

# contador=0
# while contador<=5:
#     print(contador)
#     contador+=1
# print(f"el valor final {contador}")
    
# nombre="jose"
# nombre.upper() #convertir el texto en mayuscula

# apellidos="ALVAREZ"
# print (apellidos.lower()) #convertir el texto en minuscula
 
# segundo_nombre="luis"
# segundo_nombre.capitalize()  #convierte la primera letra en mayuscula



# Programa para calcular el promedio de un conjunto de notas ingresadas por el usuario

# Pedir al usuario la cantidad de notas a registrar
cantidad_notas = int(input("Ingrese la cantidad de notas a registrar: "))

# Inicializar la variable suma para almacenar la suma de las notas
suma_notas = 0
contador = 0

# Utilizar un bucle while para pedir las notas al usuario y calcular la suma
while contador < cantidad_notas:
    suma_notas += float(input("Ingrese la nota: "))
    contador += 1

# Calcular el promedio dividiendo la suma de las notas entre la cantidad de notas
promedio = suma_notas / cantidad_notas

# Imprimir el promedio de las notas
print(f"El promedio de las {cantidad_notas} notas ingresadas es: {promedio}")