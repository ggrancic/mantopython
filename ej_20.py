# Hacer un algoritmo que pida 10 números y luego indique cuantos fueron pares y cuantos impares.

c_par = 0
c_impar = 0

for x in range(10):

    numero = int(input('Ingresa un numero: '))

    if numero % 2 == 0:

        c_par += 1
    
    else:

        c_impar += 1

print('La cantidad de números pares es:', c_par)
print('La cantidad de números impares es:', c_impar)