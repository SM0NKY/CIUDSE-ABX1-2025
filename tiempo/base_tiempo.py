from typing import Protocol
from dataclasses import dataclass

@dataclass
class Time(Protocol):
    tiempo_calculado:int|float;    # Tiempo teórico esperado
    tiempo_real:int|float;       # Tiempo real medido
    tiempo_aceleracion:int|float;    # Tiempo para alcanzar velocidad
    tiempo_frenado:int|float;    # Tiempo para detenerse
    tiempo_total:int|float;      # Tiempo total