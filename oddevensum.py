num = int(input())
odd_sum = 0
even_sum = 0
for i in range(1, num+1):
    element = int(input())
    if i % 2 == 0:
        even_sum += element
    else:
        odd_sum += element
if even_sum == odd_sum:
    print(f'Yes')
    print(f'Sum = {even_sum}')
else:
    print(f'No')
    print(f'Diff = {abs(even_sum - odd_sum)}')