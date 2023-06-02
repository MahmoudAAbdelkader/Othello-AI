import tkinter as tk
from tkinter import messagebox
from board import ReversiBoard
from MinMax import getBestMove
from alphaBetaPruning import getBestMove as alphaBetaPruningBestMove

import math


class OthelloGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Othello Game")
        self.board = ReversiBoard()
        self.player = "B"
        self.buttons = []

        self.white_label = tk.Label(self.root, text="White: 0")
        self.white_label.grid(row=8, column=0, columnspan=4)
        self.black_label = tk.Label(self.root, text="Black: 0")
        self.black_label.grid(row=8, column=4, columnspan=4)

        self.create_board()

    def create_board(self):
        for row in range(8):
            row_buttons = []
            for col in range(8):
                button = tk.Button(
                    self.root, text=self.board.board[row][col], width=5, height=2,
                    command=lambda r=row, c=col: self.make_move(r, c)
                )
                button.grid(row=row, column=col)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        self.highlight_valid_moves()

    def make_move(self, row, col):
        if self.board.isGameOver():
            messagebox.showinfo("Game Over", "The game is already over.")
            return

        if self.board.isValidMove(self.player, row, col):
            self.board.makeMove(self.player, row, col)
            self.update_board()

            if self.board.isGameOver():
                winner = self.board.getWinner()
                white_count = len(self.board.getLocations("W"))
                black_count = len(self.board.getLocations("B"))
                messagebox.showinfo("Game Over", f"Game Over! Winner: {winner} with score: White({white_count}), Black({black_count})")
                self.disable_buttons()

            else:
                self.player = "W" if self.player == "B" else "B"
                self.make_computer_move()

        else:
            messagebox.showinfo("Invalid Move", "Invalid move! Please try again.")

    def update_board(self):
        for row in range(8):
            for col in range(8):
                button = self.buttons[row][col]
                button.config(text=self.board.board[row][col])

    def make_computer_move(self):
        move = alphaBetaPruningBestMove(self.board, self.player, 7)
        if move is not None:
            self.board.makeMove(self.player, move[0], move[1])
            self.update_board()

            if self.board.isGameOver():
                winner = self.board.getWinner()
                white_count = len(self.board.getLocations("W"))
                black_count = len(self.board.getLocations("B"))
                messagebox.showinfo("Game Over", f"Game Over! Winner: {winner} with score: White({white_count}), Black({black_count})")
                self.disable_buttons()

            else:
                self.player = "W" if self.player == "B" else "B"
                self.highlight_valid_moves()
        self.update_cell_counts()

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")

    def highlight_valid_moves(self):
        for row in range(8):
            for col in range(8):
                button = self.buttons[row][col]
                if self.board.isValidMove(self.player, row, col):
                    button.config(bg="light green")
                else:
                    button.config(bg="SystemButtonFace")

    def update_cell_counts(self):
        white_count = len(self.board.getLocations("W"))
        black_count = len(self.board.getLocations("B"))
        self.white_label.config(text=f"White: {white_count}")
        self.black_label.config(text=f"Black: {black_count}")


if __name__ == '__main__':
    root = tk.Tk()
    game = OthelloGUI(root)
    root.mainloop()
