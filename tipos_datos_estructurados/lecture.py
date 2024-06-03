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













# Crear diccionarios para almacenar la información de los estudiantes, aulas y observaciones
estudiantes = {
    "Carlos": {"nota": 85, "asistencia": 0, "observacion": None},
    "Luisa": {"nota": 90, "asistencia": 0, "observacion": None}
}

aulas = {
    "Aula 1": ["Carlos"],
    "Aula 2": ["Luisa"]
}

# Función para que el alumno realice una observación
def realizar_observacion(estudiante, observacion):
    estudiante["observacion"] = observacion

# Simular que el secretario académico asigna aulas
aulas["Aula 1"].append("Luisa")

# Simular que un alumno realiza una observación
realizar_observacion(estudiantes["Carlos"], "Necesito aclaración sobre mi nota")

# Mostrar la información de los estudiantes y aulas
for aula, lista_estudiantes in aulas.items():
    print(f"{aula}: {', '.join(lista_estudiantes)}")

for nombre, info in estudiantes.items():
    print(f"Estudiante: {nombre}, Nota: {info['nota']}, Asistencia: {info['asistencia']} %, Observación: {info['observacion']}")