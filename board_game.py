import string
import numpy as np

USER1 = 1
USER2 = 2


def create_board(size):
    total_cells = size * size

    # create board
    board = np.zeros((size, size), dtype=int)
    cells = [(i, j) for i in range(size) for j in range(size)]

    # add player 1
    player_idxes = np.random.choice(range(len(cells)), size=int(total_cells / 2), replace=False)
    player_cells = [cells[i] for i in player_idxes]

    for i, (row, col) in enumerate(player_cells):
        if i <= total_cells / 4:
            board[col, row] = 1
        else:
            board[col, row] = 2
    return board


def afficher_carre(carre):
    # Si c'est le position de joueur 1, affichez '*'
    if carre == 1:
        return 'x'  # '•'
    # Si c'est le position de joueur 2, affichez '@'
    elif carre == 2:
        return 'o'  # '∘
    # Si le carre n'est pas occupé, affichez une espace empty
    else:
        return ' '


def afficher_grille(board):
    # afficher la row d'indice de colonne de 0-9:
    print('    ' + '   '.join([str(i) for i in range(len(board))]))
    # print('  -------------------------------------')
    print('-----' * board.shape[0])

    #afficher le reste de board:
    cpt = 0
    for row in board:
        chaque_ligne = ''
        #afficher chaque row avec son indice de A - I
        for col in row:
            chaque_ligne += afficher_carre(col) + ' | '
        print(cpt, '|', chaque_ligne)
        print('-----' * board.shape[0])
        cpt += 1
    print("Jouer 1:x                    Jouer 2: o")


def check_valid_and_get_opponent(board, s, e):
    user = board[s[0], s[1]]
    opponent_user = USER1 if user == USER2 else USER2

    opponent_cell = (-1, -1)

    if s[0] == e[0]:  # horizontal
        bidx = s[1] + 1 if s[1] < e[1] else e[1]  # begin index
        eidx = s[1] + 1 if s[1] > e[1] else e[1] + 1
        opponent_idx = e[1] + 1 if s[1] > e[1] else e[1] - 1

        segment = board[e[0], bidx:eidx]  # segment between s & e
        opponent_cell = (e[0], opponent_idx)  # opponent cell

        cond1 = any(segment != user)
        cond2 = sum(segment == opponent_user) == 1
        cond3 = board[e[0], opponent_idx] == opponent_user

    elif s[1] == e[1]:  # vertical
        bidx = s[0] + 1 if s[0] < e[0] else e[0]  # begin index
        eidx = s[0] if s[0] > e[0] else e[0]
        opponent_idx = e[0] + 1 if s[0] > e[0] else e[0] - 1

        segment = board[bidx:eidx, e[1]]  # segment between s & e
        opponent_cell = (opponent_idx, e[1])  # opponent 6cell

        cond1 = any(segment != user)
        cond2 = sum(segment == opponent_user) == 1
        cond3 = board[opponent_idx, e[1]] == opponent_user

    elif abs(s[0] - e[0]) == abs(s[1] - e[1]):  # diagonal
        cond1 = True
        cond2 = True
        cond3 = True

    return (cond1 and cond2 and cond3), opponent_cell


def update_opponent(board, cell):
    # change opponent color
    board[cell[0], cell[1]] = USER1 if board[cell[0], cell[1]] == USER2 else USER2
    return board


def update_cell(board, s, e):
    user = board[s[0], s[1]]
    # delete start
    board[s[0], s[1]] = 0
    # add end position
    board[e[0], e[1]] = user
    return board


def get_input(which="start"):
    inp = input(f"Enter {which}:\n")
    row, col = inp.split(' ')
    return (int(row), int(col))


def step(board, current_user, s=None, e=None):
    print("Your are player", current_user)
    # check start point, end point
    if s is None:
        s = get_input("start point")
    if e is None:
        e = get_input("end point")

    # start_valid
    if board[s[0], s[1]] != current_user:
        print("Invalid start point for user", current_user)
        return step(board, current_user, s=None, e=None)

    is_valid, opponent_cell = check_valid_and_get_opponent(board, s, e)
    if is_valid:
        board = update_opponent(board, opponent_cell)
        board = update_cell(board, s, e)

        # show board
        afficher_grille(board)

        # continue playing
        do_continue = input("Continue? (y/n):\n")

        if do_continue == 'y':
            return step(board, current_user, s=e, e=None)

        elif do_continue == 'n':
            current_user = USER1 if current_user == USER2 else USER2
            return step(board, current_user, s=None, e=None)


if __name__ == '__main__':
    size = int(input("Enter board size:\n"))
    board = create_board(size)
    afficher_grille(board)

    choose_new_board = True
    while choose_new_board:
        new_board = input("Do you want to create new board? (y/n):\n")
        if new_board == 'y':
            board = create_board(size)
            afficher_grille(board)
        elif new_board == 'n':
            choose_new_board = False

    user = input("Enter user you want to play:\n")
    step(board, USER1)
