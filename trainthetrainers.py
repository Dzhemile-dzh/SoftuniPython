number_of_jury = int(input())
total_grade = 0
total_presentations = 0
presentation = input()
while presentation != 'Finish':
    presentation_average_grade = 0
    for presentation_grade in range(number_of_jury):
        current_grade = float(input())
        presentation_average_grade += current_grade
        total_grade += current_grade
        total_presentations += 1
    presentation_average_grade /= number_of_jury
    print(f'{presentation} - {presentation_average_grade:.2f}.')
    presentation = input()
total_average_grade = total_grade / total_presentations
print(f"Student's final assessment is {total_average_grade:.2f}.")