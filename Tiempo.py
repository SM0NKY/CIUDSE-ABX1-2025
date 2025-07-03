class Data:
    pass
class Complete:
    pass
class Lent:
    pass
#Datos adquiridos
class Datos(Data):
    def Time(self, tiempo_restante):
        """
        Tiempo restante hasta apogeo o aterrizaje (en días, minutos, etc.).
        """
        self.tiempo_restante = tiempo_restante

        def obtener_datos(self):
            return self.tiempo_restante
#Abrir completa
class Apertura_Com(Complete):
    def apertura_com(self, datos:Datos):
        """
        Esto determinará si el tiempo es el justo para realizar la apertura completa.
        Ejemplo: abrir si queda poco tiempo (<= 2 unidades
        """
        tiempo = datos.obtener_tiempo()
        if tiempo <=2:
            print("Apertura completa activada")
            return True
        else:
            print("La apertura fallo")
            return False

#Aluste lento
class Apentura_Len(Lent):
    def apertura_len(self, datos:Datos):
        """
        Esto determinara su si el timepo se acerca para abrir de forma lenta:
        """
        tiempo = datos.obtener_tiempo()
        if tiempo <= 7:
            print("Aperura lenta activa")
            return True
        else:
            print("Apertura fallida")
            return False