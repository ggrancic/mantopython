# Hacer un algoritmo que analice si en dos números ingresados: cual es mayor, cual es menor, o si son iguales.

n1 = int(input('Ingresa un número: '))
n2 = int(input('Ingresa otro número: '))

if n1 == n2:

    print('Son iguales.')

else:

    print('El mayor es:', max(n1, n2))
    print('El menor es:', min(n1, n2))