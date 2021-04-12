estatura = float(input('Ingrese la estatura: '))
peso = float(input('Ingrese el peso: '))
edad = int(input('Ingrese su edad: '))


imc_calc = peso / (estatura ** 2)

if edad < 45 and imc_calc < 22:
    print('Condición de riesgo: BAJO')
elif edad >= 45 and imc_calc >= 22:
    print('Condición de riesgo: ALTO')
else:
    print('Condición de riesgo: MEDIO')