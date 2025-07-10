class Data:
    pass
class Complete:
    pass
class Lent:
    pass

#Datos adquiridos
class Datos(Data):
    def __init__(self, tiempo_restante: float):
        """
        Inicializa el objeto con el tiempo restante.
        Usar __init__ es la forma correcta de crear un constructor en Python.
        """
        self.tiempo_restante = tiempo_restante

    def obtener_tiempo(self) -> float:
        """
        Devuelve el tiempo restante. Este método ahora es accesible por otras clases.
        """
        return self.tiempo_restante

#Abrir completa
class Apertura_Com(Complete):
    def apertura_com(self, datos: Datos) -> bool:
        """
        Esto determinará si el tiempo es el justo para realizar la apertura completa.
        Ejemplo: abrir si queda poco tiempo (<= 2 unidades).
        """
        tiempo = datos.obtener_tiempo()  # Llamada correcta al método
        if tiempo <= 2:
            print("Apertura completa activada")
            return True
        else:
            print("La apertura completa falló")  # Mensaje más claro
            return False

#Ajuste lento
class Apertura_Len(Lent):  # Corregido el typo "Apentura"
    def apertura_len(self, datos: Datos) -> bool:
        """
        Determina si el tiempo se acerca para abrir de forma lenta.
        """
        tiempo = datos.obtener_tiempo()  # Llamada correcta al método
        if tiempo <= 7:
            print("Apertura lenta activa")  # Corregido el typo "Aperura"
            return True
        else:
            print("Apertura lenta fallida")  # Mensaje más claro
            return False

#Si es necesario, calcular el error de los tiempos, velocidad y aceleracion, obtenidos con los calculados por el programa