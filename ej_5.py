"""
Escribir un programa que convierte un número dado de segundos en el equivalente de minutos y
segundos.
"""
import math
tiempo = int(input('Ingresa el tiempo en segundos: '))

minutos = math.trunc(tiempo / 60)

segundos = tiempo - (minutos * 60)

print(str(minutos) + " minutos" + ": " + str(segundos) + " segundos")