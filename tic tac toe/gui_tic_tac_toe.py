import tkinter as tk
from tkinter import messagebox

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # Check rows
            return True
        if all(board[j][i] == player for j in range(3)):  # Check columns
            return True
    if all(board[i][i] == player for i in range(3)):      # Check diagonal
        return True
    if all(board[i][2 - i] == player for i in range(3)):  # Check anti-diagonal
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def on_button_click(row, col):
    global turn

    if board[row][col] == " ":
        board[row][col] = players[turn]
        buttons[row][col].config(text=players[turn])

        if check_winner(board, players[turn]):
            messagebox.showinfo("Game Over", f"Player {players[turn]} wins!")
            root.quit()
        elif is_board_full(board):
            messagebox.showinfo("Game Over", "It's a draw!")
            root.quit()

        turn = 1 - turn

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create the game board
board = [[" " for _ in range(3)] for _ in range(3)]
players = ["X", "O"]
turn = 0

# Create buttons for each cell on the board
buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", font=("Helvetica", 20), width=5, height=2,
                                  command=lambda row=i, col=j: on_button_click(row, col))
        buttons[i][j].grid(row=i, column=j)

# Start the Tkinter event loop
root.mainloop()
