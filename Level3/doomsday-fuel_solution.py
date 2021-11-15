from fractions import gcd
from fractions import Fraction
def multiply_matrices(a, b):
    a_rows = len(a)
    a_cols = len(a[0])
    b_cols = len(b[0])
    rows = a_rows
    cols = b_cols
    c = make_2d_list(rows, cols)
    for row in range(rows):
        for col in range(cols):
            dot_product = Fraction(0, 1)
            for i in range(a_cols):
                dot_product += a[row][i]*b[i][col]
            c[row][col] = dot_product
    return c

def multiply_row_of_square_matrix(m, row, k):
    n = len(m)
    row_operator = make_identity(n)
    row_operator[row][row] = k
    return multiply_matrices(row_operator, m)

def make_2d_list(rows, cols):
    a = []
    for row in range(rows):
        a += [[0] * cols]
    return a

def make_identity(n):
    result = make_2d_list(n, n)
    for i in range(n):
        result[i][i] = Fraction(1, 1)
    return result

def add_multiple_of_row_of_square_matrix(m, source_row, k, target_row):
    n = len(m)
    row_operator = make_identity(n)
    row_operator[target_row][source_row] = k
    return multiply_matrices(row_operator, m)

def invert_matrix(m):
    n = len(m)
    assert(len(m) == len(m[0]))
    inverse = make_identity(n)
    for col in range(n):
        diagonal_row = col
        assert(m[diagonal_row][col] != 0)
        k = Fraction(1, m[diagonal_row][col])
        m = multiply_row_of_square_matrix(m, diagonal_row, k)
        inverse = multiply_row_of_square_matrix(inverse, diagonal_row, k)
        source_row = diagonal_row
        for target_row in range(n):
            if source_row != target_row:
                k = -m[target_row][col]
                m = add_multiple_of_row_of_square_matrix(m, source_row, k, target_row)
                inverse = add_multiple_of_row_of_square_matrix(inverse, source_row, k, target_row)
    return inverse

def lcm(a, b):
    result = a * b / gcd(a, b)
    return result

def lcm_for_arrays(args):
    array_length = len(args)
    if array_length <= 2:
        return lcm(*args)
    initial = lcm(args[0], args[1])
    i = 2
    while i < array_length:
        initial = lcm(initial, args[i])
        i += 1
    return initial

def solution(m):
    nonterminals = []
    terminalstates = []
    reachableterminals = []
    probabilities = []
    sumofstates = []
    idx = 0
    for state in m:
        if all(transition==0 for transition in state):
            terminalstates.append(idx)
        else:
            nonterminals.append(idx)
        sumofstates.append(sum(state))
        idx += 1
    for state in m:
        probability = []
        idx = 0
        for transition in state:
            if (sumofstates[m.index(state)] != 0):
                probability.append(Fraction(transition, sumofstates[m.index(state)]))
            if (idx in terminalstates):
                if (transition != 0):
                    reachableterminals.append(idx)
            idx += 1
        if m.index(state) in terminalstates:
            m[m.index(state)][m.index(state)] = 1
            probabilities.append(m[m.index(state)])
        else:
            probabilities.append(probability)
    if len(terminalstates) == 1:
        return [1, 1]
    R = []
    for row in nonterminals:
        current_row = []
        for col in terminalstates:
            current_row.append(probabilities[row][col])
        R.append(current_row)
    Q = []
    for row in nonterminals:
        current_row = []
        for col in nonterminals:
            current_row.append(probabilities[row][col])
        Q.append(current_row)
    IQ = [([0]*(len(m)-len(terminalstates))) for i in range(len(m)-len(terminalstates))]
    for i in range(len(Q)):
        for j in range(len(Q[0])):
            if i == j:
                IQ[i][j] = 1-Q[i][j]
            else:
                IQ[i][j] = -Q[i][j]
    F = invert_matrix(IQ)
    FR = multiply_matrices(F,R)
    submission = []
    denominator = lcm_for_arrays([item.denominator for item in FR[0]])
    result = [item.numerator * denominator / item.denominator for item in FR[0]]
    result.append(denominator)
    for r in result:
        submission.append(int(float(r)))
    return submission




solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
solution([
        [1, 2, 3, 0, 0, 0],
        [4, 5, 6, 0, 0, 0],
        [7, 8, 9, 1, 0, 0],
        [0, 0, 0, 0, 1, 2],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ])
solution([
        [0, 0, 12, 0, 15, 0, 0, 0, 1, 8],
        [0, 0, 60, 0, 0, 7, 13, 0, 0, 0],
        [0, 15, 0, 8, 7, 0, 0, 1, 9, 0],
        [23, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [37, 35, 0, 0, 0, 0, 3, 21, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])
solution([
        [0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
        [0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
        [0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
        [48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
        [0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])
solution([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])
solution([
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])
solution([
        [0, 86, 61, 189, 0, 18, 12, 33, 66, 39],
        [0, 0, 2, 0, 0, 1, 0, 0, 0, 0],
        [15, 187, 0, 0, 18, 23, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])
solution([
        [0, 0, 0, 0, 3, 5, 0, 0, 0, 2],
        [0, 0, 4, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 4, 4, 0, 0, 0, 1, 1],
        [13, 0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 1, 8, 7, 0, 0, 0, 1, 3, 0],
        [1, 7, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])
