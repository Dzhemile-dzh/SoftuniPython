n = int(input())
list_num = []
for i in range(0, n):
    num = int(input())
    list_num.append(num)
list_max = max(list_num)
list_sum = sum(list_num) - list_max
if list_sum == list_max:
    print(f'Yes')
    print(f'Sum = {list_sum}')
elif list_sum < list_max:
    res = list_max - list_sum
    print(f'No')
    print(f'Diff = {res}')
else:
    res = list_sum - list_max
    print(f'No')
    print(f'Diff = {res}')