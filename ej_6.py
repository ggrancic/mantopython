n1 = int(input('Ingrese un número: '))
n2 = int(input('Ingrese otro número: '))

if len(str(n1)) > 2 or len(str(n1)) < 2:
    print("Longitud del número 1 incorrecta. Debe ser de dos dígitos.")
elif len(str(n2)) > 2 or len(str(n2)) > 2:
    print("Longitud del número 2 incorrecta. Debe ser de dos dígitos.")
else:
    producto = n1 * n2
    cociente = n1 / n2
    resto = n1 % n2
    print("Producto = ", producto)
    print("Cociente = ", cociente)
    print("Resto = ", resto)