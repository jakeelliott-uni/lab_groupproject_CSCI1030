import tkinter as tk
import argparse
from chessGUI import *
from helperFunctions import *

GAME_REGISTRY = {
    "Chess": ChessGameGUI,
}

"""
This creates the main menu with buttons that connect to the start method of the gameGUI classes.
Any GUI class just needs to take 'root' and 'on_close' as arguments, and have a 'start()' method.
Terminal commands are also handled below and are passed to the Launcher.
Could use a new coat of paint.
"""

class Launcher:
    def __init__(self, root, args):
        self.root = root
        self.main_frame = tk.Frame(root, height=args.height, width=args.width)
        self.main_frame.pack_propagate(False)
        self.active_game = None

        # Attach the game classes to each button, their start() method called through launch()
        for title, game_class in GAME_REGISTRY.items():
            tk.Button(
                self.main_frame,
                text=title,
                command=lambda cls=game_class: self.launch(cls)
            ).pack()

        # interface-hadi: small tkinter button that opens a UI pop-up 
        tk.Button(
            self.main_frame, 
            text="Info", 
            command=lambda: messagebox.showinfo("Info", "Welcome to Chess Arcade!")
        ).pack(pady=5)

        

        # Create a button that when clicked opens an input box for a name
        create_player_button = tk.Button(
            self.main_frame,
            text="Create Player",
            command=ask_for_player_name,
        )
        create_player_button.pack(side="bottom", pady=10)
        # This name is used in helper ask_for_player_name() and create_player()
        # Where a json file is updated with the new player info 
        create_player_button = tk.Button(
            self.main_frame,
            text="Create Player",
            command=ask_for_player_name,
        )
        create_player_button.pack(side="bottom", pady=10)

        self.main_frame.pack()

    def launch(self, game_class):
        self.main_frame.pack_forget()
        self.active_game = game_class(self.root, on_close=self.return_to_menu)
        self.active_game.start()

    # This is what's passed to 'on_close', it reopens this main menu 
    def return_to_menu(self):
        self.active_game = None
        self.main_frame.pack()

# Add terminal command arguments here
def add_args_to_parser(parser):
    parser.add_argument('--width', type=int, default=700)
    parser.add_argument('--height', type=int, default=600)
    parser.add_argument('--title', type=str, default="Chess Arcade")  # argparse-hadi

# Create a parser object to collect command arguments
# Initializes the 'root', sets the initial menu title, initializes a Launcher(root), then runs .mainloop()
# Can make the actual main() less cluttered
def run():
    parser = argparse.ArgumentParser()
    add_args_to_parser(parser)
    args = parser.parse_args()

    root = tk.Tk()
    root.title("Chess Arcade")
    Launcher(root, args)
    root.mainloop()

if __name__ == "__main__":
    run()
