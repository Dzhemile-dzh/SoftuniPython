film = float(input())
statist = int(input())
cena_obleklo = float(input())
sum_dekor = film*10/100
sum_obleklo = statist * cena_obleklo
if statist > 150:
    otstupka = sum_obleklo*10/100
    sum_otstupka = sum_obleklo - otstupka
    sum_film = sum_dekor + sum_otstupka
elif statist < 150:
    sum_film = sum_dekor + sum_obleklo
if sum_film <= film:
    result = film - sum_film
    print('Action!')
    print(f'Wingard starts filming with {result:.2f} leva left.')
elif sum_film >= film:
    result = sum_film - film
    print('Not enough money!')
    print(f'Wingard needs {result:.2f} leva more.')