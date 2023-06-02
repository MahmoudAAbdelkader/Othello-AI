import tkinter as tk
from tkinter import messagebox
from board import ReversiBoard
from MinMax import getBestMove
from alphaBetaPruning import getBestMove as alphaBetaPruningBestMove


class OthelloGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Othello Game")
        self.board = ReversiBoard()
        self.player = "B"
        self.buttons = []

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
                messagebox.showinfo("Game Over", "Game Over! Winner: " + self.board.getWinner() + " With score: " + str(len(self.board.getLocations("W"))))
                self.disable_buttons()
            elif not self.board.hasValidMove(self.player):
                messagebox.showinfo("No Valid Moves", "No valid moves available for " + self.player + ". The other player continues.")
                self.player = "W" if self.player == "B" else "B"
                self.make_computer_move()
            else:
                self.player = "W" if self.player == "B" else "B"
                self.highlight_valid_moves()

        else:
            messagebox.showinfo("Invalid Move", "Invalid move! Please try again.")

    def update_board(self):
        for row in range(8):
            for col in range(8):
                button = self.buttons[row][col]
                button.config(text=self.board.board[row][col])

    def make_computer_move(self):
        # move = alphaBetaPruningBestMove(self.board, self.player, 2)
        move = getBestMove(self.board, self.player, 4)
        if move is not None:
            self.board.makeMove(self.player, move[0], move[1])
            self.update_board()

            if self.board.isGameOver():
                messagebox.showinfo("Game Over", "Game Over! Winner: " + self.board.getWinner() + " With score: " + str(len(self.board.getLocations("W"))))
                self.disable_buttons()
            elif not self.board.hasValidMove(self.player):
                messagebox.showinfo("No Valid Moves", "No valid moves available for " + self.player + ". The other player continues.")
                self.player = "W" if self.player == "B" else "B"
                self.highlight_valid_moves()
            else:
                self.player = "W" if self.player == "B" else "B"
                self.highlight_valid_moves()

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


if __name__ == '__main__':
    root = tk.Tk()
    game = OthelloGUI(root)
    root.mainloop()
