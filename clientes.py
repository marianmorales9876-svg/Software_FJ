# ==========================================
# SOFTWARE FJ - GESTION DE CLIENTES
# ==========================================

from excepciones import ValidacionError, ClienteError
from registro import registrar_evento, registrar_error


class Cliente:
    """
    Representa un cliente del sistema Software FJ.
    Protege los datos personales y valida la informacion.
    """

    def __init__(self, nombre, documento, correo, telefono):

        # Validar nombre
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValidacionError("El nombre no puede estar vacio.")

        # Validar documento
        if not str(documento).isdigit():
            raise ValidacionError("El documento debe contener solo numeros.")

        # Validar correo
        if not isinstance(correo, str) or "@" not in correo or "." not in correo:
            raise ValidacionError("El correo electronico no es valido.")

        # Validar telefono
        if not str(telefono).isdigit() or len(str(telefono)) < 7:
            raise ValidacionError("El telefono debe tener minimo 7 digitos.")

        # Encapsulacion de datos personales
        self.__nombre = nombre.strip()
        self.__documento = str(documento)
        self.__correo = correo.strip().lower()
        self.__telefono = str(telefono)

        registrar_evento(f"Cliente registrado: {self.__nombre}")

    # Consultar nombre
    @property
    def nombre(self):
        return self.__nombre

    # Consultar documento
    @property
    def documento(self):
        return self.__documento

    # Consultar correo
    @property
    def correo(self):
        return self.__correo

    # Consultar telefono
    @property
    def telefono(self):
        return self.__telefono

    # Mostrar informacion del cliente
    def mostrar_informacion(self):
        return (
            f"Nombre: {self.__nombre} | "
            f"Documento: {self.__documento} | "
            f"Correo: {self.__correo} | "
            f"Telefono: {self.__telefono}"
        )

    # Representacion del objeto
    def __str__(self):
        return f"Cliente: {self.__nombre} - CC: {self.__documento}"