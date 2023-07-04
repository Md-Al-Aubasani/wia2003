import spacy
import time
import tkinter as tk
from tkinter import messagebox, simpledialog


def word_association_game():
    nlp = spacy.load("en_core_web_lg")

    players = int(entry_players.get())
    starting_word = entry_starting_word.get().lower()
    time_limit = 15  # Time limit for each player's turn

    current_word = starting_word
    doc_current = nlp(current_word)
    eliminated_players = set()

    current_player = 1

    while len(eliminated_players) < players - 1:
        if current_player not in eliminated_players:
            messagebox.showinfo("Word Association Game", f"Player {current_player}, it's your turn.\n"
                                                         f"The current word is: {current_word}")
            start_time = time.time()
            response = get_input("Word Association Game", "Enter a word:")
            end_time = time.time()

            if response == "quit":
                messagebox.showinfo("Word Association Game",
                                    f"Player {current_player} has quit the game.")
                eliminated_players.add(current_player)
                continue

            if end_time - start_time > time_limit:
                messagebox.showinfo("Word Association Game", f"Time's up for Player {current_player}!\n"
                                    f"They are eliminated.")
                eliminated_players.add(current_player)
                continue

            doc_response = nlp(response)

            if len(doc_current.ents) == 0 or len(doc_response.ents) == 0:
                messagebox.showinfo("Word Association Game", f"Sorry, the word '{response}' or '{current_word}' "
                                    f"could not be associated with any entities.\n"
                                    f"Player {current_player} is eliminated.")
                eliminated_players.add(current_player)
                continue

            similarity = doc_current.similarity(doc_response)
            category = doc_current.ents[0].label_ == doc_response.ents[0].label_

            if similarity < 0.3 and not category:
                messagebox.showinfo("Word Association Game", f"Sorry, the word '{response}' is not associated with "
                                    f"'{current_word}'.\nPlayer {current_player} is eliminated.")
                eliminated_players.add(current_player)
                continue

        current_player = (current_player % players) + 1

    winner = set(range(1, players + 1)) - eliminated_players
    if len(winner) > 0:
        messagebox.showinfo("Word Association Game",
                            f"Player {list(winner)[0]} is the winner!")
    else:
        messagebox.showinfo("Word Association Game",
                            "No winner. The game ended.")


def get_input(title, prompt):
    root = tk.Tk()
    root.withdraw()
    return simpledialog.askstring(title, prompt)


# Create the GUI window
window = tk.Tk()
window.title("Word Association Game")

# Create player input label and entry
label_players = tk.Label(window, text="Enter the number of players:")
label_players.pack()
entry_players = tk.Entry(window)
entry_players.pack()

# Create starting word input label and entry
label_starting_word = tk.Label(window, text="Enter the starting word:")
label_starting_word.pack()
entry_starting_word = tk.Entry(window)
entry_starting_word.pack()

# Create start button
start_button = tk.Button(window, text="Start Game",
                         command=word_association_game)
start_button.pack()

# Run the GUI event loop
window.mainloop()
