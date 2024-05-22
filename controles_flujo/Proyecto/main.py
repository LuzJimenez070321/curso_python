
# Base de datos simulada de horarios disponibles
horarios_disponibles = {
    '1': {'fecha': '2024-05-22', 'hora': '10:00', 'costo': 10},
    '2': {'fecha': '2024-05-22', 'hora': '12:00', 'costo': 15},
    '3': {'fecha': '2024-05-22', 'hora': '14:00', 'costo': 20}
}

# Mostrar los horarios disponibles
print("Horarios disponibles:")
for key, value in horarios_disponibles.items():
    print(f"{key}: Fecha: {value['fecha']} Hora: {value['hora']} Costo: ${value['costo']}")

# Reservar un horario
seleccion = input("Seleccione el número de horario que desea reservar: ")
horario_seleccionado = horarios_disponibles.get(seleccion)
if horario_seleccionado:
    print(f"Ha reservado el horario para el {horario_seleccionado['fecha']} a las {horario_seleccionado['hora']}")
    # Proceso de pago simulado
    print(f"Se ha realizado el pago de ${horario_seleccionado['costo']}")
    # Verificar la reserva
    print("Detalles de la reserva:")
    print(f"Fecha: {horario_seleccionado['fecha']}")
    print(f"Hora: {horario_seleccionado['hora']}")
    print(f"Costo: ${horario_seleccionado['costo']}")
else:
    print("Horario no válido. Intente de nuevo.")

