from helperFunctions import *
from boardState import *
def main():
    print("Chess 2.0")
    print("////////////////////////////////")
    print("K = king, Q = Queen, B = Bishop, R = Rook, N = Knight, P = pawn")
    print("Input your move in Pa2b3 format.")
    # Format is flexible whatever is easier for Movement and BoardState
    print("Type Q to quit.")

    printBoard()

    player_turn = True

    while True:
        
        if player_turn:
            print("Player 1's turn.")
        else:
            print("Player 2's turn.")


        move = input("Enter your move: ")

        if move == "Q":
            print("This code ran")
            break

        if not cleanMoveInput(move):
            print("Try a different move.")
            continue

        # Jonad in progress: Coding updateBoard()
        if cleanMoveInput(move):
            print("Valid move input.")
            # Call updateBoard() with the move variable to update the board state
            updateBoard(move)
            # Print it afterwards
            printBoard()

        # Call boardState() and/or Update boardState() along with move variable like boardState(move)
        # e.g. state = boardState() or if no return values just boardState() and it prints the state

        # Handle what happens if there is a check or checkmate. Break loop if checkmate and declare winner. 
        # e.g. boardState() can return more than one value if there is a check or checkmate. 

        if player_turn:
            player_turn = False
        else:
            player_turn - True



if __name__ == '__main__':
    main()
 