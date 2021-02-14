"""
Hacer un algoritmo que calcule el área de un triángulo, pidiendo al usuario los datos que son
necesarios para calcularlo.
"""

base = float(input('Ingresa la longitud de la base: '))
altura = float(input('Ingresa la longitud de la altura: '))

area = (base * altura) / 2

print('El área del triángulo es:', area, 'm2')