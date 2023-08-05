def fill(A):
    n = 1
    for i in range(3):
        for j in range(3):
            A[i][j] = n
            n += 1
    return A

def print_table(A):
    for i in  range(3):
        for j in range(3):
            print(A[i][j], end = " ")
        print()
    return A

def put(a, n):
    row = (n - 1) // 3
    column = (n - 1) % 3
    A[row][column] = a

def check(A):
    for i in range(3):
        if A[i][0] == A[i][1] == A[i][2]:
            return True
        if A[0][i] == A[1][i] == A[2][i]:
            return True
    if A[0][0] == A[1][1] == A[2][2]:
        return True
    if A[0][2] == A[1][1] == A[2][0]:
        return True
    
    return False

A = [[0] * 3 for i in range(3)]
