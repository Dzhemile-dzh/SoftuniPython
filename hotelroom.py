mounth = input()
nights = int(input())
studio = 0
apartment = 0
discount_studio = 0
discount_apartment = 0
if mounth == 'May' or mounth == 'October':
    studio = 50*nights
    apartment = 65*nights
    if 7 < nights < 14:
        discount_studio = 5/100
    elif nights > 14:
        discount_studio = 30/100
        discount_apartment = 10/100
elif mounth == 'June' or mounth == 'September':
    studio = 75.20*nights
    apartment = 68.70*nights
    if nights > 14:
        discount_studio = 20/100
        discount_apartment = 10/100
elif mounth == 'July' or mounth == 'August':
    studio = 76*nights
    apartment = 77*nights
    if nights > 14:
        discount_apartment = 10/100
result_apartment = apartment - (apartment*discount_apartment)
result_studio = studio - (studio * discount_studio)
print(f'Apartment: {result_apartment:.2f} lv.')
print(f'Studio: {result_studio:.2f} lv.')