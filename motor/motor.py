from typing import List, Dict, Any, Callable
from motor.base import Motor
from icecream import ic
from machine import Pin
import time as tm


class Motor():
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
    pulsoscvuelta:int;
    pin_motor:List[Pin,Pin] = [];


    def __init__(self) -> object:
        self.giros:int = 0
        self.velocidadactual:int = 0 
        
    
    def acelerar(self) -> None:
        """
        Aumenta la velocidad del motor en una dependiendo de la cantidad de giros
        Parameters:
        -----------
        `None`

        Returns:
        ----------
        `None`
        """

    def velocida(self) -> int:
        ...
        #Calculo de la velocidad con respecto a los datos #