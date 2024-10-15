import sys
from utils.game import TicTacToe
import tkinter as tk
from tkinter import messagebox
from tkinter import font
import random

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.configure(bg="#1e1e1e")
        self.game = TicTacToe()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()
        self.root.geometry("500x500")
        self.root.bind("<Configure>", self.resize_widgets)

    def create_widgets(self):
        self.title = tk.Label(self.root, text="Tic-Tac-Toe", font=("Helvetica", 28, "bold"), fg="#f7f7f7", bg="#1e1e1e")
        self.title.pack(pady=20)

        self.frame = tk.Frame(self.root, bg="#1e1e1e")
        self.frame.pack(expand=True, fill="both")

        for r in range(3):
            for c in range(3):
                button = tk.Button(self.frame, text=" ", font=("Arial", 32, "bold"), fg="#ffffff",
                                  bg="#3a7bd5", activebackground="#ffb74d",
                                  command=lambda r=r, c=c: self.make_move(r, c),
                                  relief="groove", bd=6)
                button.grid(row=r, column=c, sticky="nsew", padx=10, pady=10)
                self.buttons[r][c] = button

        for r in range(3):
            self.frame.grid_rowconfigure(r, weight=1)
            self.frame.grid_columnconfigure(r, weight=1)

    def resize_widgets(self, event):
        new_size = min(self.root.winfo_width() // 10, self.root.winfo_height() // 10)
        self.title.config(font=("Helvetica", new_size, "bold"))

        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(font=("Arial", new_size, "bold"))

    def make_move(self, row, col):
        if self.game.board[row][col] == ' ':
            self.buttons[row][col].config(text=self.game.current_player, state=tk.DISABLED,
                                          disabledforeground=("#ff6347" if self.game.current_player == 'X' else "#4caf50"))
            self.game.board[row][col] = self.game.current_player
            if self.game.check_winner(row, col):
                self.game.winner = self.game.current_player
                self.end_game()
            elif self.game.is_game_over():
                self.end_game()
            else:
                self.game.current_player = 'O' if self.game.current_player == 'X' else 'X'

    def end_game(self):
        if self.game.winner:
            messagebox.showinfo("Game Over", f"Grattis! Spelare {self.game.winner} vinner!")
        else:
            messagebox.showinfo("Game Over", "Det blev oavgjort!")
        self.reset_game()

    def reset_game(self):
        self.game = TicTacToe()
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text=" ", state=tk.NORMAL, bg="#3a7bd5")


def main():
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()