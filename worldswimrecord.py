import math
record_sec = float(input())
distance = float(input())
time = float(input())
swimming = distance * time
delay = math.floor(distance / 15) * 12.5
sum_swim = swimming + delay
if record_sec <= sum_swim:
    result = sum_swim - record_sec
    print(f'No, he failed! He was {result:.2f} seconds slower.')
else:
    result = sum_swim
    print(f'Yes, he succeeded! The new world record is {result:.2f} seconds.')