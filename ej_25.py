"""
Un alumno desea saber que nota necesita en el tercer certamen para aprobar. El promedio se calcula
con la siguiente formula.
    NC =( C 1+ C 2+ C 3)/3
    NF = NC ⋅0.7+ NL ⋅0.3
Donde N C es el promedio de parciales, NL el promedio de prácticos y N F la nota final.

Escriba un programa que pregunte al usuario las notas de los dos primeros parciales y la nota de prácticos,
y muestre la nota que necesita el alumno para aprobar la materia con nota final 60.
    Ingrese nota parcial 1: 45
    Ingrese nota parcial 2: 55
    Ingrese nota prácticos: 65
    Necesita nota 72 en el parcial 3
"""

import math

c1 = int(input('Ingrese la nota del primer parcial: '))
c2 = int(input('Ingrese la nota del segundo parcial: '))
nl = int(input('Ingrese el promedio de prácticos: '))

# Cálculo de nc

nc = (60 - (nl * 0.3)) / 0.7

# Cálculo de c3

c3 = (nc * 3) - c1 - c2

print('Necesita nota', math.trunc(c3), 'en el parcial 3')