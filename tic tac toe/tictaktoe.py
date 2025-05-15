import tkinter as tk
from tkinter import messagebox

def check_winner():
    global winner
    for combo in [[0,1,2], [3,4,5], [6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != " ":
            for i in combo:
                buttons[i].config(bg='green')
            winner = True
            response = messagebox.askyesno("Game Over", f"{buttons[combo[0]]['text']} wins! Play again?")
            if response:
                reset_game()
            else:
                root.destroy()
            return

    if all(button["text"] != " " for button in buttons) and not winner:
        response = messagebox.askyesno("Game Over", "It's a draw! Play again?")
        if response:
            reset_game()
        else:
            root.destroy()

def button_click(index):
    if buttons[index]["text"] == " " and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        toggle_player()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

def reset_game():
    global current_player, winner
    for button in buttons:
        button.config(text=" ", bg="SystemButtonFace")
    current_player = "X"
    winner = False
    label.config(text=f"Player {current_player}'s turn")

root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [tk.Button(root, text=" ", font=('normal', 25), width=5, height=2,
                     command=lambda i=i: button_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

current_player = 'X'
winner = False

label = tk.Label(root, text=f"Player {current_player}'s turn", font=('normal', 15))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()
