import random
from colorama import Fore

options = ('piedra', 'papel', 'tijera')

pc_win = 0
user_win = 0

rondas = 1
while True:

    print('*' * 50)
    print(f'Ronda {rondas}')
    print('*' * 50)
    print(f'Puntos User {user_win}')
    print(f'Puntos Pc {pc_win}')


    user = input('Piedra, Papel o Tijera => ').lower()
    pc = random.choice(options)

    # if not user in options:
    # print('Invalid')

    print('User options:', user.capitalize())
    print('Pc options:', pc.capitalize())

    color_verde = Fore.GREEN
    color_amarillo = Fore.YELLOW
    color_rojo = Fore.RED

    if user == pc:
        print(color_amarillo + 'Empate')
        print('\n')
    elif user == 'piedra':
        if pc == 'tijera':
            print('Piedra gana a Tijera')
            print(color_verde + 'Ganaste!')
            user_win += 1
            print('\n')
        else:
            print('Papel gana a Piedra')
            print(color_amarillo + 'Perdiste')
            pc_win += 1
            print('\n')
    elif user == 'papel':
        if pc == 'piedra':
            print('Papel gana a Piedra')
            print(color_verde + 'Ganaste!')
            user_win += 1
            print('\n')
        else:
            print('Tijera gana a Papel')
            print(color_amarillo + 'Perdiste')
            pc_win += 1
            print('\n')
    elif user == 'tijera':
        if pc == 'papel':
            print('Tijera gana a Papel')
            print(color_verde + 'Ganaste!')
            user_win += 1
            print('\n')
        else:
            print('Piedra gana a Tijera')
            print(color_amarillo + 'Perdiste!')
            pc_win += 1
            print('\n')
    else:
        print(color_rojo + 'Opcion invalida')
        print('\n')

    if pc_win == 3:
        print('Gano PC')
        break
    if user_win == 3:
        print('Gano User')
        break

    rondas += 1

print('Fin')