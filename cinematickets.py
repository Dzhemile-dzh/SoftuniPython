line = input()
total_tickets = 0
standard_tickets = 0
student_tickets = 0
kid_tickets = 0

while line != 'Finish':
    movie_name = line
    free_seats = int(input())

    sod_tickets_per_movie = 0
    command = input()
    while command != 'End':
        ticked_type = command
        total_tickets += 1
        sod_tickets_per_movie += 1
        
        if ticked_type == 'standard':
            standard_tickets += 1
        elif ticked_type == 'student':
            student_tickets += 1
        else:
            kid_tickets += 1
        if sod_tickets_per_movie == free_seats:
            break
        command = input()
    percent_theatre_seats = sod_tickets_per_movie/free_seats * 100
    print(f'{movie_name} - {percent_theatre_seats:.2f}% full.')
    line = input()
print(f'Total tickets: {total_tickets}')
percent_student_tickets = student_tickets/total_tickets * 100
print(f'{percent_student_tickets:.2f}% student tickets.')
percent_standard_tickets = standard_tickets/total_tickets * 100
print(f'{percent_standard_tickets:.2f}% standard tickets.')
percent_kid_tickets = kid_tickets/total_tickets * 100
print(f'{percent_kid_tickets:.2f}% kids tickets.')