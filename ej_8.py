a = int("Ingrese el valor del coeficiente a: ")
b = int("Ingrese el valor del coeficiente b: ")
c = int("Ingrese el valor del coeficiente c: ")
d = int("Ingrese el valor del coeficiente d: ")
e = int("Ingrese el valor del coeficiente e: ")
f = int("Ingrese el valor del coeficiente f: ")

x = ((c * e) - (b * f)) / ((a * e) - (b * d))

y = ((a * f) - (c * d)) / ((a * e) - (b * d))

print("El valor de x es: ", x)
print("El valor de y es: ", y)