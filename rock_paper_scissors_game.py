import tkinter as tk
import random

# List of choices.
choices = ['Rock', 'Paper', 'Scissors']

# Method to check the winner.
def check_winner(user_choice):
    computer_choice = random.choice(choices)
    computer_choice_label['text'] = f"Computer chose {computer_choice}"

    # Logic.
    if user_choice == computer_choice:
        result_label['text'] = "It's a Draw!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result_label['text'] = "You Win!"
    else:
        result_label['text'] = "You Lose!"
    
# Method to exit the game.
def exit_game():
    root.destroy()

# Create the application assets.
root = tk.Tk()
root.title("Game")
root.geometry("300x300")

# Title label.
title_label = tk.Label(root, text="Rock, Paper, Scissors Game")
title_label.pack(pady=10)

# Button frame for buttons.
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# 'Rock' button.
rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 12), command=lambda: check_winner("Rock"))
rock_button.grid(row=0, column=0, padx=10)

# 'Paper' button.
paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 12), command=lambda: check_winner("Paper"))
paper_button.grid(row=0, column=1, padx=10)

# 'Scissors' button.
scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 12), command=lambda: check_winner("Scissors"))
scissors_button.grid(row=0, column=2, padx=10)

# Print the computer choice.
computer_choice_label = tk.Label(root, text="", font=("Arial", 12))
computer_choice_label.pack(pady=10)

# Print the winner.
result_label = tk.Label(root, text="", fg="dark blue", font=("Arial", 12))
result_label.pack(pady=10)

# Exit button.
exit_button = tk.Button(root, text="Exit", font=("Arial", 12), command=exit_game)
exit_button.pack(pady=10)

# Run the game.
root.mainloop()
