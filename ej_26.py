anio = int(input('Ingrese un agno: '))

if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
     print(f'{anio} es bisiesto')
else:
    print(f'{anio} no es bisiesto')