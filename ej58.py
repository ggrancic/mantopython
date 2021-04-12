# En este ejercicio se han dividio los incisos en sus correspondientes funciones.
# Para realizar el testing puede llamarlas.

import math

# 1 - Función para devolver el n-esimo numero de fibonacci.
def fib_ult(n):
   if n <= 1:
       return n
   else:
       return (fib_ult(n-1) + fib_ult(n-2))

# 2 - Función para verificar si es un número de fibonacci.
def fibonacci_ver(n):
    phi = 0.5 + 0.5 * math.sqrt(5.0)
    a = phi * n
    if n == 0 or abs(round(a) - a) < 1.0 / n:
        return 'Es un numero de Fibonacci'
    else:
        return 'No es un numero de Fibonacci'

# 3 - Funcion para imprimir la secuencia de fibonacci correspondiente.
def suc_fib(n): 
    a, b = 0, 1
    for x in range(0, n):
        print(a, end=' ')
        a,b = b, a + b

n = int(input('Ingrese n: '))

# Llamando funciones. Comente la que no quiera ejecutar.

print(f'F{n} =', fib_ult(n))
print(f'{n}', fibonacci_ver(n))

# En este ultimo caso, no se coloca print de antemano porque la funcion misma imprime por pantalla la secuencia, de manera que se eliminan
# los saltos de linea para que el output quede presentado como en el enunciado...
suc_fib(n)