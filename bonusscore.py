number = int(input())
if number <= 100:
    bonus = 5
elif number > 100 and number < 1000:
    bonus = number*20/100
elif number > 1000:
    bonus = number*10/100

if number % 2 == 0:
    bonusB = 1
elif number % 10 == 5:
    bonusB = 2
else:
    bonusB = 0
sum_bonus = bonus + bonusB
sum = sum_bonus + number
print(sum_bonus)
print(sum)