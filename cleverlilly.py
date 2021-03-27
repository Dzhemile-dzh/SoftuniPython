years = int(input())
washing_machine = float(input())
toy_price = int(input())
even = 0
odd = 0
sum_even = 0
sibling = 0
for year in range(1, years + 1):
    if year % 2 == 0:
        even += 10
        sum_even += even
        sibling += 1
    else:
        odd += 1
odd_toy = odd * toy_price
summary = sum_even + odd_toy - sibling
if summary >= washing_machine:
    result = summary - washing_machine
    print(f'Yes! {result:.2f}')
else:
    result = washing_machine - summary
    print(f'No! {result:.2f}')