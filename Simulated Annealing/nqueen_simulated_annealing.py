import random
from math import exp
k = int(input("Enter a Number : "))
def get_random_board(n):
    board = []
    for i in range(0, n):
        row = random.randint(0, n - 1)
        board.append(row)
    print("Randomly generated board: ", board)
    return board


def count_conflicts(board):
    n = len(board)
    # for (int i = 0; i < n; i++)
    #    printf("%d %d", i, board[i]);

    row_conflicts = 0
    diag_conflicts = 0
    inv_diag_conflicts = 0

    for i in range(0, n):
        # q1 is queen 1 at (r1, c1)
        r1 = board[i]
        c1 = i
        for j in range(i + 1, n):
            # q2 is queen 2 at (r2, c2)
            r2 = board[j]
            c2 = j
            if r1 == r2:
                row_conflicts += 1
            if r1 - c1 == r2 - c2:
                diag_conflicts += 1
            if r1 + c1 == r2 + c2:
                inv_diag_conflicts += 1

    total_conflicts = row_conflicts + diag_conflicts + inv_diag_conflicts
    # print(row_conflicts, diag_conflicts, inv_diag_conflicts)
    return total_conflicts


def get_next_board(board):
    next_board = []

    c = random.randint(0, len(board) - 1)
    r = random.randint(0, len(board) - 1)
    next_board = list(board)
    next_board[c] = r

    conflicts = count_conflicts(next_board)
    return next_board, conflicts


board = get_random_board(k)

best_board = list(board)
E1 = count_conflicts(best_board)
print("Initial board: ", board, " Conflicts: ", E1)

T = 1000  # T is for temperature
cooling_rate = 0.006
count = 0
while T > 1:
    count+=1
    next_board, E2 = get_next_board(best_board)
    print("New board:     ", next_board, " Conflicts: ", E2)
    if E2 < E1:
        E1 = E2
        best_board = list(next_board)
    else:
        rnd = random.uniform(0, 1)
        if rnd < float(exp((E1-E2) /T)):
            E1 = E2
            best_board = list(next_board)
        if count_conflicts(best_board) == 0 and E1 == 0:
            break
    T = T - cooling_rate

print("Best board: ", best_board, " Conflicts: ", E1)
print(count)