from typing import List, Dict, Any, Callable, Literal
from motor.base import Motor_funciones ; from tiempo import Time
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
        self.tiempo_utilizado = 1;
        self.tiempo_actual = 0;
    


    ##    
    @staticmethod
    def exceptions(mensaje:List[str]|Literal["Error al calcular la velocidad","Error al modificar la velocidad"]) -> Any:
        def decorator(func:Callable) -> Callable[...,Any]:
            def wr(*args, **kwargs) -> Any:
                try:
                    return func(*args,**kwargs)
                except Exception as e:
                    ic(f"Error al calcular los datos en la funcion {func.__name__}: {mensaje}",e)
                return wr
            return decorator 
    


    def pasos_p_vueltas(self, vueltas:int|float = 1) -> int|float:
        """
        Calcula el numero de micropasos para realizar una vuelta
        """
        return self.pulsoscvuelta * self.microstepping
    


    def acelerar(self, velocidad_final: float, tiempo_aceleracion: float = 2.0) -> float:
        """
        Acelera el motor gradualmente hasta la velocidad objetivo
        
        Parameters:
        -----------
        `velocidad_final`: float - Velocidad objetivo en RPM
        `tiempo_aceleracion`: float - Tiempo para alcanzar la velocidad (segundos)
        
        Returns:
        ----------
        `float` - Aceleración calculada en RPM/s²
        """

        velocidad_inicial = self.velocidadactual
        
        # Calcular aceleración necesaria
        aceleracion = (velocidad_final - velocidad_inicial) / tiempo_aceleracion
        
        # Aplicar aceleración gradualmente
        self.aplicar_aceleracion(aceleracion, tiempo_aceleracion)
        
        return aceleracion

    
    
    def aplicar_aceleracion(self, aceleracion: float, tiempo: float):
        """
        Aplica la aceleración al motor paso a paso

        Parameters:
        -----------
        `aceleracion`: float - Velocidad de aceleración en RPM/s
        `tiempo`: float - Tiempo de aceleración en segundos

        Returns:
        ----------
        `None`
        """
        tiempo_inicio = tm.time()
        velocidad_actual = self.velocidadactual
        
        while tm.time() - tiempo_inicio < tiempo:
            # Calcular nueva velocidad
            tiempo_transcurrido = tm.time() - tiempo_inicio
            nueva_velocidad = velocidad_actual + (aceleracion * tiempo_transcurrido)
            
            # Aplicar velocidad al motor
            self.ajustar_velocidad_motor(nueva_velocidad)
            
            # Pequeña pausa para control
            tm.sleep(0.01)
        
        # Asegurar velocidad final exacta
        self.velocidadactual = velocidad_actual + (aceleracion * tiempo)

    def ajustar_velocidad_motor(self, velocidad_rpm: float) -> None:
        """
        Convierte RPM a frecuencia de pasos y ajusta el motor
        """
        # Convertir RPM a frecuencia de pasos
        frecuencia_pasos = (velocidad_rpm * self.pasos_p_vueltas()) / 60
        
        # Aplicar al motor (aquí iría tu lógica de control del motor)
        self.velocidadactual = velocidad_rpm
        
        # AQUÍ VAN LAS INSTRUCCIONES PARA HACER GIRAR EL MOTOR
        self.controlar_motor_pasos(frecuencia_pasos)

    def desacelerar(self, velocidad_final: float, tiempo_desaceleracion: float = 2.0) -> float:
        """
        Desacelera el motor gradualmente 

        Parameters:
        -----------
        `velocidad_final`: float - Velocidad final del motor en RPM
        `tiempo_desaceleracion`: float - Tiempo de desaceleración en segundos

        Returns:
        ----------
        `velocidad_actual`: float - Velocidad actual del motor en RPM
        """
        return self.acelerar(velocidad_final, tiempo_desaceleracion)


    def controlar_motor_pasos(self, frecuencia_pasos: float) -> None:
        """
        Controla el motor paso a paso con la frecuencia especificada
        
        Parameters:
        -----------
        `frecuencia_pasos`: float - Frecuencia en Hz (pasos por segundo)

        Returns:
        ----------
        `None`
        """
        
        # Por el momento este es un esquema solamente de prueba
        
        if frecuencia_pasos > 0:
            # Calcular tiempo entre pasos
            tiempo_entre_pasos = 1.0 / frecuencia_pasos
            
            # Secuencia de pasos para el motor (ejemplo para 4 pines)
            secuencia = [
                [1, 0, 0, 0],
                [0, 1, 0, 0], 
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ]
            
            # Aplicar secuencia al motor
            for paso in secuencia:
                for i, pin in enumerate(self.pin_motor):
                    pin.value(paso[i])
                tm.sleep(tiempo_entre_pasos)