"""
Escriba un programa que reciba como entrada dos números, y los muestre ordenados de menor a
mayor:
    Ingrese numero: 51
    Ingrese numero: 24
    24 51
"""

#n1 = int(input('Ingrese un número: '))
#n2 = int(input('Ingrese otro un número: '))

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
cantidad = int(input('Ingrese la cantidad de numeros que desea ordenar: '))
for x in range(cantidad):
    num = int(input('Ingrese un número: '))
    lista.append(num)

# Pregunto si quiero orden ascendente o descendente.
opcion = input('Desea orden ascendente (A) u orden descendente (D): ')
if opcion == 'D':

    # Acá lo que hago es separar por comas cada valor de la lista, pero con map lo presento como string a cada valor de la lista
    # dentro del map, le paso que me conviera a string cada valor con str y le paso la lista pero ya acomodada gracias
    # al metodo sorted.
    print (', '.join(map(str, sorted(lista, reverse=True))))

elif opcion == 'A':
    # hago lo mismo que en el anterior if, pero esta vez sin el reverse=True. osea que me devuelve en orden ascendente.
    print (', '.join(map(str, sorted(lista))))
else:
    print('Opción incorrecta!!!!')
