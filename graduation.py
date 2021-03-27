name = input()
sum_grades = 0.0
excluded = 0
count = 1
notPassed = 0
while count <= 12:
    grade = float(input())
    if grade < 4.00:
        notPassed += 1
        if notPassed == 2:
            print(f'{name} has been excluded at {count-1} grade')
            break
        count += 1
    elif grade >= 4.00:
        count += 1
        sum_grades += grade
        notPassed = 0
if notPassed == 0:
    average = sum_grades/12
    print(f'{name} graduated. Average grade: {average:.2f}')