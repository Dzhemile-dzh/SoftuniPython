plod = input()
den = input()
kolichestvo = float(input())
if plod == 'banana' or plod == 'apple' or plod == 'orange' or plod == 'grapefruit' or plod == 'kiwi' or plod == 'pineapple' or plod == 'grapes':
    if den == 'Monday' or den == 'Tuesday' or den == 'Wednesday' or den == 'Thursday' or den == 'Friday':
        if plod == 'banana':
            res = 2.50
        elif plod == 'apple':
            res = 1.20
        elif plod == 'orange':
            res = 0.85
        elif plod == 'grapefruit':
            res = 1.45
        elif plod == 'kiwi':
            res = 2.70
        elif plod == 'pineapple':
            res = 5.50
        elif plod == 'grapes':
            res = 3.85
        print(f'{kolichestvo * res:.2f}')
    elif den == 'Saturday' or den == 'Sunday':
        if plod == 'banana':
            res = 2.70
        elif plod == 'apple':
            res = 1.25
        elif plod == 'orange':
            res = 0.90
        elif plod == 'grapefruit':
            res = 1.60
        elif plod == 'kiwi':
            res = 3.00
        elif plod == 'pineapple':
            res = 5.60
        elif plod == 'grapes':
            res = 4.20
        print(f'{kolichestvo * res:.2f}')
    else:
        print('error')
else:
    print('error')