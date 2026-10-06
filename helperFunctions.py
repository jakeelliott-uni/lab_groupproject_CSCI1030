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