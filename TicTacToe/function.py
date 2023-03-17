# from gen_var import *

# only playing on 3 X 3 board
GAME_BOARD = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
# the first 3 items  represent rows 1 - 3 in the board  ,  the next 3  1 - 3 columns
# the 7 position is for diagonal left to right and 8 pos for the diagonal right to left
VICTORY_X = [0, 0, 0, 0, 0, 0, 0, 0]
VICTORY_O = [0, 0, 0, 0, 0, 0, 0, 0]
PLAYER1 = 'X'
PLAYER2 = 'O'
SIZE = ['0', '1', '2']
COMPUTER = 'C'
HUMAN = 'H'


LOGO = """
******* TIC   TAC   TOE *******
        |  _  |  _  |  _  |
        |  _  |  _  |  _  |
        |  _  |  _  |  _  |
*******************************        
"""


def reset_board():
    global VICTORY_X
    global VICTORY_O
    global GAME_BOARD

    for i in range(0, 8):
        VICTORY_X[i] = 0
        VICTORY_O[i] = 0

    for i in range(0, 3):
        for j in range(0, 3):
            GAME_BOARD[i][j] = '_'


def computer_play():
    global VICTORY_X
    global VICTORY_O
    global GAME_BOARD
    empty = '_'
    total_sq = 0
    row1 = -1
    col1 = -1
    board_s = len(GAME_BOARD)
    for x in VICTORY_X:
        total_sq += x
    for x in VICTORY_O:
        total_sq += x
    if GAME_BOARD[1][1] == empty and total_sq <= 1:
        row1 = 1
        col1 = 1
    elif col1 == -1 or row1 == -1:
        for i in range(0, 3):
            if VICTORY_X[i] == 2 or VICTORY_O[i] == 2:
                for j in range(0, 3):
                    if GAME_BOARD[i][j] == empty:
                        col1 = j
                        row1 = i
        if VICTORY_X[6] == 2 or VICTORY_O[6] == 2:
            for i in range(0, 3):
                if GAME_BOARD[i][i] == empty:
                    row1 = i
                    col1 = i
        if VICTORY_X[7] == 2 or VICTORY_O[7] == 2:
            j = board_s - 1
            for i in range(0, board_s):
                if GAME_BOARD[j][i] == empty:
                    row1 = i
                    col1 = j
                j -= 1
    if col1 == -1 or row1 == -1:
        for i in range(0, 3):
            for j in range(0, 3):
                if GAME_BOARD[i][j] == empty:
                    col1 = j
                    row1 = i
    return row1, col1


def check_board(ply1):
    global VICTORY_X
    global VICTORY_O
    global GAME_BOARD
    free = 0
    victory = [0, 0, 0, 0, 0, 0, 0, 0]
    b_size = len(GAME_BOARD)
    for i in range(0, b_size):
        victory[i] = GAME_BOARD[i].count(ply1)
        free += GAME_BOARD[i].count('_')
        if GAME_BOARD[i][i] == ply1:
            victory[6] += 1
        for j in range(0, b_size):
            if GAME_BOARD[i][j] == ply1:
                victory[j+3] += 1
    j = b_size - 1
    for i in range(0, b_size):
        if GAME_BOARD[j][i] == ply1:
            victory[7] += 1
        j -= 1
    if ply1 == PLAYER1:
        VICTORY_X = victory
    else:
        VICTORY_O = victory
    print(f'player{ply1} victory = {VICTORY_X}') if ply1 == PLAYER1 else print(f'player{ply1} victory = {VICTORY_O}')
    print(f'free = {free}')
    if VICTORY_X.count(b_size) > 0:
        return PLAYER1
    elif VICTORY_O.count(b_size) > 0:
        return PLAYER2
    elif free == 0:
        return 'D'
    return 0


def print_bord():
    global GAME_BOARD
    for i in range(0, len(GAME_BOARD)):
        print(f'|  {GAME_BOARD[i][0]}  |  {GAME_BOARD[i][1]}  |  {GAME_BOARD[i][2]}  |\n')


# FUNC for input from player for row and col
def play_move(plyer, opponent):
    global GAME_BOARD
    legal = False
    if opponent == COMPUTER and plyer == PLAYER1:
        row, col = computer_play()
    else:
        while not legal:
            row = input(f'select row number  0-2 : ')
            col = input(f'select col number  0-2 : ')
            if row.isnumeric() and col.isnumeric() and row in SIZE and col in SIZE:
                if GAME_BOARD[int(row)][int(col)] == '_':
                    legal = True
                else:
                    print(f'select an empty place')
            else:
                print(f'enter only numbers ({SIZE})')
                legal = False
    GAME_BOARD[int(row)][int(col)] = plyer
    return check_board(plyer)
