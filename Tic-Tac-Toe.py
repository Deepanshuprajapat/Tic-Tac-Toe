import tkinter as tk
from tkinter import messagebox

# Initialize the game window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Game variables
current_player = "X"
game_over = False

# Winning combinations (indexes in the button list)
win_conditions = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]

# Function to check for a winner
def check_winner():
    global game_over
    for combo in win_conditions:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins! 🎉")
            game_over = True
            return

    # Check for a tie (if all buttons are filled)
    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "It's a tie! 🤝")
        game_over = True

# Function to handle button clicks
def button_click(index):
    global current_player, game_over
    if buttons[index]["text"] == "" and not game_over:
        buttons[index]["text"] = current_player
        check_winner()
        if not game_over:
            toggle_player()

# Function to switch players
def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

# Create buttons
buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, 
                     command=lambda i=i: button_click(i)) for i in range(9)]

# Place buttons in a 3x3 grid
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

# Display current player
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

# Run the Tkinter loop
root.mainloop()
