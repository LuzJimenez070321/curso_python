# lista=["abel","antony","miguel"]
# diccionario={"nombre":"antonio","edad":15,"sexo":False}
# print(diccionario["nombre"])

# texto="hola"
# lista_texto=list(texto)
# lista2=[e for e in texto]

# texto_largo="hola como estan bienvenidos al salon"
# nueva_lista=texto_largo.split(" ")
# print(nueva_lista)


# #crear un programa que reciba una lista desordenada y muestre por terminanal la lista ordenada y la lista previa a ser ordenada.
# lista=[4,76,1,3,6,8,2]
# lista.sort()
# print(lista)







# yo como secretario academico
# debo asignar  los aulas de los estudiantes
# para que puedan registrar su asistencia
# 


# crear una lista de numeros enteros del siguiente texto 
# texto="1,4,8,9,6"
# nueva_lista=[]
# for n in texto.split(","):
#     nueva_lista.append(int(n))
# print(nueva_lista)    
# # aplicando la tecnica vlc valor bucle y condidcion 

# texto="1,4,8,9,6"
# nueva_lista=[int(n) for n in texto.split(",") if n%2==0]
# print(nueva_lista)

# diccionarios por comprension
lista_amigos=["abel","anthony","edith","ruth"]
diccionario={}
for _,v in enumerate(lista_amigos):
    diccionario[v]=len(v)
print(diccionario)    

# aplicando el vlc
lista_amigos=["abel","anthony","edith","ruth"]
diccionario={amigo:len(amigos)for amigo in lista_amigos}
print(diccionario)