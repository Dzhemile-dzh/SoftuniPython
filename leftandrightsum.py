num = int(input())
scores = []
scores2 = []
for i in range(0, num):
    scores.append(int(input()))
x = sum(scores)
for i in range(num, num*2):
    scores2.append(int(input()))
y = sum(scores2)
if x == y:
    print(f'Yes, sum = {x}')
elif x > y:
    res = x - y
    print(f'No, diff = {res}')
else:
    res = y - x
    print(f'No, diff = {res}')