## crear una funcion que reciba por argumento  n numeros y retorne una lista con los numeros pares
# def numeros_pares(*args):
#     numeros_pares = [num for num in args if num % 2 == 0]
#     return numeros_pares

# # Ejemplo de uso
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# pares = numeros_pares(*numeros)
# print(pares)

## crar tres funciones para los siguientes casos 
## calcular el numero menor
def numero_menor(*args):
    return min(args) 
## calcular el munero mayor 
def numero_mayor(*args):
    return max(args)
## calcular la suma de todos los numeros 
def suma_numeros(*args):
    return sum(args)
# se le pasara por argumento n numeros
numeros = [10, 5, 7, 3, 8, 12]
print("Número menor:", numero_menor(*numeros))
print("Número mayor:", numero_mayor(*numeros))
print("Suma de todos los números:", suma_numeros(*numeros))