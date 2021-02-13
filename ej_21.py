"""
Hacer un algoritmo que permita ingresar N números y que luego calcule la suma y el promedio de los
números ingresados.
"""

cantidad = 0
suma = 0

continuar = True

while continuar == True:

    opcion = input('Desea ingresar un numero?\nOPCION (S/N): ')

    if opcion.upper() == 'S':

        numero = int(input('Ingresa un número: '))

        suma += numero
        cantidad += 1

    elif opcion.upper() == 'N':

        break

    else:

        print('Opcion incorrecta!!!!!')

if suma != 0 and cantidad != 0:

    promedio = suma / cantidad
    print('La suma de los números es:', suma)
    print('El promedio es:', promedio)
else:
    print('Error. No se ha ingresado ningún número.')