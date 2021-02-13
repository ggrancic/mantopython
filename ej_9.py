anchura = 11
altura = 5
spc = ' ' #Espacio

for i in range(altura):
    if i == 0 or i == altura-1:
        print('*' * anchura)
    else:
        print('*' + spc * (anchura-2) + '*')