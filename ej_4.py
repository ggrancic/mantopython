"""
Escribir un programa que solicite al usuario la longitud y anchura de un rectángulo y a continuación
visualice su superficie con cuatro decimales
"""

altura = float(input('Ingrese la altura: '))
anchura = float(input('Ingrese la anchura: '))

superficie = anchura * altura

print("La superficie es: ", round(superficie, 4))