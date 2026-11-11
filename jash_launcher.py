# import tkinter as tk
# import argparse
# from jash_chessGUI import *
# from helperFunctions import *

# GAME_REGISTRY = {
#     "Chess": ChessGameGUI,
# }

# class Launcher:
#     def __init__(self, root, args):
#         self.root = root
#         self.main_frame = tk.Frame(root, height=args.height, width=args.width)
#         self.main_frame.pack_propagate(False)
#         self.active_game = None

#         for title, game_class in GAME_REGISTRY.items():
#             tk.Button(
#                 self.main_frame,
#                 text=title,
#                 command=lambda cls=game_class: self.launch(cls)
#             ).pack()

#         create_player_button = tk.Button(
#             self.main_frame,
#             text="Create Player",
#             command=ask_for_player_name,
#         )
#         create_player_button.pack(side="bottom", pady=10)

#         self.main_frame.pack()

#     def launch(self, game_class):
#         self.main_frame.pack_forget()
#         self.active_game = game_class(self.root, on_close=self.return_to_menu)
#         self.active_game.start()

#     def return_to_menu(self):
#         self.active_game = None
#         self.main_frame.pack()

# def add_args_to_parser(parser):
#     parser.add_argument('--width', type=int, default=700)
#     parser.add_argument('--height', type=int, default=600)

# def run():
#     parser = argparse.ArgumentParser()
#     add_args_to_parser(parser)
#     args = parser.parse_args()

#     root = tk.Tk()
#     root.title("Chess Arcade")
#     Launcher(root, args)
#     root.mainloop()

# if __name__ == "__main__":
#     run()