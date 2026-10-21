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

        if not validMove(move):
            print("Try a different move.")
            continue

        # Jonad in progress: Coding updateBoard()
        if validMove(move):
            print("Valid move input.")
            # Call updateBoard() with the move variable to update the board state
            if player_turn:
                playerNumber = 1
            else:
                playerNumber = 2

            if is_in_check(board_state, playerNumber):
                if move[0] not in "kK":
                    print("You must move your king out of check")
                    continue
            updateBoard(move, playerNumber)
            printBoard()

        # Call boardState() and/or Update boardState() along with move variable like boardState(move)
        # e.g. state = boardState() or if no return values just boardState() and it prints the state

        winner = check_winner(board_state)
        if winner != "None":
            print(winner)
            break 

        if player_turn:
            player_turn = False
        else:
            player_turn = True



if __name__ == '__main__':
    main()
 