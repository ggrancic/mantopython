"""18. Hacer un algoritmo que haga lo siguiente:
Pida dos números al usuario, y que los multiplique. Si la multiplicación da un valor menor a 150, se
volverán a pedir los números hasta que la multiplicación de ambos tengan una respuesta mayor a 150.
Mostrar la respuesta en cada intento."""


producto = 0.0 # Se inicializa la variable como float.

# Mientras el producto sea menor o igual al valor 150, se volverá a pedir que se ingresen los valores.
while producto <= 150:
    a = float(input('Ingrese el primer número: '))
    b = float(input('Ingrese el segundo número: '))

    producto = a * b

    print('El producto es ', producto)

    # Mostrar mensaje de error si no se supera el valor 150.
    if producto <= 150:
        print('Ingrese nuevamente dos valores...\n')
    else:
        print('Correcto')