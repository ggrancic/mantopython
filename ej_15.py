"""
El área del triángulo cuyos lados son a, b y c se puede calcular por la formula

A= √ p( p−a)( p−b)( p−c )

Donde p = (a + b + c)/2. Escribir un programa que lea las longitudes de los tres lados de un triángulo y
calcule el área del triangulo.

"""

import math

a = float(input('Ingrese la longitud del lado a: '))
b = float(input('Ingrese la longitud del lado b: '))
c = float(input('Ingrese la longitud del lado c: '))

# Calculo de p (semiperimetro).

p = (a + b + c)/2

# Calculo del area (formula de heron)

area = math.sqrt(p * (p-a) * (p-b) * (p-c))

print('El área del tríangulo es:', area)