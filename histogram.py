count_numbers = int(input())
p1 = 0.0
p2 = 0.0
p3 = 0.0
p4 = 0.0
p5 = 0.0
if 1 <= count_numbers <= 1000:
    for numbers in range(count_numbers):
        number = int(input())
        if number < 200:
            p1 += 1
        elif 200 <= number <= 399:
            p2 += 1
        elif 400 <= number <= 599:
            p3 += 1
        elif 600 <= number <= 799:
            p4 += 1
        elif number >= 800:
            p5 += 1
    print(f'{(p1/count_numbers * 100):.2f}%')
    print(f'{(p2/count_numbers * 100):.2f}%')
    print(f'{(p3/count_numbers * 100):.2f}%')
    print(f'{(p4/count_numbers * 100):.2f}%')
    print(f'{(p5/count_numbers * 100):.2f}%')