# librerias 
from typing import List, Dict, Any, Callable,Protocol
import icecream as ic

class Motor_funciones(Protocol):
    def acelerar(self) -> Any:
        ...

    def detener(self) -> Any:
        ...
    
    def contador_giros(self) -> Any:
        ...
    
    def pasos_p_vueltas(self) -> int|float:
        ...
