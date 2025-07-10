from typing import Protocol, Any

class Sensores(Protocol):
    """
    Bases de las funciones del sensor acelerometro
    """
    
    def actualizar_aceleracion(self) -> Any:
        ...
    def obtener_aceleracion_actual(self) -> Any:
        ...
    def calcular_fuerzas_g(self) -> Any:
        ...

class Airbk(Protocol):
    """
    Bases para las funciones de los airbreaks
    """

    def recolectar_datos(self) -> Any:
        ...
    def apertura(self) -> Any:
        ...

