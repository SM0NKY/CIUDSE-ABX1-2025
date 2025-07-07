class Air_open:
    pass

from Data_G import Microcon
mi_Microcon = Microcon()

class AirBrakes(Air_open):
    def Datos_Recolec(self, Datos):
        """
        Esto recoleecta los datos de los acelerometros 
        """
        self.Datos = mi_Microcon.Fuerza_G()

        def Apertura(self):
            """
            Esto determina la apertura segun las fuerzas
            """
            fuerza = mi_Microcon.Fuerza_G()
            print("Estas son las fuerza g de todos los ejes", fuerza)
            if Datos == 5:
                print("Es necesario realizar la apertura de los Air Brakes")
            else:
                print("No es momento de abrir con respecto a las fuerza G")