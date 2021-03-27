cakeSide1 = int(input())
cakeSide2 = int(input())
cakeSize = cakeSide1 * cakeSide2
totalPieces = 0
command = input()
while command != 'STOP':
    piecesCounter = int(command)
    totalPieces += piecesCounter
    if totalPieces > cakeSize:
        break
    command = input()
if totalPieces > cakeSize:
    print(f'No more cake left! You need {totalPieces - cakeSize} pieces more.')
if command == 'STOP' or cakeSize > totalPieces:
    print(f'{cakeSize - totalPieces} pieces are left.')