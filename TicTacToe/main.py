# class Bord:
#     def __init__(self, bord, size):
#         self.bord = bord
#         self.size = size
import time

# only playing on 3 X 3 board
EMPTY_BOARD = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

# the first 3 items  represent rows 1 - 3 in the board  ,  the next 3  1 - 3 columns
# the 7 position is for diagonal left to right and 8 pos for the diagonal right to left
VICTORY_X = [0, 0, 0, 0, 0, 0, 0, 0]
VICTORY_O = [0, 0, 0, 0, 0, 0, 0, 0]
PLAYER1 = 'X'
PLAYER2 = 'O'
SIZE = ['0', '1', '2']

LOGO = """
******* TIC   TAC   TOE *******

        |  _  |  _  |  _  |

        |  _  |  _  |  _  |

        |  _  |  _  |  _  |
        
*******************************        
"""


def check_board(board, playr):
    global VICTORY_X
    global VICTORY_O
    full = 0
    victory = [0, 0, 0, 0, 0, 0, 0, 0]
    b_size = len(board)
    for i in range(0, b_size):
        victory[i] = board[i].count(playr)
        full += board[i].count('_')
        if board[i][i] == playr:
            victory[6] += 1
        for j in range(0, b_size):
            if board[i][j] == playr:
                victory[j+3] += 1
    j = b_size - 1
    for i in range(0, b_size):
        if board[j][i] == playr:
            victory[7] += 1
        j -= 1
    if playr == 'X':
        VICTORY_X = victory
    else:
        VICTORY_O = victory
    print(f'player{playr} victory = {VICTORY_X}') if playr == 'X' else print(f'player{playr} victory = {VICTORY_O}')
    print(f'full = {full}')
    for i in range(0, 8):
        if VICTORY_X[i] >= b_size:
            return 'X'
        if VICTORY_O[i] >= b_size:
            return 'O'
    if full == 0:
        return 'D'
    return 0


def print_bord(bord):
    for i in range(0, len(bord)):
        print(f'|  {bord[i][0]}  |  {bord[i][1]}  |  {bord[i][2]}  |\n')


# FUNC for input from player for row an col
def play_move(bord, plyer):
    legal = False
    while not legal:
        row = input(f'select row number  0-2 : ')
        col = input(f'select col number  0-2 : ')
        if row.isnumeric() and col.isnumeric() and row in SIZE and col in SIZE:
            legal = True
            bord[int(row)][int(col)] = plyer
            status = check_board(bord, plyer)
        else:
            print(f'enter only numbers ({SIZE})')
            legal = False
    return status


# ****     Main   *******  #
print(LOGO)
bord1 = EMPTY_BOARD
game_over = False
player = 'X'

while not game_over:
    print(f'player {player} your turn')
    game_status = play_move(bord1, player)
    print("\n")
    print_bord(bord1)
    if player == PLAYER1:
        player = PLAYER2
    else:
        player = PLAYER1
    if game_status in ('X', 'O'):
        print(f'\n ****** And the Winner is ********* player-{game_status}')
    if game_status == 'D':
        print(f'no more moves the board is full')
        # X = player X wins O plyer O wins and D for draw
    if game_status in ('X', 'O', 'D'):
        bord1 = EMPTY_BOARD
        # the first 3 items  represent rows 1 - 3 in the board  ,  the next 3  1 - 3 columns
        # the 7 position is for diagonal left to right and 8 pos for the diagonal right to left
        VICTORY_X = [0, 0, 0, 0, 0, 0, 0, 0]
        VICTORY_O = [0, 0, 0, 0, 0, 0, 0, 0]
        tmp1 = input('want another game press Y : ')
        if tmp1 not in ['Y', 'y']:
            game_over = True
        else:
            print(LOGO)
# end Main

