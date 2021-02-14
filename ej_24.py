# Escribir un programa que lea los lados de un rectángulo y calcule su área y perímetro.

base = float(input('Ingrese el valor de la base: '))
altura = float(input('Ingrese el valor de la altura: '))

area = base * altura
perimetro = (base * 2) + (altura * 2)

print('El área del rectángulo es:', area, 'm2')
print('El perímetro del rectángulo es:', perimetro)