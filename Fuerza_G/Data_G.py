from typing import Dict, Optional

class Data_micro:
    pass

class SensorAcelerometro(Data_micro):
    """
    Representa un sensor de acelerómetro para leer y procesar datos.

    Esta clase encapsula la lógica para manejar lecturas de aceleración
    de los ejes x, y, z, y proporciona un método para calcular las
    fuerzas G correspondientes. Es ideal para simular o interactuar con
    un sensor de hardware.

    Attributes:
        G (float): Atributo de clase que representa la constante de
            aceleración gravitacional (9.81 m/s^2).
        ejes (Dict[str, float]): Atributo de instancia que almacena los
            valores de aceleración actuales (en m/s^2) para los ejes 'x', 'y', 'z'.
    """
    G = 9.81  # Constante de gravedad como atributo de clase

    def __init__(self, ejes_iniciales: Optional[Dict[str, float]] = None):
        """
        Inicializa el sensor de acelerómetro.

        Corrige el uso de un argumento mutable por defecto. Usar `None` como
        valor predeterminado es la práctica recomendada en Python.

        Args:
            ejes_iniciales (Optional[Dict[str, float]]): Un diccionario con los
                valores iniciales de aceleración para los ejes 'x', 'y', 'z'.
                Si es `None`, los ejes se inicializan en 0.0.

        Example:
            >>> # Inicializar con valores predeterminados (todos los ejes a 0.0)
            >>> sensor_default = SensorAcelerometro()
            >>> print(sensor_default.obtener_aceleracion_actual())
            # Output:
            # {'x': 0.0, 'y': 0.0, 'z': 0.0}

            >>> # Inicializar con valores específicos
            >>> sensor_custom = SensorAcelerometro({"x": 9.81, "y": 0.5, "z": -0.2})
            >>> print(sensor_custom.obtener_aceleracion_actual())
            # Output:
            # {'x': 9.81, 'y': 0.5, 'z': -0.2}
        """
        if ejes_iniciales is None:
            self.ejes = {"x": 0.0, "y": 0.0, "z": 0.0}
        else:
            self.ejes = ejes_iniciales

    def actualizar_aceleracion(self, nueva_aceleracion: Dict[str, float]):
        """
        Actualiza los valores de aceleración (en m/s^2) para los ejes.

        Este método permite simular la llegada de nuevos datos desde un
        sensor físico.

        Args:
            nueva_aceleracion (Dict[str, float]): Un diccionario que contiene
                los nuevos valores de aceleración para 'x', 'y', 'z'.

        Example:
            >>> sensor = SensorAcelerometro()
            >>> print(f"Antes: {sensor.obtener_aceleracion_actual()}")
            >>> sensor.actualizar_aceleracion({"x": 19.62, "y": -9.81, "z": 0})
            >>> print(f"Después: {sensor.obtener_aceleracion_actual()}")
            # Output:
            # Antes: {'x': 0.0, 'y': 0.0, 'z': 0.0}
            # Después: {'x': 19.62, 'y': -9.81, 'z': 0}
        """
        self.ejes = nueva_aceleracion

    def obtener_aceleracion_actual(self) -> Dict[str, float]:
        """
        Obtiene el diccionario con la aceleración actual en m/s^2.

        Returns:
            Dict[str, float]: Un diccionario con la aceleración actual de cada
            eje ('x', 'y', 'z').

        Example:
            >>> sensor = SensorAcelerometro({"x": 9.81, "y": 0.0, "z": 0.0})
            >>> aceleracion = sensor.obtener_aceleracion_actual()
            >>> print(aceleracion)
            # Output:
            # {'x': 9.81, 'y': 0.0, 'z': 0.0}
        """
        return self.ejes

    def calcular_fuerzas_g(self) -> Dict[str, float]:
        """
        Calcula y devuelve las fuerzas G para cada eje.

        La fuerza G se calcula dividiendo el valor de aceleración de cada
        eje por la constante de gravedad G (9.81 m/s^2).

        Returns:
            Dict[str, float]: Un diccionario con el valor de las fuerzas G
            para cada eje, redondeado a 2 decimales.

        Example:
            >>> sensor = SensorAcelerometro()
            >>> sensor.actualizar_aceleracion({"x": 19.62, "y": -4.905, "z": 9.81})
            >>> fuerzas_g = sensor.calcular_fuerzas_g()
            >>> print(fuerzas_g)
            # Output:
            # {'x': 2.0, 'y': -0.5, 'z': 1.0}
        """
        fuerzas_g = {eje: round(valor / self.G, 2) for eje, valor in self.ejes.items()}
        return fuerzas_g