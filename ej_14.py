"""
La relación entre los lados (a, b) de un triángulo rectángulo y la hipotenusa (h) viene dada por la
fórmula.

a2 + b2 = h2

Escribir un programa que lea la longitud de los lados y calcule la hipotenusa.
"""

import math

lado1 = float(input('Ingrese la longitud del lado a: '))
lado2 = float(input('Ingrese la longitud del lado b: '))

hipotenusa = (lado1 ** 2) + (lado2 ** 2)

print('El valor de la hipotenusa es:', math.sqrt(hipotenusa))