# #Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no 
# # Solicitar la edad al usuario

# edad = int(input("Ingresa tu edad: "))

# # Verificar si es mayor de edad o no
# if edad >= 18:
#     print("Eres mayor de edad")
# else:
#     print("No eres mayor de edad")
   


# #Escribir un programa que almacene la cedena de caracteres de contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincida con la guardada en la variable sin tener en cuenta mayusculas y minusculas.

# # Almacenar la contraseña en una variable
# contraseña = "Contraseña123"

# # Solicitar la contraseña al usuario
# contraseña_usuario = input("Ingresa la contraseña: ")

# # Comparar las contraseñas sin tener en cuenta mayúsculas y minúsculas
# if contraseña.lower() == contraseña_usuario.lower():
#     print("La contraseña es correcta")
# else:
#     print("La contraseña es incorrecta")


# #Escribir un programa que pida al usuario un numero entero positivo y muestre por pantalla la cuenta atras desde ese numero hasta cero separados por comas.

# # Solicitar al usuario un número entero positivo
# numero = int(input("Ingresa un número entero positivo: "))

# # Verificar si el número es positivo
# if numero > 0:
#     # Inicializar la cadena de caracteres para la cuenta atrás
#     cuenta_atras = str(numero)

#     # Realizar la cuenta atrás desde el número ingresado hasta cero
#     for i in range(numero - 1, -1, -1):
#         cuenta_atras += ", " + str(i)

#     # Mostrar la cuenta atrás por pantalla
#     print(cuenta_atras)
# else:
#     print("El número ingresado no es válido")


# crear un programa que me cuente la cantidad de comas y me muestre 
# sus indices 
#OJO: tiene que pedir al usuario 
# oracion:str=input("ingresa una oracion")
# contador:int=0

# for indice,letra in enumerate(oracion):
#    if letra ==",":
#     print(f"su indice es(indice)")
#     contador+=1
#    print(f"la cantidad de comas es (contador)")


# # escribir un programa que pregunte al usuario su edad y muestre por pantalla los años que ah cumplido
# # pedir al usuario su edad 
# edad = int(input("¿cuantos años tines? "))
# #generar una listacon los años que ah cumplido
# anios_cumplidos =[str(anio)]
# for anio in range(1, edad+1) 
#   # mostrar los años cumplido
#    print ("has cumplido los años siguientes años": " + ",.join(anios_cumplidos))
        

# #crear un programa que me pida el nombre de tres personas y guarde en una variable global la ultima lñetras de sus nombres.
# #mostrar por pantalla la variable global con las tres letras de nombre de cada persona 
# for n in range(3):
#    nombre:str=input("escribe tu nombre. ")
#    #ultima_letra+=nombre[-1]
#    last_letter:str=nombre[-1]
#    ultima_letra+=last_letter
#    #ultima_letra=ultima_letra+lastletter
# print(ultima_letra)

#crear un progrma a que muestre por teminar la siguiente figura 
#a
#ee
#iii
#oooo
#uuuuu

vocales = ['a', 'e', 'i', 'o','u']
for i in range(len(vocales)):
   liena = vocales[i] * (i+1)
   print(liena)

        