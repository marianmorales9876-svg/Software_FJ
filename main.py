# ==========================================
# SOFTWARE FJ - PRUEBAS DE RESERVAS
# ==========================================

from clientes import Cliente
from servicios import ServicioSala, ServicioEquipo, ServicioAsesoria
from reservas import Reserva
from excepciones import ReservaError, ValidacionError
from registro import registrar_error

print("\n===== PRUEBAS DE RESERVAS SOFTWARE FJ =====\n")

# Crear clientes
cliente1 = Cliente("Marian Morales", "10203040", "marian@gmail.com", "3101234567")
cliente2 = Cliente("Carlos Perez", "12345678", "carlos@gmail.com", "3111234567")

# Crear servicios
sala = ServicioSala("Sala principal", 50000)
equipo = ServicioEquipo("Video beam", 30000)
asesoria = ServicioAsesoria("Asesoria de programacion", 80000)

# Listas para almacenamiento interno del sistema
lista_clientes = [cliente1, cliente2]

lista_servicios = [sala, equipo, asesoria]

lista_reservas = [] 

# PRUEBA 1: Crear reserva de sala
try:
    reserva1 = Reserva(cliente1, sala, 2)
    lista_reservas.append(reserva1) 
    print("1. Reserva creada:")
    print(reserva1.mostrar_informacion())
except Exception as error:
    print("Error:", error)

# PRUEBA 2: Confirmar reserva
try:
    print("\n2.", reserva1.confirmar())
    print(reserva1.mostrar_informacion())

except ReservaError as error:
    registrar_error(f"Prueba 2 - {error}")
    print("\n2. Error controlado:")
    print(error)

# PRUEBA 3: Crear reserva de equipos
try:
    reserva2 = Reserva(cliente2, equipo, 2)
    lista_reservas.append(reserva2) 
    print("\n3. Reserva de equipos creada:")
    print(reserva2.mostrar_informacion())

except Exception as error:
    registrar_error(f"Prueba 3 - {error}")
    print("\n3. Error controlado:")
    print(error)

# PRUEBA 4: Procesar reserva de asesoría

try:
    reserva3 = Reserva(cliente1, asesoria, 1)
    lista_reservas.append(reserva3) 
    print("\n4. Procesamiento de asesoria:")
    print(reserva3.procesar())
    print(reserva3.mostrar_informacion())

except Exception as error:
    registrar_error(f"Prueba 4 - {error}")
    print("\n4. Error controlado:")
    print(error)

# PRUEBA 5: Cancelar reserva
try:
    print("\n5.", reserva2.cancelar())
    print(reserva2.mostrar_informacion())

except Exception as error:
    registrar_error(f"Prueba 5 - {error}")
    print("\n5. Error controlado:")
    print(error)

# PRUEBA 6: Intentar confirmar reserva cancelada
try:
    reserva2.confirmar()

except ReservaError as error:
    registrar_error(f"Prueba 6 - {error}")
    print("\n6. Error controlado:")
    print(error)

# PRUEBA 7: Cliente inválido
try:
    Reserva("Cliente incorrecto", sala, 1)

except ReservaError as error:
    registrar_error(f"Prueba 7 - {error}")
    print("\n7. Error controlado:")
    print(error)

# PRUEBA 8: Servicio inválido

try:
    Reserva(cliente1, "Servicio incorrecto", 1)

except ReservaError as error:
    registrar_error(f"Prueba 8 - {error}")
    print("\n8. Error controlado:")
    print(error)

# PRUEBA 9: Cantidad negativa
try:
    Reserva(cliente1, sala, -3)

except ValidacionError as error:
    registrar_error(f"Prueba 9 - {error}")
    print("\n9. Error controlado:")
    print(error)

# PRUEBA 10: Servicio no disponible
try:
    sala.disponible = False
    Reserva(cliente1, sala, 1)

except ReservaError as error:
    registrar_error(f"Prueba 10 - {error}")
    print("\n10. Error controlado:")
    print(error)

finally:
    sala.disponible = True
    # Almacenamiento interno de las reservas creadas

# Mostrar el total de reservas almacenadas
print("\n--- ALMACENAMIENTO INTERNO ---")
print("Clientes registrados:", len(lista_clientes))
print("Servicios registrados:", len(lista_servicios))
print("Reservas almacenadas:", len(lista_reservas))
# Consultar las reservas almacenadas
for reserva in lista_reservas:
    print(reserva.mostrar_informacion())
    