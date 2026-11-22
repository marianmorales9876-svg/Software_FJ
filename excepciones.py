# ==========================================
# SOFTWARE FJ - EXCEPCIONES PERSONALIZADAS
# ==========================================

# Clase base para los errores del sistema.
class SoftwareFJError(Exception):
    """Excepción base del sistema Software FJ."""
    pass


# Error cuando los datos ingresados no son válidos.
class ValidacionError(SoftwareFJError):
    """Error en la validación de datos."""
    pass


# Error cuando un cliente no existe o es incorrecto.
class ClienteError(SoftwareFJError):
    """Error relacionado con los clientes."""
    pass


# Error cuando un servicio presenta problemas.
class ServicioError(SoftwareFJError):
    """Error relacionado con los servicios."""
    pass


# Error cuando una reserva no puede realizarse.
class ReservaError(SoftwareFJError):
    """Error relacionado con las reservas."""
    pass


# Error cuando se intenta realizar una operación no permitida.
class OperacionError(SoftwareFJError):
    """Error en una operación del sistema."""
    pass