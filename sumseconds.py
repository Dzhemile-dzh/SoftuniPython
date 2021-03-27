import math
 
first_runner = int ( input () )
second_runner = int ( input () )
third_runner = int ( input () )
 
sum_time = first_runner + second_runner + third_runner
minutes = sum_time / 60
seconds = sum_time % 60
minutes = math.floor(minutes)
 
if seconds < 10:
    print ( f'{minutes}:0{seconds:.0f}' )
else:
    print ( f'{minutes}:{seconds:.0f}' )