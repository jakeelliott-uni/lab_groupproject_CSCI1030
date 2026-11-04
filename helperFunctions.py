import json
from tkinter import simpledialog, messagebox


###########################

"""
File I/O helpers.
"""

# Is called when the Create Player button is pressed.
# Open an input box and calls create_player() with the new name
# Handles the potential ValueError with a messagebox that displays error info
def ask_for_player_name():
    name = simpledialog.askstring("Create Player", "Enter a player name.")
    if not name:
        return

    try:
        create_player(name)
    except ValueError as error:
        messagebox.showerror("Could not create player", str(error))

# Try to open a profiles.json file and just pass if it isn't created yet.
# Check if the name already exists, raising a ValueError that is captured by ask_for_player_name()
# Add the new profile to the main json dict, then write over with the updated profiles
# Will auto create a profiles.json file if one doesn't exist in the current directory
# NOTE: Make sure to maintain the same directory when running or it will create duplicate .json files
def create_player(name):
    profiles = {}

    try:
        with open("profiles.json", "r") as file:
            profiles = json.load(file)
    except FileNotFoundError:
        pass

    if name in profiles:
        raise ValueError("That name already exists")

    profiles[name] = {"wins": 0, "losses": 0, "draw": 0}

    with open("profiles.json", "w") as file:
        json.dump(profiles, file)

###############################

def cleanMoveInput(move):
    pieces = "KQBRNP"
    square_letters = "abcdefgh"
    
    piece = move[0]
    letter_one = move[1]
    num_one = move[2]

    letter_two = move[3]
    num_two = move[4]

    if piece not in pieces:
        print("Unknwn piece")
        return False

    if letter_one not in square_letters or letter_two not in square_letters:
        print("Squares must be a letter from a - h")
        return False

    if int(num_one) < 1 or int(num_one) > 8 or int(num_two) < 1 or int(num_two) > 8:
        print("Grid must be a number from 1 - 8")
        return False

    return True


def validMove(move):
    if not cleanMoveInput(move):
        print("Invalid format")
        return False

    piece = move[0]
    piece = piece.lower()

    starting_num_x = letterToNumber(move[1])
    starting_num_y = int(move[2])
    ending_num_x = letterToNumber(move[3])
    ending_num_y = int(move[4])


    if piece == "p":
        if starting_num_x is not ending_num_x:
            print("Pawns only move one square forward except for their first move")
            return False

    if piece == "r":
        if starting_num_x is not ending_num_x and starting_num_y is not ending_num_y:
            print("Rooks only move in a straight line.")
            return False

    if piece == "k":
        if abs(ending_num_x - starting_num_x) > 1 or abs(ending_num_y - starting_num_y ) > 1:
            print("The King can only move one square at a time.")
            return False

    if piece == "b":
        if abs(ending_num_x - starting_num_x) != abs(ending_num_y - starting_num_y):
            print("Bishops only diagonally.")
            return False

    if piece == "n":
        diff_x = abs(ending_num_x - starting_num_x)
        diff_y = abs(ending_num_y - starting_num_y)
        if not ((diff_x == 1 and diff_y == 2) or (diff_x == 2 and diff_y == 1)):
            print("Knights only in an L-shape.")
            return False

    return True

def letterToNumber(letter):
    number = 0
    if letter == "a":
        number  = 0
    elif letter == "b":
        number = 1 
    elif letter == "c":
        number = 2
    elif letter == "d":
        number = 3
    elif letter == "e":
        number = 4
    elif letter == "f":
        number = 5
    elif letter == "g":
        number = 6
    elif letter == "h":
        number = 7
    else:
        print("Invalid starting number  letter.")
        return 0

    return number 
    
def check_winner(board):
    p1_king_alive = False
    p2_king_alive = False

    for row in board:
        for piece in row:
            if piece == 'k':
                p1_king_alive = True
            elif piece == 'K':
                p2_king_alive = True

    if p1_king_alive and not p2_king_alive:
        return "Player 1 Wins"
    elif p2_king_alive and not p1_king_alive:
        return "Player 2 Wins"
    else:
        return "None"


def numberToLetter(num):
    letters = "abcdefgh"
    return letters[num]


def is_in_check(board, playerNumber):
    king_row = -1
    king_col = -1
    target_king = 'k' if playerNumber == 1 else 'K'

    for r in range(8):
        for c in range(8):
            if board[r][c] == target_king:
                king_row = r
                king_col = c

    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece != " ":
                is_opponent = piece.isupper() if playerNumber == 1 else piece.islower()
                if is_opponent:
                    start_letter = numberToLetter(c)
                    start_num = str(8 - r)
                    end_letter = numberToLetter(king_col)
                    end_num = str(8 - king_row)
                    move_string = piece.upper() + start_letter + start_num + end_letter + end_num

                    if validMove(move_string):
                        return False
    return True



# oop-hadi: I just created a class representing a player profile managing  player state and methods
class PlayerProfile:
    def __init__(self, name, wins=0):
        self.name = name
        self.wins = wins

    def add_win(self):
        self.wins += 1

# fileio-hadi: function to save player score using json file I/O
import json

def save_player_score(name, wins):
    try:
        with open("profiles.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    data[name] = {"wins": wins}
    with open("profiles.json", "w") as f:
        json.dump(data, f)

# recursion-hadi: recursive function to count remaining pieces on the board
def count_pieces_recursive(board, row=0, col=0):
    if row >= len(board):
        return 0
    next_row = row + 1 if col == len(board[0]) - 1 else row
    next_col = 0 if col == len(board[0]) - 1 else col + 1
    has_piece = 1 if board[row][col] != " " else 0
    return has_piece + count_pieces_recursive(board, next_row, next_col)
