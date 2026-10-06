
# Placeholder for the actual board state
board_state = [
    ["R", "N", "B", "Q", "K", "B", "N", "R"],   # 0   INDEXES, !! NOT CHESS NOTATION !!
    ["P", "P", "P", "P", "P", "P", "P", "P"],   # 1
    [" ", " ", " ", " ", " ", " ", " ", " "],   # 2
    [" ", " ", " ", " ", " ", " ", " ", " "],   # 3
    [" ", " ", " ", " ", " ", " ", " ", " "],   # 4
    [" ", " ", " ", " ", " ", " ", " ", " "],   # 5
    ["p", "p", "p", "p", "p", "p", "p", "p"],   # 6
    ["r", "n", "b", "q", "k", "b", "n", "r"]    # 7
]
#     0    1    2    3    4    5    6    7
# First Index is the row (0-7), second index is the column (0-7)


def printBoard():


    # Print on the top
    print("   a b c d e f g h")
    print(" +-----------------+")   
    for i in range(8):
        print(f"{8 - i}| {' '.join(board_state[i])} |")
        print(" +-----------------+")

    # Print on the bottom
    print("   a b c d e f g h")

def updateBoard(move, playerNumber):

    # Vertical movement
    startY = move[2]
    endY = move[4]

    # 8 - row number = index in the board_state list

    # Horizontal movement
    startX = move[1]
    endX = move[3]
    startColumn = 0
    endColumn = 0

    # Convert the starting letter to a column index
    if startX == "a":
        startColumn = 0
    elif startX == "b":
        startColumn = 1 
    elif startX == "c":
        startColumn = 2
    elif startX == "d":
        startColumn = 3
    elif startX == "e":
        startColumn = 4
    elif startX == "f":
        startColumn = 5
    elif startX == "g":
        startColumn = 6
    elif startX == "h":
        startColumn = 7
    else:
        print("Invalid starting column letter.")
        return

    # Convert ending letter to column index
    if endX == "a":
        endColumn = 0
    elif endX == "b":
        endColumn = 1
    elif endX == "c":
        endColumn = 2
    elif endX == "d":
        endColumn = 3
    elif endX == "e":
        endColumn = 4
    elif endX == "f":
        endColumn = 5
    elif endX == "g":
        endColumn = 6
    elif endX == "h":
        endColumn = 7
    else:
        print("Invalid ending column letter.")
        return

    # Turn it to a coordinate system
    """
    startPos = (8 - int(startY), column)
    endPos = (8 - int(endY), column)
    """
    startRow = 8 - int(startY)
    endRow = 8 - int(endY)

    board_state[startRow][startColumn] = " "
    if playerNumber == 1:
        board_state[endRow][endColumn] = move[0].lower()
    else:
        board_state[endRow][endColumn] = move[0].upper()
    
 