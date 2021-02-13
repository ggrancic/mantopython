"""
Escribir un programa que lea el radio de un círculo y a continuación visualice: circunferencia del
círculo, área del círculo o diámetro del círculo.
"""

import math

radio = float(input('Ingresa el valor del radio: '))

diametro = 2 * radio

area = (math.pi * (radio ** 2))

circunferencia = math.pi * diametro

print('Circunferencia:', circunferencia,'\nÁrea:', area, '\nDiámetro:', diametro)