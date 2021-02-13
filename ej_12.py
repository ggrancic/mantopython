mes = int(input('Ingrese un mes: '))
meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

if mes == 0 or mes > 12:
    print("Valor incorrecto")
else:
    print(meses[mes-1])