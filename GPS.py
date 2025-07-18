class Datos:
    pass
class Correccion:
    pass

class Datos_Pos(Datos):
    def Datos_Ad(self, Data_Posi):
        """
        Estos son los datos que se adqieren segun laa posicion horizontal
        """
        self.Data_Pos = Data_Posi
        def Obtenerer_Da(self):
            return self.Data_posi
        
class Correc(Correccion):
    def Correc_Data(self, Datos:Datos_Pos):
        """
        Esto es para la correccion de la posicion
        """
        Posicion = self.obtener_Data()
        if Posicion >= 5 | Posicion <= -5:
            print("Se requiere de correcciones")
            return True
        else:
            print("No se requere de correcciones")
            return False
        
        #Todo este codigo es solo para hacer las correcciones horizontales