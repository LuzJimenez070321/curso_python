""" este es el script principal""" 
def f_es_menor(lista):
    """funcion para saber el numero menor de un lista"""
    menor=lista[0]
    for n in lista:
        if n < menor:
            menor=n
    return menor  