"""
Escriba un programa que pida al usuario dos palabras, y que indique cuál de ellas es la más larga y por
cuántas letras lo es.
"""

p1 = input('Ingresa la palabra: ')
p2 = input('Ingresa la otra palabra: ')

# Primero debería ver si tienen la misma longitud.
if len(p1) == len(p2):
    print('Tienen la misma longitud')
else:
    # Acá voy a usar max() para ver cual es mas grande.
    print('La palabra más larga es:',max(len(p1), len(p2)))