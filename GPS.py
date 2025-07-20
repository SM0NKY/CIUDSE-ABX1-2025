#Esto es para que sea fluido pero de igual manera hacer correcciones en dado caso de no necesitarse
import time
timestamp = time.time()
import matplotlib.pyplot as plt

#Visualización en tiempo real (matplotlib o folium)
plt.plot(1,2,3,4,5,6) #ejemplo
plt.title("Trayectoria hoizontal")
plt.ylabel("Tiempo")
plt.xlabel("Desplazamiento")
plt.show()
class Datos:
    pass
class Correccion:
    pass

class Datos_Pos(Datos):
    def __init__(self):
        self.data_pos = 0.0  # posición inicial

    def datos_adquiridos(self, data_posi):
        """
        Guarda los datos adquiridos de posición horizontal
        """
        self.data_pos = data_posi

    def obtener_dato(self):
        return self.data_pos
        
class Correc(Correccion):
    def Correc_Data(self, Datos:Datos_Pos):
        """
        Esto es para la correccion de la posicion
        """
        Posicion = Datos.Obtener_Datos()
        if Posicion >= 5 or Posicion <= -5:
            print("Se requiere de correcciones")
            return True
        else:
            print("No se requere de correcciones")
            return False
        
        #Todo este codigo es solo para hacer las correcciones horizontales



        #Esto es para probar sin un GPS
        """
        datos = [0, 2, 4, 6, 8, 10]
for d in datos:
    pos.datos_adquiridos(d)
    correc.correc_data(pos)
        """
