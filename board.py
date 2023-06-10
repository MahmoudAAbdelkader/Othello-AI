class Board:
    BOARD = [
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", "W", "B", " ", " ", " "],
            [" ", " ", " ", "B", "W", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "]
        ]
    
    def __init__(self):
        self.count = 2

    def set_board(self, new_board):
        Board.BOARD = new_board

    def get_board(self):
        return Board.BOARD

    def get_piece(self, row, col):
        if row >= 0 and row < 8 and col >= 0 and col < 8:    
            return Board.BOARD[row][col]

    def set_piece(self, row, col, piece):
        Board.BOARD[row][col] = piece

    def is_game_over(self):
        # TODO: Implement the logic for determining if the game is over
        pass

    def set_valid_moves(self, valid_moves):
        for i in valid_moves:
            Board.BOARD[i[0]][i[1]] = 'V'