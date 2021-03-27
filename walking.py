walking_counter = 0
home_counter = 0
result = 0
home_result = 0 
while walking_counter < 10000:
    walking = input()
    if walking == 'Going home':
        home_walking = int(input())
        home_counter += 1
        break
    walking_counter += int(walking)
if home_counter == 0:
    result = abs(10000 - walking_counter)
    print('Goal reached! Good job!')
    print(f'{result} steps over the goal!')
else:
    home_result = walking_counter + home_walking
    if home_result < 10000:
        result = 10000 - home_result
        print(f'{result} more steps to reach goal.')
    else:
        result = abs(home_result - 10000)
        print('Goal reached! Good job!')
        print(f'{result} steps over the goal!')