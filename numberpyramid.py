num = int(input())
counter = 1
all_is_printed = False
for row in range(1, num + 1):
    for col in range(1, row + 1):
        print(f'{counter}', end=' ')
        counter += 1
        if counter > num:
            all_is_printed = True
            break
    if all_is_printed:
        break
    print()