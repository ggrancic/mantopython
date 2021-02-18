"""
Escriba un programa que reciba como entrada dos números, y los muestre ordenados de menor a
mayor:
    Ingrese numero: 51
    Ingrese numero: 24
    24 51
"""

n1 = int(input('Ingrese un número: '))
n2 = int(input('Ingrese otro un número: '))

"""
# Trabajando con condicionales
if n1 > n2:
    print(n1, n2)
elif n2 > n1:
    print(n2, n1)
else:
    print('Son iguales.')
"""

# Trabajando con listas.
lista = []
numeros = " "
for x in range(2):
    num = int(input('Ingrese un número: '))
    lista.append(num)

print(sorted(lista, reverse=True))
