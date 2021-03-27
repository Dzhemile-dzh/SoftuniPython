book = input()
count = 0
while book != 'No More Books':
    book_search = input()
    count += 1
    if book_search == book:
        print(f'You checked {count-1} books and found it.')
        break
    if book_search == 'No More Books':
        print(f'The book you search is not here!')
        print(f'You checked {count-1} books.')
        break