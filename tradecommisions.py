grad = input()
prodajbi = float(input())
if prodajbi >= 0:
    if grad == 'Sofia':
        if 0 <= prodajbi <= 500:
            res = 5/100*prodajbi
        elif 500 <= prodajbi <= 1000:
            res = 7/100*prodajbi
        elif 1000 < prodajbi <= 10000:
            res = 8/100*prodajbi
        elif prodajbi > 10000:
            res = 12/100*prodajbi
        else:
            print('error')
        print(f'{res:.2f}')
    elif grad == 'Varna':
        if 0 <= prodajbi <= 500:
            res = 4.5/100*prodajbi
        elif 500 <= prodajbi <= 1000:
            res = 7.5/100*prodajbi
        elif 1000 < prodajbi <= 10000:
            res = 10/100*prodajbi
        elif prodajbi > 10000:
            res = 13/100*prodajbi
        else:
            print('error')
        print(f'{res:.2f}')
    elif grad == 'Plovdiv':
        if 0 <= prodajbi <= 500:
            res = 5.5/100*prodajbi
        elif 500 <= prodajbi <= 1000:
            res = 8/100*prodajbi
        elif 1000 < prodajbi <= 10000:
            res = 12/100*prodajbi
        elif prodajbi > 10000:
            res = 14.5/100*prodajbi
        else:
            print('error')
        print(f'{res:.2f}')
    else:
        print('error')
else:
    print('error')