import tkinter as tk
import json
import argparse
from chessGUI import ChessGameGUI # Import Hadi's class, thanks Hadi :P

DEFAULT_CONFIG = {
    "title": "Krazy Chess",
    "width": 700,
    "height": 600
}
"""
AI Use:
Free AI Model: Gemini
Prompt: "What the heck do I do with recursion here? (Just answer, no code) <mainMenu.py attached>"

Response: 
"
There, are actually quite a few ways you can use recursion in your program!

Here are some ideas, from relatively simple to more advanced.
1. Count the pieces on the board
Beginner-friendly
Recursively go through a list of chess pieces and count how many remain.

Why it's useful: You could display how many pieces each player has remaining.
2. Check whether a square is occupied
Beginner-friendly
You could recursively search through your collection of pieces to determine whether a particular square is occupied.

Why it's useful: This could help with checking whether a destination square already contains a piece.
3. Display the board recursively
Beginner-friendly
Instead of using a regular loop to print each row of your chessboard, you could recursively print them.

Why it's useful: Demonstrates recursion through the actual chessboard.
4. Find possible moves for a piece
Intermediate
This one is particularly interesting!

Imagine a rook moving horizontally or vertically. You could recursively check each square in a direction until:
- It reaches the edge of the board.
- It encounters another piece.
- It encounters an enemy piece.

This is a simplified example; you'd still need to handle friendly and enemy pieces.
5. AI move searching
Advanced
If you eventually implement chess against an AI, recursion becomes incredibly useful.

The AI can:
1. Look at all possible moves.
2. Imagine what the opponent could do.
3. Imagine its next moves.
4. Evaluate which sequence is best.
This is commonly done using an algorithm called Minimax, which uses recursion to explore possible future game states.
"

"""


    # JONAD :: json

def load_config():
    try:
        with open("settings.json", "r") as file:
            config = json.load(file) # Reading the file as a py dict

        return config

    except FileNotFoundError:
        return DEFAULT_CONFIG.copy()

def save_config(config):
    with open("settings.json", "w") as file:
        json.dump(config, file)


#Jonad::OOP + GUI
class MainMenu:
    def __init__(self, root, config):
        self.root = root
        
        self.config = config
        # self.root.title("Krazy Chess <TITLE W.I.P.>")
        self.root.title(self.config["title"])
        #self.root.geometry("700x600") # Dimensions of the window
        self.root.geometry(f'{self.config["width"]}x{self.config["height"]}')
        self.root.resizable(False, False) #P.S. I don't wanna have to deal with resizing graphics rn
        # P.P.S, I'm gonna mess with it ig, if it beraks, it breaks.


        self.menu_frame = None # Holds the menu screen.
        self.active_game = None # This will hold the chess game in the future when it's running

        self.show_main_menu() # A function made below

    def clear_screen(self):
        if self.menu_frame is not None:
            self.menu_frame.destroy() # Deletes the previous frame and EVERYTHING inside it

        self.menu_frame = tk.Frame(self.root) # Creates a new frame
        self.menu_frame.pack(expand = True, fill = "both") # Dis play the new frame

    # Button creator
    def create_button(self, text, command, state="normal"):
        button = tk.Button(
            self.menu_frame,
            text = text,
            font = (14),
            width = 25,
            height = 2,
            command = command, # What happens when clocked
            state = state # Enabled/Disabled
        )
        button.pack(pady=8)

    # MAIN MENU

    def show_main_menu(self):
        self.clear_screen() # Make sure everything is reseted to default fistr
        self.root.title("Krazy Chess")
        #self.root.protocol("WM_DELETE_WINDOW", self.root.destroy) # What happens when the user clicks the x, terminates iot rather than just abruptly ending the program
        # replaced it with my own function

        self.root.protocol("WM_DELETE_WINDOW", self.quit_game)
        tk.Label(
            self.menu_frame,
            text = "WIP",
            font = ("Arial", 32, "bold")
        ).pack(pady = 50)

        self.create_button("Play", self.show_play_menu)
        self.create_button("Credits", self.show_credits)
        self.create_button("Quit", self.quit_game)

    # BUTTONS

    def show_play_menu(self):
        self.clear_screen() # As we transiting to a different frame, clear the previous one

        tk.Label(
            self.menu_frame,
            text = "play",
            font = ("Arial", 26, "bold")
        ).pack(pady = 40)

        self.create_button("Local", self.show_local_modes)
        self.create_button("Against AI", self.show_ai_modes)
        self.create_button("Back", self.show_main_menu)

    def show_local_modes(self):
        self.clear_screen()

        tk.Label(
            self.menu_frame,
            text = "Local Gamemodes",
            font = ("Arial", 26, "bold")
        ).pack(pady = 30)

        self.create_button("Regular", self.launch_chess)

        self.create_button("WIP (Coming Soon)", lambda: None, "disabled")
        self.create_button("WIP2 (Coming Soon)", lambda: None, "disabled")

        self.create_button("Back", self.show_play_menu)

    def show_ai_modes(self):
        self.clear_screen()

        tk.Label(
            self.menu_frame,
            text = "Against AI",
            font = ("Arial", 26, "bold")
        ).pack(pady = 30)

        self.create_button("Regular (Coming Soon)", lambda: None, "disabled")
        self.create_button("WIP (Coming Soon)", lambda: None, "disabled")

        self.create_button("Back", self.show_play_menu)

    def show_credits(self):
        self.clear_screen()

        tk.Label(
            self.menu_frame,
            text = "Credits",
            font = ("Arial", 26, "bold")
        ).pack(pady = 30)

        tk.Label(
            self.menu_frame,
            text = "Chess Game Thingy mabob\n\n\n" # !!! IMPORTATNT CHANGE THIS LATER DONT DORGET!!!
                    "Hadi Zahid"
                    "Jake Elliott\n"
                    "Jashahan Jagathas\n"
                    "Jonad Gabrielle Senolos\n"
                    "Ziad Ridwan\n",
            font = ("Arial", 16),
            justify = "center" # Text alignment
        ).pack(pady = 30)

        self.create_button("Back", self.show_main_menu) # PROBLEM NOT SHOWING!!!

    def launch_chess(self):
        self.menu_frame.pack_forget()
        # ^ Hides it, not delete, might come back to main menu

        # Test #1

        # !!!IF DOESNT WORK CHANGE IT!!!

        """
        self.active_game = ChessGameGUI( # Thanks Hadi :D
            # ^ Creates an INSTANCE of the game
            self.root,
            on_close=self.show_main_menu # callback function
        )
        """
        self.active_game = ChessGameGUI(self.root, on_close = self.show_main_menu)

        self.active_game.start()


    def quit_game(self):
        save_config(self.config)
        self.root.destroy()

# Jonad :: argparse
def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Launch Krazy Chess with custom settings."
    )

    parser.add_argument("--title", type=str, help="Window title")
    parser.add_argument("--width", type=int, help="Window width")
    parser.add_argument("--height", type=int, help="Window height")

    return parser.parse_args()

if __name__ == "__main__":
    root = tk.Tk()

    config = load_config()

    args = parse_arguments()

    if args.title is not None:
        config["title"] = args.title

    if args.width is not None:
        config["width"] = args.width

    if args.height is not None:
            config["height"] = args.height

    MainMenu(root, config)
    root.mainloop()