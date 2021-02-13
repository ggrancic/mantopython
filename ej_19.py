"""
Hacer un algoritmo que muestre la tabla de multiplicar de un numero ingresado por el usuario. Y que
la muestre con el formato: A x B = C
"""

numero = int(input('Ingresa el numero del que quieres saber su tabla: '))

contador = 0

for x in range(numero + 1):

    producto = numero * x

    print(numero, '*', x, '=', producto)