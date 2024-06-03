### Crear una lista de 5 alumnos almacenaremos su noombre apellido y edad 
# lista_alumnos=[
#     {
#         "nombre":"abel"
#         "edad":20
#     },{
#         "nombre":"ruth"
#         "edad":13
#     },{
#         "nombre":"antoni"
#         "edad":80
#     },{
#         "nombre":"luz"
#         "edad":15
#     },{
#         "nombre":"edith"
#         "edad":16
#     }]

# #insertar ala lista al final de la lista los datos antoni 
# lista_nombres=["edith","ruth","luz","abel"]
# lista_nombres.append("antony")
# print(lista_nombres)


#eliminar de la lista si existe los datos de abel
# lista_nombres=["edith","ruth","luz","abel"]
# lista_nombres.remove("abel")
# print(lista_nombres)


# buscar y mostrar el alumno el posocion 4 de la lista

# lista_nombres=["edith","ruth","luz"]
# indice=lista_nombres.index("ruth")
# print(lista_nombres[indice])


## 2. crear una lista de con 4 disccionarios donde tendran los datos de sus mascotas (nombre,edad,sexo,raza)

# tareas
# mostrar la lista con los 4 diccionarios 
# editar el tercer regritro y cambiarle la edad sin modificar la lista original
# mostrar la lista original y luego la lista del tercer registro modificado



# un empresario de alquiler de motos desea guardar una base de datos de la informacionde sus vehiculos, proceso que desea automatizar un sistema informatico, las acciones que puede realizar el emprezario son ver las listas de autos que tiene, podra tambien actualizar la lista y agregar un nuevo vehiculo

######
# casos de uso
 
# yo como empresario 
# quiero ver la lista de vehiculos,actualizar y agregar algun dato
# para ver los vehiculos en mi base de datos 

# programacion 

# Base de datos de vehículos
vehiculos = [
    {"modelo": "Honda", "marca": "CBR500R", "año": 2021, "estado": "Disponible", "precio_alquiler": 50},
    {"modelo": "Yamaha", "marca": "YZF-R3", "año": 2020, "estado": "Alquilado", "precio_alquiler": 40},
    {"modelo": "Suzuki", "marca": "GSX250R", "año": 2019, "estado": "Disponible", "precio_alquiler": 45}
]

# Función para ver la lista de vehículos
def ver_lista_vehiculos():
    print("Lista de Vehículos:")
    for idx, vehiculo in enumerate(vehiculos):
        print(f"ID: {idx}, Modelo: {vehiculo['marca']} {vehiculo['modelo']}, Estado: {vehiculo['estado']}, Precio de alquiler: ${vehiculo['precio_alquiler']} por día")
    print("\n")

# Función para agregar un nuevo vehículo
def agregar_vehiculo():
    modelo = input("Ingrese el modelo del vehículo: ")
    marca = input("Ingrese la marca del vehículo: ")
    año = input("Ingrese el año del vehículo: ")
    estado = input("Ingrese el estado del vehículo (Disponible/Alquilado): ")
    precio_alquiler = input("Ingrese el precio de alquiler por día del vehículo: ")

    vehiculo_nuevo = {"modelo": modelo, "marca": marca, "año": año, "estado": estado, "precio_alquiler": precio_alquiler}
    vehiculos.append(vehiculo_nuevo)
    print("Nuevo vehículo agregado correctamente.\n")

# Función para actualizar la lista de vehículos
def actualizar_lista():
    ver_lista_vehiculos()
    indice = int(input("Ingrese el ID del vehículo que desea actualizar: "))
    if indice >= 0 and indice < len(vehiculos):
        vehiculo = vehiculos[indice]
        nuevo_estado = input("Ingrese el nuevo estado del vehículo (Disponible/Alquilado): ")
        vehiculo['estado'] = nuevo_estado
        print("Estado del vehículo actualizado correctamente.\n")
    else:
        print("ID de vehículo no válido.\n")

# Ejecutar las funciones
ver_lista_vehiculos()
agregar_vehiculo()
ver_lista_vehiculos()
actualizar_lista()
ver_lista_vehiculos() 







