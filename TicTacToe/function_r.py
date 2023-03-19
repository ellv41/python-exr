# from gen_var import *
import random

# GAME_BOARD = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

GAME_STATUS_VAL = [['_', '_', '_'],
                   ['_', '_', '_'],
                   ['_', '_', '_'],
                   ['_', '_', '_'],
                   ['_', '_', '_'],
                   ['_', '_', '_'],
                   ['_', '_', '_'],
                   ['_', '_', '_']]

GAME_STATUS_MAP = [[0, 1, 2],
                   [3, 4, 5],
                   [6, 7, 8],
                   [0, 3, 6],
                   [1, 4, 7],
                   [2, 5, 8],
                   [0, 4, 8],
                   [2, 4, 6]]


GAME_BOARD = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
# the first 3 items  represent rows 1 - 3 in the board  ,  the next 3  1 - 3 columns
# the 7 position is for diagonal left to right and 8 pos for the diagonal right to left
VICTORY_X = [0, 0, 0, 0, 0, 0, 0, 0]
VICTORY_O = [0, 0, 0, 0, 0, 0, 0, 0]
PLAYER1 = 'X'
PLAYER2 = 'O'
SIZE = ['0', '1', '2']
COMPUTER = 'C'
HUMAN = 'H'
FREE_SPC = '_'

LOGO = """
************* PLAY ******************
******** TIC   TAC   TOE ************  """


def grade_next_move():
    global GAME_STATUS
    me_wining = -1
    opo_wining = -1
    move = -1
    for g1 in range(0, 8):
        if GAME_STATUS_VAL[g1].count('X') == 2 and GAME_STATUS_VAL[g1].count('_') == 1:
            move = GAME_STATUS_MAP[g1][GAME_STATUS_VAL[g1].index('_')]
            return move
    for g1 in range(0, 8):
        if GAME_STATUS_VAL[g1].count('O') == 2 and GAME_STATUS_VAL[g1].count('_') == 1:
            move = GAME_STATUS_MAP[g1][GAME_STATUS_VAL[g1].index('_')]
            return move
    return move


def computer_play_rnd():
    global VICTORY_X
    global VICTORY_O
    global GAME_BOARD
    pos = -1
    empty = '_'
    empty_i = []
    board_s = len(GAME_BOARD)
    empty_spaces_sum = GAME_BOARD.count('_')
    for i in range(0, board_s):
        if GAME_BOARD[i] == empty:
            empty_i.append(i)
    # print(empty_i)
    pos = grade_next_move()
    if pos == -1:
        pos = random.choice(empty_i)
    print(f'pos {pos}')
    return pos


def check_board(ply1):
    global VICTORY_X
    global VICTORY_O
    global GAME_BOARD
    global GAME_STATUS
    victory = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 3):
        victory[i] = GAME_BOARD[i*3:i*3+3].count(ply1)
        victory[i+3] = GAME_BOARD[i::3].count(ply1)
    victory[6] = GAME_BOARD[0::4].count(ply1)
    victory[7] = GAME_BOARD[2:7:2].count(ply1)
    for id1 in range(0, 9):
        for i in range(0, 8):
            for j in range(0, 3):
                # print(f' GAME_BOARD[id1 = {GAME_BOARD[id1]}')
                if GAME_STATUS_MAP[i][j] == id1:
                    # print(f'{i}:{GAME_BOARD[id1]}')
                    GAME_STATUS_VAL[i][j] = GAME_BOARD[id1]
    print(GAME_STATUS_VAL)
    # print(f'status for {ply1} = {victory}')
    if ply1 == PLAYER1:
        VICTORY_X = victory
    else:
        VICTORY_O = victory
    if VICTORY_X.count(3) > 0:
        return PLAYER1
    elif VICTORY_O.count(3) > 0:
        return PLAYER2
    elif GAME_BOARD.count(FREE_SPC) == 0:
        return 'D'
    return 0


# FUNC for input from player for row and col
def play_move(plyer, opponent):
    global GAME_BOARD
    legal = False
    index = -1
    free_sq = GAME_BOARD.count(FREE_SPC)
    if opponent == COMPUTER and plyer == PLAYER1:
        index = computer_play_rnd()
    else:
        while not legal:
            row = input(f'select row number  0-2 : ')
            col = input(f'select col number  0-2 : ')
            if row.isnumeric() and col.isnumeric() and row in SIZE and col in SIZE:
                index = (int(row) * 3) + int(col)
                if GAME_BOARD[index] == '_':
                    legal = True
                else:
                    print(f'select an empty place')
            else:
                print(f'enter only numbers ({SIZE})')
                legal = False
    GAME_BOARD[index] = plyer
    return check_board(plyer)


def print_bord():
    global GAME_BOARD
    print("")
    for i in range(0, len(GAME_BOARD), 3):
        print(f'|  {GAME_BOARD[i]}  |  {GAME_BOARD[i+1]}  |  {GAME_BOARD[i+2]}  |\n')


def reset_board():
    global VICTORY_X
    global VICTORY_O
    global GAME_BOARD

    for i in range(0, 8):
        VICTORY_X[i] = 0
        VICTORY_O[i] = 0

    for i in range(0, 9):
        GAME_BOARD[i] = '_'


if __name__ == "__main__":

    while True:
        print(LOGO)
        game_over = False
        opponent = input("for playing against the computer press C : ").upper()
        # opponent = COMPUTER
        if opponent != COMPUTER:
            opponent = HUMAN
        player = PLAYER2
        # start the game first move is  played by X (C)
        reset_board()
        print_bord()
        while not game_over:
            print(f'player {player} your turn')
            if GAME_BOARD.count(FREE_SPC) > 0:
                game_status = play_move(player, opponent)
                if player == PLAYER1:
                    player = PLAYER2
                else:
                    player = PLAYER1
                if game_status in ('X', 'O'):
                    print(f'\n ****** And the Winner is ********* player-{game_status}')
                    game_over = True
            else:
                print(f'no more moves the board is full')
                game_over = True
                game_status = 0
            print_bord()
        if input('want another game press Y : ').upper() != 'Y':
            break

# end Main
