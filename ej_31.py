# Escriba un programa que entregue la edad del usuario a partir de su fecha de nacimiento:

from time import localtime

print('Ingresa tu fecha de nacimiento: ')
dia = int(input('Dia: '))
mes = int(input('Mes: '))
agno = int(input('Año: '))

# Fecha actual es posterior al cumpleaños o es el mismo día.
if localtime().tm_mon > mes or localtime().tm_mon == mes:
    edad =  localtime().tm_year - agno

# Fecha actual es anterior al cumpleaños. Osea, no cumplió todavía.
else:
    edad =  (localtime().tm_year - agno) - 1

print(f'Usted tiene {edad} años.')