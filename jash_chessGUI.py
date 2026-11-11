# import tkinter as tk
# import random
# from pieces import *

# class ChessGameGUI:
#     def __init__(self, root, on_close):
#         self.root = root
#         self.on_close = on_close
#         self.frame = tk.Frame(root)

#         self.pieces = {}
#         self.buttons = {}
#         self.selected_piece = None
#         self.moves_count = 0  # Tracks two moves per turn

#     def start(self):
#         self.root.title("Chess Board")
#         self.root.protocol("WM_DELETE_WINDOW", self.quit)

#         # Standard back row for Player 1 (row 0)
#         self.pieces = {
#             (0, 0): Rook(0, 0),
#             (0, 1): Knight(0, 1),
#             (0, 2): Bishop(0, 2),
#             (0, 3): Queen(0, 3),
#             (0, 4): King(0, 4),
#             (0, 5): Bishop(0, 5),
#             (0, 6): Knight(0, 6),
#             (0, 7): Rook(0, 7),
#         }

#         # Standard back row for Player 2 (row 7)
#         back_row_p2 = [
#             Rook(7, 0), Knight(7, 1), Bishop(7, 2), Queen(7, 3), 
#             King(7, 4), Bishop(7, 5), Knight(7, 6), Rook(7, 7)
#         ]
#         for p in back_row_p2:
#             self.pieces[(p.row, p.col)] = p

#         # Randomize row 1 and row 6 with Bishop, Rook, or Knight (No Pawns)
#         random_choices = [Bishop, Rook, Knight]
#         for col in range(8):
#             p1_class = random.choice(random_choices)
#             self.pieces[(1, col)] = p1_class(1, col)

#             p2_class = random.choice(random_choices)
#             self.pieces[(6, col)] = p2_class(6, col)

#         # Build 8x8 grid of buttons
#         for row in range(8):
#             for col in range(8):
#                 bg = "#f0d9b5" if (row + col) % 2 == 0 else "#b58863"

#                 btn = tk.Button(
#                     self.frame,
#                     width=4,
#                     height=3,
#                     bg=bg,
#                     font=("Arial", 16, "bold"),
#                     command=lambda r=row, c=col: self.on_square_click(r, c),
#                 )
#                 btn.grid(row=row, column=col)
#                 self.buttons[(row, col)] = btn

#         self.frame.pack()
#         self.update_board()

#     def quit(self):
#         self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)
#         self.frame.pack_forget()
#         self.on_close()

#     def get_blocked_list(self):
#         return list(self.pieces.keys())

#     def on_square_click(self, row, col):
#         clicked_coord = (row, col)

#         if self.selected_piece is None:
#             if clicked_coord in self.pieces:
#                 self.selected_piece = self.pieces[clicked_coord]
#                 self.buttons[clicked_coord].config(bg="yellow")
#             return

#         if (self.selected_piece.row, self.selected_piece.col) == clicked_coord:
#             self.selected_piece = None
#             self.update_board()
#             return

#         old_coord = (self.selected_piece.row, self.selected_piece.col)
#         blocked = self.get_blocked_list()

#         moved = self.selected_piece.move(row, col, blocked)
#         if moved:
#             del self.pieces[old_coord]
#             self.pieces[clicked_coord] = self.selected_piece
#             self.selected_piece = None
            
#             # Count moves (allows two moves before resetting counter)
#             self.moves_count += 1
#             if self.moves_count >= 2:
#                 self.moves_count = 0

#             self.update_board()
#         else:
#             self.selected_piece = None
#             self.update_board()

#     def update_board(self):
#         for (r, c), btn in self.buttons.items():
#             default_bg = "#f0d9b5" if (r + c) % 2 == 0 else "#b58863"
#             btn.config(text="", bg=default_bg)

#             if (r, c) in self.pieces:
#                 piece_type = self.pieces[(r, c)].__class__.__name__
#                 label = "N" if piece_type == "Knight" else piece_type[0]
#                 btn.config(text=label)