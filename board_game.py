import sys
import math
import string
import numpy as np
from copy import deepcopy
from time import sleep
PLAYER1 = 1
PLAYER2 = 2
ALPHABET = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
CELL_CODE = [' ', 'x', 'o']


def cell2code(cell): # (0, 0) -> 'a1'
    return ALPHABET[cell[0]].upper() + str(cell[1] + 1)


def code2cell(code): # 'a1' -> (0, 0)
    row = ALPHABET.index(code[0])  # 'a' start from 0, 'b' start from 1, etc
    col = int(code[1:]) - 1  # 1 must start from 0 in python array
    return (row, col)


def create_board(size, style=1):  # 1 is a standard board;  2 is a random board
    total_cells = size * size

    # create zero board
    board = np.zeros((size, size), dtype=int)
    cells = [(i, j) for i in range(size) for j in range(size)]

    if style == 1:  # standard
        third = int(size // 3)
        board[0:third] = 1
        board[-third:] = 2
        return board
    else:  # random
        player_idxes = np.random.choice(range(len(cells)), size=int(total_cells / 2), replace=False)
        player_cells = [cells[i] for i in player_idxes]

        for i, (row, col) in enumerate(player_cells):
            if i <= total_cells / 4:
                board[col, row] = 1
            else:
                board[col, row] = 2
        return board


def highlight_cell(cell_code, cell_value, cell, cur_cell=None, cur_player=None):
    # highlight the current cell
    # cell_code = 'x' or 'o', cell = (row, col)
    if cur_player is not None and cell_value == cur_player:
        # highlight the cell that is occupied by current player in a very gray color
        return '\x1b[6;30;47m' + str(cell_code) + '\x1b[0m'
    if cur_cell is not None and cell[0] == cur_cell[0] and cell[1] == cur_cell[1]:
        return '\x1b[6;30;42m' + str(cell_code) + '\x1b[0m'
    return cell_code


def afficher_grille(board, cur_cell=None, cur_player=None):

    # afficher la row d'indice de colonne de 0-9:
    print('    ' + '   '.join([str(i + 1) for i in range(len(board))]))
    print('--+' + '---+' * board.shape[0])

    #afficher le reste de board:
    for row in range(board.shape[0]):
        chaque_ligne = ''
        #afficher chaque row avec son indice de A - I
        for col in range(board.shape[1]):
            cell = (row, col)
            cell_value = board[row, col]  # 0, 1, 2
            cell_code = CELL_CODE[cell_value]  # ' ', 'x', 'o'
            # following just hight light the cell
            cell_code = highlight_cell(cell_code, cell_value, cell=cell, cur_cell=cur_cell, cur_player=cur_player)
            chaque_ligne += cell_code + ' | '
        print(ALPHABET[row].upper(), '|', chaque_ligne)
        print('--+' + '---+' * board.shape[0])
    print(f"Jouer 1: {CELL_CODE[PLAYER1]}             Jouer 2: {CELL_CODE[PLAYER2]} ")


def get_step(number1, number2):
    diff = number2 - number1
    return int(math.copysign(1, diff)) if diff != 0 else 0


def get_interested_segment_and_cell(board, cur_cell, end_cell):
    # return the segment between a and b (include a and b)
    # and the cell that is prior to the end cell
    x1, y1 = cur_cell
    x2, y2 = end_cell

    row_step = get_step(x1, x2)  # 1 or -1 or 0
    col_step = get_step(y1, y2)  # 1 or -1 or 0

    row_idxs = list(range(x1, x2 + row_step, row_step)) if row_step != 0 else [x1] * (abs(y2 - y1) + 1)
    col_idxs = list(range(y1, y2 + col_step, col_step)) if col_step != 0 else [y1] * (abs(x2 - x1) + 1)

    segment = []  # will include both a and b
    for i, j in zip(row_idxs, col_idxs):
        segment.append(board[i, j])

    prior_end_cell = (row_idxs[-2], col_idxs[-2]) if len(segment) >= 2 else cur_cell
    return np.array(segment), prior_end_cell


def is_occupied_by_player(board, cell, player):
    return board[cell[0], cell[1]] == player


def get_number_of_cells_occupied_by(player, region):
    # return the number of cells occupied by player in region
    return np.sum(region == player)


def get_another_player(player):
    return PLAYER1 if player == PLAYER2 else PLAYER2


def is_valid_boundaries(board, cell):
    return 0 <= cell[0] < board.shape[0] and 0 <= cell[1] < board.shape[1]


def get_input(which="start"): # a2 b1 c8 -> [(0, 1), (1, 0), (2, 7)]
    input_codes = input(f"Enter {which}: (e.g: a2 B1 c8, etc)\n").strip().lower().split()
    return [code2cell(code) for code in input_codes]


def update_opponent(board, cell):
    # change opponent color
    board[cell[0], cell[1]] = PLAYER1 if board[cell[0], cell[1]] == PLAYER2 else PLAYER2
    return board


def update_cell(board, cur_cell, end_cell):
    cur_player = board[cur_cell[0], cur_cell[1]]
    board[cur_cell[0], cur_cell[1]] = 0  # delete current cell
    board[end_cell[0], end_cell[1]] = cur_player  # update end cell
    return board


def update_board(board, cur_cell, end_cell, opponent_cell):
    board = update_opponent(board, opponent_cell)
    board = update_cell(board, cur_cell, end_cell)
    return board


def check_finished(board, cur_player):
    opponent_player = get_another_player(cur_player)
    if np.sum(board == opponent_player) == 6:
        print("Game over! Player", cur_player, "won")
        if input("Play again? (y/n): ") == 'y':
            return game()
        else:
            sys.exit()


def do_if_valid(board, cur_player, cur_cell, end_cell, opponent_cell):
    board = update_board(board, cur_cell, end_cell, opponent_cell)
    # show board:  we need to pass the end_cell as cur_cell, see below line
    afficher_grille(board, cur_cell=end_cell)
    print(f"Yayay! Good move from {cell2code(cur_cell)} to {cell2code(end_cell)}!")
    sleep(1)
    print("Next player's turn", flush=True)
    return board


def step(board, cur_player, cur_cell, end_cell=None, next_move=None):
    playerA = cur_player  # current player
    playerB = get_another_player(playerA)  # another player / opponent

    if cur_cell is None:
        afficher_grille(board, cur_cell=cur_cell, cur_player=cur_player)  # show board with highlighted current cell
        print(f"Player {cur_player}, select a start cell to move, It must be occupied by {CELL_CODE[cur_player]}")

        cur_cell = get_input("the start cell")[0]
        afficher_grille(board, cur_cell=cur_cell)  # show board with highlighted current cell

    is_cur_cell_occupied_by_A = is_occupied_by_player(board, cur_cell, playerA)

    # case 1: cur cell is not occupied by current player or wrong inputs
    if not is_cur_cell_occupied_by_A or not is_valid_boundaries(board, cur_cell):
        afficher_grille(board, cur_cell=None)  # show board with no highlighted cells
        print("Wrong inputs for starting cell. Try again")
        return step(board, playerA, cur_cell=None, end_cell=None)  # ask for new input for cur cell & end cell

    # read next cell(s)
    print(f"You are at {ALPHABET[cur_cell[0]].upper()}{cur_cell[1] + 1}.", end=" ")
    next_cells = get_input("next cell(s)")
    
    STRATEGY = None # "kill" or "jump"

    cur_board = deepcopy(board)
    for i, end_cell in enumerate(next_cells):
        segment, prior_end_cell = get_interested_segment_and_cell(board, cur_cell, end_cell)
        end_cell_occupied_by_B = is_occupied_by_player(board, end_cell, playerB)
        prior_end_cell_occupied_by_B = is_occupied_by_player(board, prior_end_cell, playerB)

        num_cells_occupied_by_A = get_number_of_cells_occupied_by(playerA, segment)
        num_cells_occupied_by_B = get_number_of_cells_occupied_by(playerB, segment)
        
        # case 2: end cell has wrong inputs
        if not is_valid_boundaries(board, end_cell):
            afficher_grille(board, cur_cell=cur_cell)  # show board with highlighted current cell
            print("Wrong inputs for the next cell. Try again")
            return step(cur_board, playerA, cur_cell=cur_cell, end_cell=None)  # ask for new input for only end cell

        # case 3: jump over 1 cell occupied by opponent and land on an empty cell
        if num_cells_occupied_by_A == 1 and num_cells_occupied_by_B == 1 and prior_end_cell_occupied_by_B:
            opponent_cell = prior_end_cell
            if STRATEGY is None or STRATEGY == "jump":
                STRATEGY = "jump"
                board = do_if_valid(board, playerA, cur_cell, end_cell, opponent_cell)
                cur_cell = end_cell
            else:
                print("You cannot jump over 1 cell if you have already killed an opponent cell. Try again")
                return cur_board, cur_player

        # case 4: replace end cell if it is occupied by opponent
        if num_cells_occupied_by_A == 1 and num_cells_occupied_by_B == 1 and end_cell_occupied_by_B:
            opponent_cell = end_cell
            if STRATEGY is None and len(next_cells) == 1:
                STRATEGY = "kill"
                board = do_if_valid(board, playerA, cur_cell, end_cell, opponent_cell)
            elif STRATEGY == None and len(next_cells) > 1:
                print("You can perform 1 kill only. Try again")
                return cur_board, cur_player

            elif STRATEGY == "jump":
                print("You cannot kill an opponent cell if you have already jumped over 1 cell. Try again")
                return cur_board, cur_player
    
    check_finished(board, cur_player)
    return board, get_another_player(cur_player)


def select_board():
    board_style = input("Select the board style: 1 for a standard board, 2 for a random board.\nEnter board style: ")
    board_size = int(input("Enter board size (e.g. 9 for a 9x9 board): "))
    if board_style.strip() == '1':
        return create_board(board_size, style=1)
    elif board_style.strip() == '2':
        return create_board(board_size, style=2)
    else:  # wrong style: not 1 or 2
        return select_board()


def game():
    board = select_board()
    afficher_grille(board)
    cur_player = int(input("Enter player you want to play (Player 1 or Player 2) Enter 1 or 2: "))
    while True:
        board, cur_player = step(board, cur_player, cur_cell=None, end_cell=None)
        sleep(2)


if __name__ == '__main__':
    game()
