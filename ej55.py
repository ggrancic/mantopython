def palindromo_checker(palabra):
    """
    Retornamos true o false si la palabra es igual (o no)
    al string slice reverso.
    """
    return palabra == palabra[::-1]

def palindromo_espacios(palabra):
    """
    Primero convertimos todo a lower para evitar el problema
    de que si se ingresan mayusculas o minusculas combinadas.
    luego eliminamos los espacios con el metodo replace()
    finalmente hacemos lo mismo que la funcion anterior
    """
    palabra_minus = palabra.lower()
    palabra_s_esp = palabra_minus.replace(" ", "")
    return palabra_s_esp == palabra_s_esp[::-1]


palabra = input('Ingrese una palabra: ')

if palindromo_espacios(palabra):
    print('Es palindromo')
else:
    print('No es palindromo')
