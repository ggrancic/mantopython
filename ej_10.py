anchura = 11
altura = 5
txt = 'CINCO'
spc = ' ' #Espacio

for i in range(altura):
    if i == 0 or i == altura-1:
        print('*' * anchura)

    elif i == 2:
        print('*' + spc * 2 + txt + spc * 2 + '*')

    else:
        print('*' + spc * (anchura-2) + '*')