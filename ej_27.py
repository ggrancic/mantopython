"""
Escriba un programa que pida al usuario dos palabras, y que indique cuál de ellas es la más larga y por
cuántas letras lo es.
"""

p1 = input('Ingresa la palabra: ')
p2 = input('Ingresa la otra palabra: ')



# Primero debería ver si tienen la misma longitud.
if len(p1) > len(p2):
    print('La palabra ' + p1 + ' tiene mayor longitud\nTiene', len(p1) - len(p2), 'letras más que ' + p2)
elif len(p2) > len(p1):
    print('La palabra ' + p2 + ' tiene mayor longitud\nTiene', len(p2) - len(p1), 'letras más que ' + p1)
else:
    print('Son iguales.')