### Player Classes ###

class Player:
    def __init__(self, color):
        self.color = color
        self.score = 2  # initial score
        self.is_turn = False

    def get_color(self):
        return self.color

    def update_score(self, score):
        self.score += score

    def switch_turn(self):
        self.is_turn = not self.is_turn


class AIPlayer(Player):
    def choose_move(self, game_board):
        # TODO: Implement the logic for choosing a move
        return (0, 0)  # Return a dummy move for now


class HumanPlayer(Player):
    pass
#     def get_input(self):
#         for event in pygame.event.get():
#             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#                 x, y = event.pos
#                 col = x // self.square_size
#                 row = y // self.square_size
#                 if 0 <= row < 8 and 0 <= col < 8:
#                     return (row, col)
#         return None