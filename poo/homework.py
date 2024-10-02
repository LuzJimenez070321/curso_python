# Ejercicio 01
# crear una clase Banco 
# sus atributos seran nombre, apellido, dn, numero de cuenta y saldo inicial 
# como metodos pódremos hacer deposito retirar dinero y ver estado de cuenta 
# class Banco:
def __init__(self, nombre, apellido, dni, numero_cuenta, saldo_inicial):
         self.nombre = nombre
         self.apellido = apellido
         self.dni = dni
         self.numero_cuenta = numero_cuenta
         self.saldo = saldo_inicial
def depositar(self, monto):
        self.saldo += monto
        print(f"Se ha depositado PEN{monto} en su cuenta. Saldo actual: PEN{self.saldo}")

#     def retirar(self, monto):
#         if monto > self.saldo:
#             print("No tiene suficiente saldo para realizar la retirada.")
#         else:
#             self.saldo -= monto
#             print(f"Se ha retirado PEN{monto} de su cuenta. Saldo actual: PEN{self.saldo}")

#     def ver_estado_cuenta(self):
#         print(f"Nombre: {self.nombre} {self.apellido}")
#         print(f"DNI: {self.dni}")
#         print(f"Número de cuenta: {self.numero_cuenta}")
#         print(f"Saldo: PEN{self.saldo}") 

# banco = Banco("Luz", "Jimenez", 75604355, 1234567890, 1000)
# banco.ver_estado_cuenta()
# banco.depositar(500)
# banco.retirar(200)
# banco.ver_estado_cuenta()


# Ejercicio 02
# crear uba clase agencia 
# con sus atributos nombre y apellidos del pasajero dni numero de asiento fecha de aviaje 
# sus metodos seran ingresar origen, ingresar destino, cancelar viaje, ver estado de pasaje 

class Agencia:
    def __init__(self, nombre, apellido, dni, numero_asiento, fecha_viaje):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.numero_asiento = numero_asiento
        self.fecha_viaje = fecha_viaje
        self.origen = None
        self.destino = None
        self.estado_viaje = "Reservado"

    def ingresar_origen(self, origen):
        self.origen = origen
        return f"Origen ingresado: {origen}"

    def ingresar_destino(self, destino):
        self.destino = destino
        return f"Destino ingresado: {destino}"

    def cancelar_viaje(self):
        self.estado_viaje = "Cancelado"
        return"Viaje cancelado"

    def ver_estado_viaje(self):
        return f"Nombre: {self.nombre} {self.apellido}"
        return f"DNI: {self.dni}" 
        return f"Número de asiento: {self.numero_asiento}"
        return f"Fecha de viaje: {self.fecha_viaje}"
        return f"Origen: {self.origen}"
        return f"Destino: {self.destino}"
        return f"Estado del viaje: {self.estado_viaje}"

agencia = Agencia("Juan", "Castañeda", 40786521, 10, "2024-03-16")
agencia.ver_estado_viaje()
agencia.ingresar_origen("Lima")
agencia.ingresar_destino("Luna Pizarro")
agencia.ver_estado_viaje()
agencia.cancelar_viaje()
agencia.ver_estado_viaje()