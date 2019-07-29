# -*- coding: utf-8 -*-

"""
Módulo de simulación del modo de rotación bidimensional del algoritmo CORDIC
"""

# Sistemas Digitales - FIUBA
# José F González <jfgonzalez@fi.uba.ar>


import math


# =============================================================================
# FUNCIONES
# =============================================================================

def rotation_mode(x_i, y_i, i, angle_accumulator):
    
    """ Iteración de rotación de un vector en un ángulo 
    
    Parámetros
    ----------
    x_i : float 
        Posición inicial del vector en x
    
    y_i : float
        Posición inicial del vector en y
    
    i : int
        Contador de iteraciones
        
    angle_accumulator : float
        Resto del ángulo a desplazar en radianes.
        En i = 0 es el ángulo deseado a rotar.
        
    Retornos
    --------
    x : float
        Posición final del vector en x
        
    y : float
        Posición final del vector en y
        
    angle_accumulator : float    
        Nuevo resto angular
        
    """
    
    if angle_accumulator < 0:
        direction_i = 1
    else:
        direction_i = -1
    
    x = x_i - y_i*direction_i*(2**(-i))
    y = y_i + x_i*direction_i*(2**(-i))
    
    angle_accumulator = angle_accumulator - direction_i*math.atan(2**(-i))
    
    return x, y, angle_accumulator


x, y, angle = rotation_mode(0.939, 0.342, 0 , 20)
print(x,y,angle)

