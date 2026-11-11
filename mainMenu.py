import tkinter as tk
from chessGUI import ChessGameGUI # Import Hadi's class, thanks Hadi :P

#Jonad
class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Krazy Chess <TITLE W.I.P.>")
        self.root.geometry("700x600") # Dimensions of the window
        self.root.resizable(False, False) #P.S. I don't wanna have to deal with resizing graphics rn

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
        self.root.protocol("WM_DELETE_WINDOW", self.root.destroy) # What happens when the user clicks the x, terminates iot rather than just abruptly ending the program

        tk.Label(
            self.menu_frame,
            text = "WIP",
            font = ("Arial", 32, "bold")
        ).pack(pady = 50)

        self.create_button("Play", self.show_play_menu)
        self.create_button("Credits", self.show_credits)
        self.create_button("Quit", self.root.destroy)

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
                    "Name\n"
                    "Name\n"
                    "Name\n"
                    "Name\n"
                    "Name\n",
            font = ("Arial", 16),
            justify = "Center" # Text alignment
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

if __name__ == "__main__":
    root = tk.Tk()
    MainMenu(root)
    root.mainloop()