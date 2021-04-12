n = int(input('Cantidad de palabras: '))

lista_de_palabras = []
contador_palabras = 1

for x in range(n):

    palabra = input(f'Palabra {contador_palabras}: ')

    lista_de_palabras.append(palabra)

    contador_palabras += 1

#clasificador = sorted(lista_de_palabras, key=len)

palabra_mas_larga = max(lista_de_palabras, key=len)
palabra_mas_corta = min(lista_de_palabras, key=len)

print('La palabra mas larga es', palabra_mas_larga)
print('La palabra mas corta es', palabra_mas_corta)