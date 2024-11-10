"""
    Simulating of Transition Prob

"""

import numpy as np
import pandas as pd


def select_move(ava_places):
    """
        Select Move between options
    """
    y = np.random.randint(0, len(ava_places))
    y = ava_places[y]
    return y


def place_letter(pos, n, places, board):
    """
        Place a sign in the board
    """
    places.remove(pos)
    board[pos] = n
    return board


def tic_0(pos_0, size, a):
    """
        Construct Tic Tac Toe initial
    """
    tic_board = np.zeros((size, size))
    ava_places = [(i, j) for i in range(size) for j in range(size)]
    if pos_0 in ava_places:
        ava_places.remove(pos_0)
    tic_board[pos_0] = a
    return tic_board, ava_places


def check_rows(board, size):
    """
        Check the id rows to verify the tic tac toe
    """
    ava_rs = []
    for it in range(size):
        if board[it,:].min() > 0:
            ava_rs.append(it)
    return ava_rs

def check_cols(board, size):
    """
        Check cols 
    """
    ava_cs = []
    for jt in range(size):
        if board[:, jt].min() > 0:
            ava_cs.append(jt)
    return ava_cs


def extract_diag(board, size):
    """
        Extract the board diagonals
    """
    d_l = []
    d_r = []
    for it in range(size):
        d_l.append(board[it, it])
        d_r.append(board[it, size - (it + 1)])
    return [d_l, d_r]


def check_diag(board, size):
    """
        Check the diagonals
    """
    dd = extract_diag(board, size)
    ava_d = []
    for s, dg in enumerate(dd):
        q = np.array(dg)
        if q.min() > 0:
            ava_d.append(s)
    return ava_d


def verif_ttt(board, size, player):
    """
        A
    """
    rows = check_rows(board, size)
    cols = check_cols(board, size)
    diag = check_diag(board, size)
    if len(rows) > 0:
        for r in rows:
            if board[r,:].sum() % player == 0:
                return 1
    if len(cols) > 0:
        for c in cols:
            if board[:,c].sum() % player == 0:
                return 1
    if len(diag) > 0:
        dd = extract_diag(board, size)
        for d in diag:
            dy = np.array(dd[d])
            if dy.sum() % player == 0:
                return 1
    return 0


def winner(player, rival, board, size):
    """
        Select a Winner.
    """
    sp = verif_ttt(board, size, player=player)
    sr = verif_ttt(board, size, player=rival)
    result = sp * player + sr * rival
    result = 0.5 if result == 0 else result
    return result




def tic_tac_toe(pos_0, size, players, **kwargs):
    """
        Play a Tic Tac Toe
    """
    x = players[0]
    o = players[1]
    initial = kwargs.get("initial", x)
    if initial == x:
        rival = o
    else:
        rival = x
    board, places = tic_0(pos_0, size, initial)
    k = 1
    tic_board = board
    while True:
        sign = initial if k % 2 == 0 else rival
        pos = select_move(ava_places = places)
        tic_board = place_letter(pos, sign, places, board= tic_board)
        crit_w = winner(initial, rival, tic_board, SIZE_BOARD)
        if crit_w > 1 or k == size * size - 1:
            break
        k = k + 1
    return crit_w, tic_board



# Tic Tac Toe Game
X, O = 7, 5
SIZE_BOARD = 3
INIT_POS = (0, 0)


CRIT_W, TIC_BOARD = tic_tac_toe(INIT_POS, size = SIZE_BOARD, players=[X,O], initial = X)



board = pd.DataFrame(data = TIC_BOARD, index=range(SIZE_BOARD), columns=range(SIZE_BOARD))
board = board.replace(X, "X")
board = board.replace(O, "O")
board = board.replace(0, "")
print(CRIT_W)
print(board)
