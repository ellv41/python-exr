from function import *

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

