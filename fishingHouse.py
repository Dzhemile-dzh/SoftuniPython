budget = int(input())
season = input()
fisherman = int(input())
boat_rent = 0
if season == "Spring":
    boat_rent = 3000
    if fisherman > 12:
        boat_rent = boat_rent * 0.75
    elif 7 <= fisherman <= 11:
        boat_rent = boat_rent * 0.85
    elif fisherman <= 6:
        boat_rent = boat_rent * 0.90
    if fisherman % 2 == 0 and season != "Autumn":
        boat_rent = boat_rent * 0.95
elif season == "Summer" or season == "Autumn":
    boat_rent = 4200
    if fisherman > 12:
        boat_rent = boat_rent * 0.75
    elif 7 <= fisherman <= 11:
        boat_rent = boat_rent * 0.85
    elif fisherman <= 6:
        boat_rent = boat_rent * 0.90
    if fisherman % 2 == 0 and season != "Autumn":
        boat_rent = boat_rent * 0.95
elif season == "Winter":
    boat_rent = 2600
    if fisherman > 12:
        boat_rent = boat_rent * 0.75
    elif 7 <= fisherman <= 11:
        boat_rent = boat_rent * 0.85
    elif fisherman <= 6:
        boat_rent = boat_rent * 0.90
    if fisherman % 2 == 0 and season != "Autumn":
        boat_rent = boat_rent * 0.95
if budget >= boat_rent:
    print(f"Yes! You have {abs(budget - boat_rent):.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(budget - boat_rent):.2f} leva.")