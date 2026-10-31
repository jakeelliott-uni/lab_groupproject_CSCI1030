import tkinter as tk
from chessGUI import *

GAME_REGISTRY = {
    "Chess": ChessGameGUI,
}

"""
This creates the main menu with buttons that connect to the start method of the gameGUI classes.
Any GUI class just needs to take 'root' and 'on_close' as arguments, and have a 'start()' method.
Could use a new coat of paint.
"""

class Launcher:
    def __init__(self, root):
        self.root = root
        self.main_frame = tk.Frame(root, height=200, width=300)
        self.main_frame.pack_propagate(False)
        self.active_game = None

        # Attach the game classes to each button, their start() method called through launch()
        for title, game_class in GAME_REGISTRY.items():
            tk.Button(
                self.main_frame,
                text=title,
                command=lambda cls=game_class: self.launch(cls)
            ).pack()

        self.main_frame.pack()

    def launch(self, game_class):
        self.main_frame.pack_forget()
        self.active_game = game_class(self.root, on_close=self.return_to_menu)
        self.active_game.start()

    # This is what's passed to 'on_close', it reopens this main menu 
    def return_to_menu(self):
        self.active_game = None
        self.main_frame.pack()

# Initializes the 'root', sets the initial menu title, initializes a Launcher(root), then runs .mainloop()
# Can make the actual main() less cluttered
def run():
    root = tk.Tk()
    root.title("Chess Arcade")
    Launcher(root)
    root.mainloop()

if __name__ == "__main__":
    run()