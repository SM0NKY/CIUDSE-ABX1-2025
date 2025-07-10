from Fuerza_G.Data_G import SensorAcelerometro

class Air_open:
    """
    Clase base para sistemas de apertura de aire (Air Brakes).
    
    Esta clase puede ser utilizada como base para diferentes tipos de mecanismos de apertura,
    permitiendo una estructura común y la posibilidad de extender funcionalidades en el futuro.
    Actualmente no define métodos ni atributos, pero sirve como punto de partida para herencia.
    """
    pass

# Instancia global del sensor (puedes mover esto dentro de la clase si prefieres)
mi_sensor = SensorAcelerometro()

class AirBrakes(Air_open):
    """
    Clase que representa el sistema de Air Brakes controlado por fuerzas G.
    
    Hereda de Air_open para mantener una estructura jerárquica y permitir futuras extensiones
    o especializaciones de mecanismos de apertura.
    """
    def recolectar_datos(self):
        """
        Recolecta los datos de fuerzas G de los acelerómetros.
        Utiliza el sensor global para obtener las fuerzas G actuales en los ejes x, y, z.
        
        Returns:
            dict: Diccionario con las fuerzas G de cada eje.
        """
        self.datos_g = mi_sensor.calcular_fuerzas_g()
        print("Fuerzas G recolectadas:", self.datos_g)
        return self.datos_g

    def apertura(self, umbral: float = 5.0):
        """
        Determina si es necesario abrir los Air Brakes según las fuerzas G.
        Compara el valor absoluto de las fuerzas G en cada eje con un umbral dado.
        Si alguna fuerza G supera el umbral, se considera necesario abrir.
        
        Args:
            umbral (float): Valor de referencia para decidir la apertura.
        Returns:
            bool: True si se debe abrir, False en caso contrario.
        """
        fuerzas = self.recolectar_datos()
        # Ejemplo: abrir si la fuerza G en cualquier eje supera el umbral
        if any(abs(g) >= umbral for g in fuerzas.values()):
            print("Es necesario realizar la apertura de los Air Brakes")
            return True
        else:
            print("No es momento de abrir con respecto a las fuerzas G")
            return False