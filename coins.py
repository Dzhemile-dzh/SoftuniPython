coins = 0
money = float(input())
while money > 0:
    coins += 1
    if money >= 2:
        money -= 2
    elif money >= 1:
        money -= 1
    elif money >= 0.5:
        money -= 0.5
        money = round(money, 2)
    elif money >= 0.2:
        money -= 0.2
        money = round(money, 2)
    elif money >= 0.1:
        money -= 0.1
        money = round(money, 2)
    elif money >= 0.05:
        money -= 0.05
        money = round(money, 2)
    elif money >= 0.02:
        money -= 0.02
        money = round(money, 2)
    elif money != 0:
        money = 0
        break
print(coins)