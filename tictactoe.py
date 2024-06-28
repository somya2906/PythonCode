#########  Python code for tic-tac-toe game ###############
from IPython.display import clear_output

#  function to diplay tic tac toe game board
def display_board(board):
    clear_output()
    print(' '+ board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---|---|---')
    print(' '+ board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---|---|---')
    print(' '+ board[1] + ' | ' + board[2] + ' | ' + board[3])

# function to have players choose between X or O
def start_input():
    print("Welcome to tic-tac-toe!")
    choice_1 = ''
    while choice_1 not in ['X', 'O']:
        choice_1 = input("Player 1: Choose between X and O: ")

    if choice_1 == 'X':
        choice_2 = 'O'
    elif choice_1 == 'O':
        choice_2 = 'X'

    print('Player 1 chooses ', choice_1)
    print('Player 2 chooses ', choice_2)
    return choice_1, choice_2

# function for player to choose there postion on the board
def pos_inp(taken_pos):
    pos = ''
    while pos not in range(1,10) or pos in taken_pos:
        if pos not in range(1,10):
            pos = int(input('Enter the postion between (1-9): '))
        if pos in taken_pos:
            pos = int(input('This position is already taken, enter another value between (1-9): '))

    taken_pos.append(pos)
    return taken_pos, pos

# function to update board
def update_board(pos,c1):
    if c1 % 2 == 0:
        test_board[pos] = P2
    else:
        test_board[pos] = P1

# function to check for the winner after every turn
def check_game(t):
    if ((t[1] == t[5] == t[9] == P1) or \
    (t[3] == t[5] == t[7] == P1) or \
    (t[1] == t[2] == t[3] == P1) or \
    (t[4] == t[5] == t[6] == P1) or \
    (t[7] == t[8] == t[9] == P1) or \
    (t[1] == t[4] == t[7] == P1) or \
    (t[2] == t[5] == t[8] == P1) or \
    (t[3] == t[6] == t[9] == P1)):
        print('Player1 Wins!!')
        game = 'off'
        return game
    elif ((t[1] == t[5] == t[9] == P2) or \
    (t[3] == t[5] == t[7] == P2) or \
    (t[1] == t[2] == t[3] == P2) or \
    (t[4] == t[5] == t[6] == P2) or \
    (t[7] == t[8] == t[9] == P2) or \
    (t[1] == t[4] == t[7] == P2) or \
    (t[2] == t[5] == t[8] == P2) or \
    (t[3] == t[6] == t[9] == P2)):
        print('Player2 Wins!!')
        game = 'off'
        return game
    else:
        game = 'on'
        return game


#### main logic begins ################
play_inp = 'yes'
test_board = [' '] * 10

while play_inp == 'yes':
    taken_pos = [0]
    c1 = 1
    play_inp = 'no'
    game = 'on'
    P1, P2 = start_input()
    while game == 'on':
        taken_pos, select_pos = pos_inp(taken_pos)
        update_board(select_pos,c1)
        display_board(test_board)
        game = check_game(test_board)
        c1 = c1 + 1
    play_inp = input('Do you want to play another game?(Yes/No): ')