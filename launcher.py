import tkinter as tk
from chessGUI import *

GAME_REGISTRY = {
    "Chess": ChessGameGUI,
}

class Launcher:
    def __init__(self, root):
        self.root = root
        self.main_frame = tk.Frame(root, height=200, width=300)
        self.main_frame.pack_propagate(False)
        self.active_game = None

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

    def return_to_menu(self):
        self.active_game = None
        self.main_frame.pack()

def run():
    root = tk.Tk()
    root.title("Chess Arcade")
    Launcher(root)
    root.mainloop()

if __name__ == "__main__":
    run()