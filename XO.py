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
    if A[row][column] != "X" and A[row][column] != "O":
        A[row][column] = a
    else:
        print(f"{y} YOU CHEATED!!!")
        exit(0)

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
fill(A)
print("In each turn put the number of an empty square to fill it with your symbol.")
player1 = input("Name of the first player is: ")
player2 = input("Name of the second player is: ")
input("Press enter when you are ready...")
print()
print_table(A)
print()
for i in range(9):
    print(f"{player1} It's your turn.")
    y = player1
    s = int(input())
    put("X", s)
    print_table(A)
    print()
    if check(A):
        print(f"{y} you WON!")
        break

    print(f"{player2} It's your turn.")
    y = player2
    s = int(input())
    put("O", s)
    print_table(A)
    print()
    if check(A):
        print(f"{y} you WON!")
        break
