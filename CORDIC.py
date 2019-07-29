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
    
    """ Iteración de rotación de un vector en un ángulo en radianes 
    
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
        Nuevo resto angular en radianes
        
    """
    if angle_accumulator > 0:
        direction_i = 1
    else:
        direction_i = -1
    
    x = x_i - y_i*direction_i*(2**(-i))
    y = y_i + x_i*direction_i*(2**(-i)) 

    angle_accumulator = angle_accumulator - direction_i*math.atan(2**(-i))
    
    return x, y, angle_accumulator


def multiple_rotations(initial_angle, rotation_angle, iterations):
	""" Múltiples corrimientos de corrección al ángulo de rotación

	Parámetros
	----------
	initial_angle : float
		Ángulo inicial del vector en radianes.

	rotation_angle : float
		Ángulo a rotar en radianes.

	iterations : int
		Cantidad de iteraciones del algoritmo.

	Retornos
	--------
	x : float
		Posición final en x

	y : float
		Posición final en y

	angle_accumulator : float
		Resto del ángulo del corrimiento

	"""

	i = 0

	x = math.cos(initial_angle)
	y = math.sin(initial_angle)

	angle_accumulator = rotation_angle

	while i < iterations:
		x, y, angle_accumulator = rotation_mode(x, y, i, angle_accumulator)
		i += 1

	return x, y, angle_accumulator


def preprocess(initial_angle,rotation_angle, iterations):
	""" Ajustes del ángulo inicial

	Parámetros
	----------
	initial_angle : float
		Ángulo inicial del vector en radianes.

	rotation_angle : float
		Ángulo a rotar en radianes.

	iterations : int
		Cantidad de iteraciones del algoritmo.

	"""

	#if initial_angle < 180


# =============================================================================
# PRUEBAS
# =============================================================================


initial_angle = (-90*math.pi)/180
rotation_angle = (-100*math.pi)/180

x, y, angle_accumulator = multiple_rotations(initial_angle, rotation_angle, 30)

if x < 0 and y > 0:
	angle = 180 + (math.atan(y/x)*180)/math.pi

elif x < 0 and y < 0:
	angle = -180 + (math.atan(y/x)*180)/math.pi

else :
	angle = (math.atan(y/x)*180)/math.pi

print(angle, angle_accumulator)

