init_board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

test_board = [
    [0,1,2],
    [3,4,5],
    [6,7,8]
]
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(board)):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            # Skip a line
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + "", end=" ")

def test_print(board):
    for i in range(len(board)):
        if i == 1 or i == 2:
            print("------------")
        for j in range(len(board)):
            if j == 1 or j == 2:
                print(" | ", end="")
            if j == 2:
                print(board[i][j])
                print("\n")
            else:
                print(str(board[i][j]) + "", end=" ")


test_print(test_board)
#print_board(init_board)