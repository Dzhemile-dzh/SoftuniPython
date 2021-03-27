stop = input()
total = 0
 
while stop != 'NoMoreMoney':
    installments = float(stop)
    if installments < 0:
        print('Invalid operation!')
        break
    else:
        total += installments
        print(f'Increase: {installments:.2f}')
    stop = input()
print(f'Total: {total:.2f}')