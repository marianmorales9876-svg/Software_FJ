# ==========================================
# SOFTWARE FJ - GESTION DE RESERVAS
# ==========================================

from clientes import Cliente
from servicios import Servicio
from excepciones import ReservaError, ValidacionError
from registro import registrar_evento, registrar_excepcion


class Reserva:
    """
    Representa una reserva realizada por un cliente
    para utilizar un servicio de Software FJ.
    """

    contador = 0

    def __init__(self, cliente, servicio, cantidad):

        # Validar que exista un cliente valido
        if not isinstance(cliente, Cliente):
            raise ReservaError("La reserva requiere un cliente valido.")

        # Validar que exista un servicio valido
        if not isinstance(servicio, Servicio):
            raise ReservaError("La reserva requiere un servicio valido.")

        # Validar cantidad
        if isinstance(cantidad, bool) or not isinstance(cantidad, (int, float)) or cantidad <= 0:
            raise ValidacionError("La cantidad debe ser mayor a cero.")

        # Validar disponibilidad del servicio
        if not servicio.disponible:
            raise ReservaError("El servicio no se encuentra disponible.")

        # Crear identificador unico
        Reserva.contador += 1
        self.__id = Reserva.contador

        # Guardar datos de la reserva
        self.__cliente = cliente
        self.__servicio = servicio
        self.__cantidad = cantidad
        self.__estado = "Pendiente"

        # Calcular costo inicial
        self.__costo = servicio.calcular_costo(cantidad)

        registrar_evento(f"Reserva {self.__id} creada correctamente.")

    # Consultar identificador
    @property
    def id(self):
        return self.__id

    # Consultar estado
    @property
    def estado(self):
        return self.__estado

    # Consultar costo
    @property
    def costo(self):
        return self.__costo

    # Confirmar reserva
    def confirmar(self):

        if self.__estado != "Pendiente":
            raise ReservaError("Solo se pueden confirmar reservas pendientes.")

        if not self.__servicio.disponible:
            raise ReservaError("El servicio ya no esta disponible.")

        self.__estado = "Confirmada"

        registrar_evento(f"Reserva {self.__id} confirmada.")

        return "Reserva confirmada correctamente."

    # Cancelar reserva
    def cancelar(self):

        if self.__estado == "Cancelada":
            raise ReservaError("La reserva ya se encuentra cancelada.")

        self.__estado = "Cancelada"

        registrar_evento(f"Reserva {self.__id} cancelada.")

        return "Reserva cancelada correctamente."

    # Procesar reserva con manejo de excepciones
       # Procesar reserva con manejo de excepciones
    def procesar(self):
        try:
            if self.__estado == "Cancelada":
                raise ReservaError("No se puede procesar una reserva cancelada.")

            if not self.__servicio.disponible:
                raise ReservaError("El servicio no esta disponible.")

            registrar_evento(f"Procesando reserva {self.__id}.")

            resultado = self.confirmar()

        except Exception as error:
            registrar_excepcion(
                f"Error al procesar reserva {self.__id}: {error}"
            )
            raise ReservaError(
                "No fue posible procesar la reserva."
            ) from error

        else:
            return resultado

        finally:
            registrar_evento(
                f"Finalizado el intento de procesamiento de reserva {self.__id}."
            )
    # Mostrar informacion de la reserva
    def mostrar_informacion(self):

        return (
            f"Reserva N. {self.__id} | "
            f"Cliente: {self.__cliente.nombre} | "
            f"Servicio: {self.__servicio.nombre} | "
            f"Cantidad: {self.__cantidad} | "
            f"Costo: ${self.__costo:.2f} | "
            f"Estado: {self.__estado}"
        )