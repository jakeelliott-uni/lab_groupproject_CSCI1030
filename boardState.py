def printBoard():

    # Placeholder for the actual board state
    board_state = [
        ["R", "N", "B", "Q", "K", "B", "N", "R"],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        ["r", "n", "b", "q", "k", "b", "n", "r"]
    ]

    print("   a b c d e f g h")
    print(" +-----------------+")   
    for i in range(8):
        print(f"{8 - i}| {' '.join(board_state[i])} |")
        print(" +-----------------+")   

def updateBoard(move):
    
    pass
 