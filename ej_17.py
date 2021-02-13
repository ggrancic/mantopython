"""
Hacer un algoritmo que permita ingresar un numero hasta el cual se mostrarán los números impares
que le anteponían, ejemplo:
usuario ingresa: 19
algoritmo muestra: 1,3,5,7,9,11,13,15,17
"""

cantidad = int(input('Ingresa la cantidad de números a visualizar: '))

for x in range(cantidad):

    if x % 2 != 0:

        print(x)