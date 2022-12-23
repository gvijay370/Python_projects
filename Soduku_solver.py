# program to solve soduku 9*9 matrix#

test1 = [
    [1, -1, 6, -1, -1, 2, 3, -1, -1],
    [-1, 5, -1, -1, -1, 6, -1, 9, 1],
    [-1, -1, 9, 5, -1, 1, 4, 6, 2],
    [-1, 3, 7, 9, -1, 5, -1, -1, -1],
    [5, 8, 1, -1, 2, 7, 9, -1, -1],
    [-1, -1, -1, 4, -1, 8, 1, 5, 7],
    [-1, -1, -1, 2, 6, -1, 5, 4, -1],
    [-1, -1, 4, 1, 5, -1, 6, -1, 9],
    [9, -1, -1, 8, 7, 4, 2, 1, -1]
]

test2 = [
    [3, -1, 5, -1, 6, 4, -1, 1, 9],
    [7, 9, -1, 5, 1, -1, -1, 8, -1],
    [2, -1, -1, 3, -1, -1, 7, -1, -1],
    [5, 7, -1, 4, -1, 9, -1, -1, 6],
    [-1, 4, -1, 2, 7, 6, -1, 3, 8],
    [9, 6, -1, -1, 5, -1, -1, 4, -1],
    [6, 3, -1, -1, 2, -1, -1, 7, -1],
    [1, 5, -1, 8, 4, 7, -1, 6, 2],
    [4, 2, 7, 6, -1, 1, -1, -1, -1]
]


def next_free_cell(s):
    for i in range(9):
        for j in range(9):
            if s[i][j] == -1:
                return i, j
    return None, None


def validate(n, m, s, guess):
    # print(n,m)
    if guess in s[n]:
        return False
    for i in range(9):
        # print(i)
        # print(m)
        if s[i][m] == guess:
            return False
    r_c = (n // 3) * 3
    c_c = (m // 3) * 3

    for i in range(r_c, r_c + 3):
        for j in range(c_c, c_c + 3):
            if s[i][j] == guess:
                return False
    # s[n][m] = guess
    return True


def main(p):
    r, c = next_free_cell(p)
    if r == None:
        print(p)
        return True

    for guess in range(1, 10):
        if validate(r, c, p, guess):

            p[r][c] = guess

            if main(p):
                return True

    return False


if main(test1):
    pass
else:
    print('soduku is unsolvable')
