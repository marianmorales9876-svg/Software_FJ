# ==========================================
# SOFTWARE FJ - REGISTRO DE EVENTOS Y ERRORES
# ==========================================

import logging
import os

# Crear la carpeta logs si todavía no existe.
os.makedirs("logs", exist_ok=True)

# Configurar el archivo donde se guardarán los registros.
logging.basicConfig(
    filename="logs/software_fj.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Registrar eventos informativos.
def registrar_evento(mensaje):
    logging.info(mensaje)
    print(f"[INFO] {mensaje}")

# Registrar errores del sistema.
def registrar_error(mensaje):
    logging.error(mensaje)
    print(f"[ERROR] {mensaje}")

# Registrar errores con información detallada.
def registrar_excepcion(mensaje):
    logging.exception(mensaje)
    print(f"[ERROR] {mensaje}")