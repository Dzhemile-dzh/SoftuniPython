plant_type = input()
plant_count = int(input())
budget = int(input())
price = 0.0
discount = 0.0
if plant_type == 'Roses':
    price = 5 * plant_count
    if plant_count > 80:
        discount = 10/100
    sum_plants = price - (price * discount)
elif plant_type == 'Dahlias':
    price = 3.80 * plant_count
    if plant_count > 90:
        discount = 15/100
    sum_plants = price - (price * discount)
elif plant_type == 'Tulips':
    price = 2.80 * plant_count
    if plant_count > 80:
        discount = 15 / 100
    sum_plants = price - (price * discount)
elif plant_type == 'Narcissus':
    price = 3.00 * plant_count
    if plant_count < 120:
        discount = 15 / 100
    sum_plants = price + (price * discount)
elif plant_type == 'Gladiolus':
    price = 2.50 * plant_count
    if plant_count < 80:
        discount = 20 / 100
    sum_plants = price + (price * discount)

if sum_plants > budget:
    result = sum_plants - budget
    print(f'Not enough money, you need {result:.2f} leva more.')
else:
    result = budget - sum_plants
    print(f'Hey, you have a great garden with {plant_count} {plant_type} and {result:.2f} leva left.'