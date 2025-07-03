from typing import List, Dict, Any, Callable, Literal
from motor.base import Motor_funciones
from icecream import ic
from machine import Pin
import time as tm


class Motor(Motor_funciones):
    """ 
    Clase para el control de la velocidad del motor

    Parameters:
    -----------
    `None`

    Atributes:
    ----------
        `__giros`: int
        `__velocidadactual`: int

    Methods:
    --------
    `acelerar`: void
    `detener`: void
    """
    #Variables del motor
    pulsoscvuelta:int = 200;
    pin_motor:List[Pin] = [];
    microstepping:int = 16;


    def __init__(self) -> None:
        self.giros:int = 0
        self.velocidadactual:int|float = 0 

    


    ##    
    def exceptions(mensaje:List[str]|Literal["Error al calcular la velocidad","Error al modificar la velocidad"]) -> Any:
        def decorator(func:Callable) -> Callable[...,Any]:
            def wr(*args, **kwargs) -> Any:
                try:
                    return func(*args,**kwargs)
                except Exception as e:
                    ic(f"Error al calcular los datos en la funcion {func.__name__}: {mensaje}",e)
                return wr
            return decorator 
    


    @exceptions("Error al modificar la velocidad")
    def aceleración(self) -> Any:
        """
        Aumenta la velocidad del motor en una dependiendo de la cantidad de giros
        Parameters:
        -----------
        `None`

        Returns:
        ----------
        `None`
        """
        #Introducir un while para ir modifican#
    

    def velocidad(self, frecuencia_pasos:float) -> int|float:
        """
        Calculo de la velocidad del motor en funcion de la cantidad de pasos
        """
        total_pasos_vuelta = self.pulsoscvuelta * self.microstepping

        velocidad = (frecuencia_pasos * 60) / total_pasos_vuelta
        self.velocidadactual = velocidad;

        return self.velocidadactual
        #Calculo de la velocidad con respecto a los datos #
    
    
    def pasos_p_vueltas(self, vueltas:int|float = 1) -> int|float:
        """
        Calcula el numero de micropasos para realizar una vuelta
        """
        return self.pulsoscvuelta * self.microstepping
    