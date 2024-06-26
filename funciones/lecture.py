# return devuelve los valores que podre hacer uso
# crear una funcion que retorne el numero 10, y muestre por terminal si es par 
# siempre que el valor que retorne mi funcion se utiliza en mas sentencias un operadores hacer return
# def diez():
#     return 10
# if diez()%2==0:
#     print("es par")
# else:
#     print("es impar") 

# print solo muestra por terminal

# return cuando queremos que muestre funcion devuelve o retorne un tipo de dato estructurado 

# # crear una funcion qu me muestre el producto de dos numeros 
# def producto(a,b):
#     return a*b
# print(producto(4,8))

# # crear una funcionn que me retorne una lista de 3 numeros 
# def lista_numeros():
#     return [3,2,6]

# # print usaremos cada vez que nuestra funcion retorne un mensaje 

# # crear una funcion que por parametro reciba un nombre y retorne un mensaje de bbienvenidadf con el nombre 

# def mensaje(nombre):
#     print("hola, {nombre}, bienvenido al chongo")
# mensaje("jose")


# # crear una funcion que reciba por parametro una lista de numeros y me devuelva el numero menor, mostrar  por terminal el valor retornado por la funcion 
# def encontrar_minimo(lista_numeros):
#     if len(lista_numeros) == 0:
#         return "La lista está vacía"

#     minimo = min(lista_numeros)
#     return minimo

# # Ejemplo de uso de la función
# numeros = [5, 3, 8, 1, 10]
# minimo_numero = encontrar_minimo(numeros)
# print("El número más pequeño de la lista es:", minimo_numero)

# # Crear una funcion que reciba como parametro de la edad de una persona mi funcion debera retornar un diccionario con los datos, luego mostrar por terminal el valor de retorno de mi funcion
# def crear_diccionario_persona(nombre, edad):
#     persona = {
#         "nombre": nombre,
#         "edad": edad
#     }
#     return persona

# # Ejemplo de uso de la función
# nombre = "Juan"
# edad = 30
# datos_persona = crear_diccionario_persona(nombre, edad)
# print("Diccionario de datos de la persona:", datos_persona)

# def suma(*args):
#     nueva_lista=
#     args[0]=10
#     print(args)
# suma(4,7,8,5,4)    

# empaquetado y desempequetado de argumentos nominales 
# def alumnos(**kwargs):
#     kwargs["nombre"]="abel"
#     print(kwargs)
# alumnos(nombre="miguel",apellido="largo",edad=30)

# # Ejemplos de lambda
# saludo=lambda n, a:f"hola, {n} , {a}"
# print(saludo("ruth","castillo"))

# # crear un programa que amonimo que reciba como parametro una lista de 5 numeros y retorne dos lista una con los numeros y otra con numeros impares 
# lista_numeros=[1,2,3,4,5,6,7,8,9,10]
# pares=lambda l:[n for n in lista if n%2==0]
# impares=lambda l:n [n for n in lista if n%2¡=0]
# print(pares(lista_numeros))
# print(impares(lista_numeros))

# list(filter())

# # map 
# lista=[4,7,8,5,2]
# nueva_lista=list(map(lambda x:x+1,lista)) # por defecto retorna una nueva lista
# print(nueva_lista)

# tengo una lista de alumnos que todos ellos aprobaron y pasan al tercer semestre 
# en mi lista estan todos con el segundo semestre por lo que tenemos que crear una solucion que cambie el campo de semetre de 2 a 3
# lista_alumnos=[
#     {
#         "nombre":"abel",
#         "edad":36,
#         "semestre":2
#     },{
#         "nombre":"anthony",
#         "edad":40,
#         "semestre":2
#     },{
#         "nombre":"edith",
#         "edad":50,
#         "semestre":2
#     }
# ]
# def objeto(e):
#     if "semestre" in e:
#         e["semestre"]=e["semestre"]+1
#     return[
#         e
#     ]    
# nueva_lista=list(map(objeto,lista_alumnos))
# print(nueva_lista)


# lista_alumnos=[
#    {
#          "nombre":"abel",
#          "edad":36,
#          "semestre":2
#      },{
#          "nombre":"anthony",
#          "edad":40,
#          "semestre":2
#      },{
#          "nombre":"edith",
#          "edad":50,
#          "semestre":2
#      }
#  ]
# def objeto(e):
#     e["programa_estudio"]="ASPTI"
#     return[
#         e
#     ]
# nueva_lista=list(map(objeto,lista_alumnos))
# print(nueva_lista)

# # filter
# devolver los numeros pares de una lista
# lista=[4,8,2,5,7,10,6,5,3,20]
# nueva_lista=list(filter(lambda x:x%2==0,lista))
# print(nueva_lista)

lista_alumnos=[
    {
          "nombre":"abel",
          "edad":36,
          "semestre":2
      },{
          "nombre":"anthony",
          "edad":40,
          "semestre":2
      },{
          "nombre":"edith",
          "edad":50,
          "semestre":2
      }
]
  
nueva_lista=list(filter(lambda x:x["edad"]<50,lista_alumnos))
print(nueva_lista)