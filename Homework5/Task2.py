# Создайте программу для игры в ""Крестики-нолики"".

# list = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]


board = list(range(1,10))

def design_board(board):
    print()
    for i in range(3):
        print('|', board[0+i*3],'|', board[1+i*3], '|', board[2+i*3], '|')

def choice(symbol):
    flag = False
    while not flag:
        player = int(input( '\n''Ваш ход, выберите номер ячейки ' + symbol + ' --> ' ))
        board[player-1] = symbol
        flag = True

def victory_check(board):
    victory = ((0,1,2),(3,4,5),(6,7,8),
               (0,3,6),(1,4,7),(2,5,8),
               (0,4,8),(2,4,6))
    for i in victory:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False

design_board(board)
counter=0
victory = False
while not victory:
    if counter % 2 == 0:
         choice('X')
    else:
        choice('0')
    counter +=1
    if counter > 4:
        win = victory_check(board)
        if win:
            print(win,'Победа')
            victory = True
            break
        if counter == 9:
            print('Ничья')
    design_board(board)
