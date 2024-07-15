""" este es el script principal""" 
def f_es_mayor(lista):
    """funcion para saber el numero mayor de una lista"""
    mayor=lista[0]
    for n in lista:
        if n > mayor:
            mayor=n
    return mayor