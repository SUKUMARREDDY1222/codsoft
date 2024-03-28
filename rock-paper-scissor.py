import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

# Function to play a round
def play_round(user_choice):
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    messagebox.showinfo("Result", f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}")

# Function to handle button clicks
def rock_click():
    play_round("rock")

def paper_click():
    play_round("paper")

def scissors_click():
    play_round("scissors")

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Create buttons
button_rock = tk.Button(root, text="Rock", command=rock_click)
button_rock.pack(pady=5)

button_paper = tk.Button(root, text="Paper", command=paper_click)
button_paper.pack(pady=5)

button_scissors = tk.Button(root, text="Scissors", command=scissors_click)
button_scissors.pack(pady=5)

# Choices list
choices = ['rock', 'paper', 'scissors']

root.mainloop()
