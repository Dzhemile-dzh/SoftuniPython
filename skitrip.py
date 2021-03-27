day_stays = int(input())
room = input()
rating = input()
night_stays = day_stays - 1
discount = 0
if room == 'room for one person':
    discount = 0
    sum_days = 18.00*night_stays
elif room == 'apartment':
    if day_stays < 10:
        discount = 30/100
    elif 10 < day_stays < 15:
        discount = 35/100
    elif day_stays > 15:
        discount = 50/100
    sum_days = 25.00 * night_stays
elif room == 'president apartment':
    if day_stays < 10:
        discount = 10/100
    elif 10 < day_stays < 15:
        discount = 15/100
    elif day_stays > 15:
        discount = 20/100
    sum_days = 35.00 * night_stays
price = sum_days - sum_days*discount
if rating == 'positive':
    result = price + price*25/100
elif rating == 'negative':
    result = price - price*10/100
print(f'{result:.2f}')