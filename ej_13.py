notas = 0
for x in range(4):
    nota = int(input('Ingresa una nota: '))
    notas += nota
media = notas // 4
if media in range(0, 59):
    print('Puntuación: E')
elif media in range(60, 69):
    print('Puntuación: D')
elif media in range(70, 79):
    print('Puntuación: C')
elif media in range(80, 89):
    print('Puntuación: B')
elif media in range(90, 100):
    print('Puntuación: A')
else:
    print("Error")