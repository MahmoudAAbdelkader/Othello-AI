from board import Board
### Player class ###

class Player:
    def __init__(self, color):
        self.color = color
        self.score = 2  # initial score
        self.is_turn = False

    def get_score(self):
        self.score = 0
        for row in Board.BOARD:
            for col in row:
                if col == self.color:
                    self.score += 1
        return self.score

    def get_color(self):
        return self.color

    # def switch_turn(self):
    #     self.is_turn = not self.is_turn

    # def is_my_turn(self):
    #     return self.is_turn


class AIPlayer(Player):
    def choose_move(self, game_board):
        # TODO: Implement the logic for choosing a move
        return (0, 0)  # Return a dummy move for now


class HumanPlayer(Player):
    pass
