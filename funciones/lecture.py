# return devuelve los valores que podre hacer uso
# crear una funcion que retorne el numero 10, y muestre por terminal si es par 
# siempre que el valor que retorne mi funcion se utiliza en mas sentencias un operadores hacer return
def diez():
    return 10
if diez()%2==0:
    print("es par")
else:
    print("es impar") 

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
def alumnos(**kwargs):
    kwargs["nombre"]="abel"
    print(kwargs)
alumnos(nombre="miguel",apellido="largo",edad=30)