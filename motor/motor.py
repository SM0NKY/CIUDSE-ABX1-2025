from typing import List, Dict, Any, Callable
from motor.base import Motor

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
    def __init__(self,) -> object:
        self.__giros:int = 0
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