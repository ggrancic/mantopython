n = int(input('Ingrese n: '))

lista_de_numeros = []
for x in range(n):
    num = int(input('Ingrese numero: '))
    lista_de_numeros.append(num)

print('El mayor es:', max(lista_de_numeros))