class Data_micro:
    pass

g = 9.81
#datos de la aceleracion que se buscan adquirir
class Microcon(Data_micro):
 def Datos(self): 
    """
    Guarda los datos de la aceleracion
    """
    self.Ejes = {"x": 0.0, "y": 0.0, "z": 0.0}

    def  Eje (self, Ejes):
        """
        Guardara los datos
        """
        self.Ejes = Ejes

        def Acele(self):
            """
            Esto devuelve la aceleracion actual
            """
            return self.Ejes
        def Fuerza_G(self):
            """
            Esto es para calcular las fuerzas G
            """
            for eje, valor in self.Ejes.items():
                return {eje:round(valor/g, 2)}
        print("Fuerza G", Fuerza_G())