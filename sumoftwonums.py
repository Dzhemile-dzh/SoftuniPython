start = int(input())
end = int(input())
magic = int(input())
count = 0
isFound = False
for first in range(start, end + 1):
    for sec in range(start, end + 1):
        sum = first + sec
        count += 1
        if sum == magic:
            print(f'Combination N:{count} ({first} + {sec} = {sum})')
            isFound = True
            break
    if isFound:
        break
if not isFound:
    print(f'{count} combinations - neither equals {magic}')