puzzle = 2.6
doll = 3
bear = 4.1
minion = 8.2
truck = 2
 
vacation_price = float(input())
puzzle_count = int(input())
doll_count = int(input())
bear_count = int(input())
minion_count = int(input())
truck_count = int(input())
 
toys_sum = puzzle * puzzle_count + doll * doll_count + bear * bear_count + minion * minion_count + truck * truck_count
 
 
if puzzle_count + doll_count + bear_count + minion_count + truck_count >= 50:
    disc = toys_sum * 0.25
    rent = (toys_sum - disc) * 0.1
    earnings = toys_sum - disc - rent
else:
    rent = toys_sum * 0.1
    earnings = toys_sum - rent
if vacation_price <= earnings:
    print(f"Yes!{abs(earnings - vacation_price): .2f} lv left.")
else:
    print(f"Not enough money!{abs(earnings - vacation_price): .2f} lv needed.")