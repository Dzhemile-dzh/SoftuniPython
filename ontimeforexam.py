import math
hour_exam = int(input())
minute_exam = int(input())
hour_arrival = int(input())
minute_arrival = int(input())
res_minute = 0
res_hour = 0
time = ''
min = (hour_exam - hour_arrival)*60 + minute_exam-minute_arrival
if min < 0:
    positive_time = -min
    time = 'Late'
    if positive_time >= 60:
        hour_late = positive_time / 60
        min_late = positive_time % 60
        print(f'{time}')
        if min_late < 10:
            print(f'{math.floor(hour_late)}:0{min_late} hours after the start')
        print(f'{math.floor(hour_late)}:{min_late} hours after the start')
    else:
        print(f'{time}')
        print(f'{positive_time} minutes after the start')
elif min == 0 or min <= 30:
    time = 'On time'
    if min == 0:
        print(f'{time}')
    else:
        print(f'{time}')
        print(f'{min} minutes before the start')
elif min > 30:
    time = 'Early'
    if min >= 60:
        hour_early = min / 60
        min_early = min % 60
        print(f'{time}')
        if 10 > min_early > 0:
            print(f'{math.floor(hour_early)}:0{min_early} hours before the start')
        elif hour_early >= 1 and min_early == 0:
            print(f'{math.floor(hour_early)}:00 hours before the start')
        else:
            print(f'{math.floor(hour_early)}:{min_early} hours before the start')
    else:
        print(f'{time}')
        print(f'{min} minutes before the start')