import tkinter as tk
from pieces import *

class ChessGameGUI:
    def __init__(self, root, on_close):
        self.root = root
        self.on_close = on_close
        self.frame = tk.Frame(root)

        self.pieces = {}
        self.buttons = {}
        self.selected_piece = None

    def start(self):
        self.root.title("Chess Board")
        # Game state: map coordinates (row, col) -> Piece instance
        self.pieces = {
            (0, 0): Rook(0, 0),
            (0, 1): Knight(0, 1),
            (0, 2): Bishop(0, 2),
            (0, 3): Queen(0, 3),
            (0, 4): King(0, 4),
            (0, 5): Bishop(0, 5),
            (0, 6): Knight(0, 6),
            (0, 7): Rook(0, 7),
        }
        for i in range(8):
            self.pieces[(1, i)] = Pawn(1, i)

        # Build 8x8 grid of buttons
        for row in range(8):
            for col in range(8):
                # Checkerboard coloring
                bg = "#f0d9b5" if (row + col) % 2 == 0 else "#b58863"

                btn = tk.Button(
                    self.frame,
                    width=4,
                    height=3,
                    bg=bg,
                    font=("Arial", 16, "bold"),
                    command=lambda r=row, c=col: self.on_square_click(r, c),
                )
                btn.grid(row=row, column=col)
                self.buttons[(row, col)] = btn

        self.frame.pack()
        self.update_board()

    def quit(self):
        self.frame.pack_forget()
        self.on_close()

    def get_blocked_list(self):
        # Coordinates of all pieces currently on the board
        return list(self.pieces.keys())

    def on_square_click(self, row, col):
        clicked_coord = (row, col)

        # 1. No piece is selected yet: attempt selection
        if self.selected_piece is None:
            if clicked_coord in self.pieces:
                self.selected_piece = self.pieces[clicked_coord]
                self.buttons[clicked_coord].config(bg="yellow")
            return

        # 2. Clicking the currently selected piece deselects it
        if (self.selected_piece.row, self.selected_piece.col) == clicked_coord:
            self.selected_piece = None
            self.update_board()
            return

        # 3. Attempt movement
        old_coord = (self.selected_piece.row, self.selected_piece.col)
        blocked = self.get_blocked_list()

        # Call the piece's move method else clear selection
        moved = self.selected_piece.move(row, col, blocked)
        if moved:
            del self.pieces[old_coord]
            self.pieces[clicked_coord] = self.selected_piece
            self.selected_piece = None
            self.update_board()
        else:
            self.selected_piece = None
            self.update_board()

    def update_board(self):
        # Refresh visual labels and colors
        for (r, c), btn in self.buttons.items():
            default_bg = "#f0d9b5" if (r + c) % 2 == 0 else "#b58863"
            btn.config(text="", bg=default_bg)

            # First letter shorthand for each piece for now
            if (r, c) in self.pieces:
                piece_type = self.pieces[(r, c)].__class__.__name__
                label = "N" if piece_type == "Knight" else piece_type[0]
                btn.config(text=label)


if __name__ == "__main__":
    root = tk.Tk()
    gui = ChessGameGUI(root)
    root.mainloop()