#Base de datos simuladas de horarios disponibles 
horarios_disponibles= {
    '1':{'fecha':'2024-05-22','hora':'10:00','costo':10},
    '2':{'fecha':'2024-05-22','hora':'12:00','costo':15},
    '3':{'fecha':'2024-05-22','hora':'14:00','costo':20}
    }
#mostrar los horarios disponibles
print("horarios disponibles")
for key, value in horarios_disponibles.imtems():
    print(f"{key}:Fecha:{value['fecha']} Hora:{value['hora']}Costo:${value['costo']}")
#reservar un horario 
seleccion=input("seleccione el numero de horarioque desea reservar")
horario_seleccionado
horarios_disponibles.get(seleccion)
if horario_seleccionado:
    print(f"ha reservado el horario para el {horario_seleccionado['fecha']} a las {horario_selecionado['costo']}")
#proceso de pago simulado
    print(f"se ha realizado el pago de ${horario_seleccionado['costo']}")
#verificar la reserva
    print("detalles de la reserva:")
    print(f"fecha: {horario_seleccionado['hora']}")
    print(f"costo:${horario_seleccionado['costo']}")
else:
    print("horario no valido.intente de nuevo")
