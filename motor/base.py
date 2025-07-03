# librerias 
from typing import List, Dict, Any, Callable,Protocol
import icecream as ic

class Motor_funciones(Protocol):
    
    def acelerar() -> None:
        ...
    
    def detener() -> None:
        ...
    
    def contador_giros() -> int:
        ...
    

