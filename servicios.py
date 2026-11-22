# ==========================================
# SOFTWARE FJ - GESTION DE SERVICIOS
# ==========================================

from abc import ABC, abstractmethod
from excepciones import ValidacionError, ServicioError
from registro import registrar_evento


# ==========================================
# CLASE ABSTRACTA SERVICIO
# ==========================================

class Servicio(ABC):

    def __init__(self, nombre, precio_base):

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValidacionError("El nombre del servicio es obligatorio.")

        if not isinstance(precio_base, (int, float)) or precio_base <= 0:
            raise ValidacionError("El precio base debe ser mayor a cero.")

        self.nombre = nombre.strip()
        self.precio_base = float(precio_base)
        self.disponible = True

            # Metodo que simula sobrecarga de calculo de costos
    def calcular_costo_opciones(self, cantidad, *args):

        # Validar cantidad de argumentos adicionales
        if len(args) == 0:
            return self.calcular_costo(cantidad)

        elif len(args) == 1:
            descuento = args[0]

            if not 0 <= descuento <= 100:
                raise ValidacionError("El descuento debe estar entre 0 y 100.")

            return self.calcular_costo(cantidad, descuento)

        elif len(args) == 2:
            descuento, impuesto = args

            if not 0 <= descuento <= 100:
                raise ValidacionError("El descuento debe estar entre 0 y 100.")

            if not 0 <= impuesto <= 100:
                raise ValidacionError("El impuesto debe estar entre 0 y 100.")

            return self.calcular_costo(cantidad, descuento, impuesto)

        else:
            raise ValidacionError("Cantidad de parametros incorrecta.")

    @abstractmethod
    def calcular_costo(self, cantidad, descuento=0, impuesto=0):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    @abstractmethod
    def validar_parametros(self, cantidad):
        pass


# ==========================================
# SERVICIO 1: RESERVA DE SALAS
# ==========================================

class ServicioSala(Servicio):

    def validar_parametros(self, cantidad):

        if not isinstance(cantidad, (int, float)) or cantidad <= 0:
            raise ServicioError("Las horas deben ser mayores a cero.")

    def calcular_costo(self, cantidad, descuento=0, impuesto=0):

        self.validar_parametros(cantidad)

        subtotal = self.precio_base * cantidad
        subtotal -= subtotal * (descuento / 100)
        total = subtotal + (subtotal * (impuesto / 100))

        return round(total, 2)

    def describir_servicio(self):

        return f"Reserva de sala: {self.nombre}. Precio por hora: ${self.precio_base}"


# ==========================================
# SERVICIO 2: ALQUILER DE EQUIPOS
# ==========================================

class ServicioEquipo(Servicio):

    def validar_parametros(self, cantidad):

        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ServicioError("La cantidad de equipos debe ser un entero positivo.")

    def calcular_costo(self, cantidad, descuento=0, impuesto=0):

        self.validar_parametros(cantidad)

        subtotal = self.precio_base * cantidad
        subtotal -= subtotal * (descuento / 100)
        total = subtotal + (subtotal * (impuesto / 100))

        return round(total, 2)

    def describir_servicio(self):

        return f"Alquiler de equipo: {self.nombre}. Precio por unidad: ${self.precio_base}"


# ==========================================
# SERVICIO 3: ASESORIAS ESPECIALIZADAS
# ==========================================

class ServicioAsesoria(Servicio):

    def validar_parametros(self, cantidad):

        if not isinstance(cantidad, (int, float)) or cantidad <= 0:
            raise ServicioError("La duración de la asesoría debe ser positiva.")

    def calcular_costo(self, cantidad, descuento=0, impuesto=0):

        self.validar_parametros(cantidad)

        subtotal = self.precio_base * cantidad
        subtotal -= subtotal * (descuento / 100)
        total = subtotal + (subtotal * (impuesto / 100))

        return round(total, 2)

    def describir_servicio(self):

        return f"Asesoría especializada: {self.nombre}. Precio por hora: ${self.precio_base}"