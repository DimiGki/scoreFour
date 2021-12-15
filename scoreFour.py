def printBoard(data):
  print('  1   2   3   4   5   6   7')
  print('+---+---+---+---+---+---+---+')
  for i in range(6):
    print('|   |   |   |   |   |   |   |')
    print('|', data[i][0], '|', data[i][1], '|', data[i][2], '|', data[i][3], '|', data[i][4], '|', data[i][5], '|', data[i][6], '|')
    print('|   |   |   |   |   |   |   |')
    print('+---+---+---+---+---+---+---+')

def dropPiece(data, name, piece):
    print('Your turn ', name)
    column = input('Select column: ')
    # Check for correct input
    while (not column.isnumeric() or int(column) < 1 or int(column) > 7 or data[0][int(column) - 1] != ' '):
        print('Please choose a correct number')
        column = input('Select column: ')
    
    column = int(column)

    for i in range(5, -1, -1):
      if (data[i][column - 1] == ' '):
        data[i][column - 1] = piece
        break

def checkWin(data):
    # Check the rows
    for row in range(0, 6):
        for i in range(0, 4):
            if (data[row][i] != ' '):
                if (data[row][i] == data[row][i + 1] == data[row][i + 2] == data[row][i + 3]):
                    return True
    # Check the columns
    for column in range(0, 7):            
        for row in range(0, 3):
            for i in range(0, 4):
                if (data[row][column] != ' '):
                    if (data[row][column] == data[row + 1][column] == data[row + 2][column] == data[row + 3][column]):
                        return True
    # Check diagonal forward
    for row in range(0, 3):
        for i in range(0, 4):
            if (data[row][i] != ' '):
                if (data[row][i] == data[row + 1][i + 1] == data[row + 2][i + 2] == data[row + 3][i + 3]):
                    return True
    # Check diagonial backward
    for row in range(0, 3):
        for col in range(6, 2, -1):
            if (data[row][i] != ' '):
                if(data[row][col] == data[row+1][col-1] == data[row+2][col-2] == data[row+3][col-3]):
                    return True

data = [
[' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ']]

pl1 = ['Pl1', 'x']
pl2 = ['Pl2', 'o']
hasWon = False

printBoard(data)

for turn in range(21):
    player = pl1
    dropPiece(data, player[0], player[1])
    printBoard(data)
    hasWon = checkWin(data)
    if (hasWon):
        print(player[0], 'wins!')
        break
    
    player = pl2
    dropPiece(data, player[0], player[1])
    printBoard(data)
    hasWon = checkWin(data)
    if (hasWon):
        print(player[0], 'wins!')
        break

    if (turn == 20):
        print('Game Over! Draw!')
