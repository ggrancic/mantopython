#Escriba un programa que simule una calculadora básica, este puede realizar operación de
#suma, resta, multiplicación y división. El programa debe recibir como entrada 2 números reales y un operador, que puede ser +, -, * o /.

operando1 = int(input('Ingrese un operando: '))
operador = input('Ingrese un operador: ')
operando2 = int(input('Ingrese otro operador: '))

if operador == '+':
    resultado = operando1 + operando2
elif operador == '-':
    resultado = operando1 - operando2
elif operador == '*':
    resultado = operando1 * operando2
elif operador == '/':
    resultado = operando1 / operando2
else:
    resultado = 'Error'

if resultado == 'Error':
    print('Error en el operando.')
else:
    print(operando1, operador, operando2, '=',resultado)