import random
import time
import tkinter as tk
from tkinter import messagebox

# Define the colors
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink']


class GameGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Color Sequence Game")

        self.pattern_label = tk.Label(self.root, text="Watch the pattern")
        self.pattern_label.pack(pady=10)

        self.user_guess = []

        self.color_buttons_frame = tk.Frame(self.root)
        self.color_buttons_frame.pack(pady=10)

        self.result_text = tk.Text(
            self.root, height=4, width=75)
        self.result_text.pack(pady=10)

#        self.submit_button = tk.Button(
#            self.root, text="Submit", command=self.check_guess)
#        self.submit_button.pack(pady=5)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=10)

        self.pattern = []

    def light_up_random_pattern(self, num):
        # Generate a random pattern of colors
        pattern = random.choices(colors, k=num)

        # Display the pattern
        for color in pattern:
            self.pattern_label.config(text=f"Lighting up {color}...")
            self.root.update()

            # Create color block
            color_frame = tk.Frame(self.root, width=50, height=50, bg=color)
            color_frame.pack(pady=15)
            self.root.update()
            time.sleep(1.5)  # Pause for 1.5 second between each color

            # Hide color block
            color_frame.destroy()
            self.root.update()
            time.sleep(0.5)  # Pause for 0.5 second between each color

        # Clear the pattern label
        self.pattern_label.config(text="")

        self.pattern = pattern

    def add_color_to_guess(self, color):
        if len(self.user_guess) < len(self.pattern):
            frame = tk.Frame(self.root, width=50, height=50, bg=color)
            frame.pack(side=tk.LEFT, padx=5)
            self.user_guess.append(color)

    def check_guess(self):
        pattern = self.pattern

        if self.user_guess == pattern:
            self.result_label.config(text="Congratulations! You won!")
        else:
            self.result_label.config(
                text="Sorry, your guess is incorrect.\nThe correct pattern was: " + ", ".join(pattern))

        self.user_guess = []

    def color_button_click(self, color):
        self.add_color_to_guess(color)
        if len(self.user_guess) == len(self.pattern):
            self.check_guess()

    def get_pattern_length(self):
        num = self.pattern_entry.get()

        # Validate the user input
        if not num.isdigit() or int(num) < 3:
            messagebox.showerror("Invalid pattern length",
                                 "Please enter a number above or equal to 3.")
            return

        num = int(num)
        self.light_up_random_pattern(num)

        self.pattern_entry.config(state=tk.DISABLED)
        # self.submit_button.config(state=tk.DISABLED)

    def play_game(self):
        # Randomly select a pattern length between 3 and 6
        # num = random.randint(3, 6)

        self.result_text.insert(tk.END, "Enter your mnemonic device here :)")

        self.pattern_entry = tk.Entry(self.root, width=5)
        self.pattern_entry.pack(pady=10)

        submit_button = tk.Button(
            self.root, text="Start Game", command=self.get_pattern_length)
        submit_button.pack(pady=5)

        # Create color buttons
        for color in colors:
            button = tk.Button(self.color_buttons_frame, width=5, height=2, bg=color,
                               command=lambda color=color: self.color_button_click(color))
            button.pack(side=tk.LEFT, padx=5)

        # self.light_up_random_pattern(num)

        self.root.mainloop()


# Start the game
game = GameGUI()
game.play_game()
