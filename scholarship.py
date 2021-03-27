import math
income = float(input())
avg_result = float(input())
min_salary = float(input())
excellent_result = avg_result * 25
social = 35/100 * min_salary
if income > min_salary:
    if avg_result < 5.50:
        print('You cannot get a scholarship!')
    elif avg_result >= 5.50:
        print(f'You get a scholarship for excellent results {math.floor(excellent_result)} BGN')
elif income <= min_salary:
    if 4.50 <= avg_result < 5.50:
        print(f'You get a Social scholarship {math.floor(social)} BGN')
    elif avg_result >= 5.50:
        if social > excellent_result:
            print(f'You get a Social scholarship {math.floor(social)} BGN')
        else:
            print(f'You get a scholarship for excellent results {math.floor(excellent_result)} BGN')
    else:
        print('You cannot get a scholarship!')