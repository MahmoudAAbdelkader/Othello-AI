###############################################################################################################
# File: heuristics.py
# Authors: Nada Amgad , Nada Youssef
# Date: 2022-6-10
# Description: This file contains all the heuristics that will be used in the game.
############################################################################################################

board = [
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", "W", "B", " ", " ", " "],
    [" ", " ", " ", "B", "W", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "]
]


#static weight associated to each coin position

board_static_weights = [
    [4, -3, 2, 2, 2, 2, -3, 4],
    [-3, -4, -1, -1, -1, -1, -4, -3],
    [2, -1, 1, 0, 0, 1, -1, 2],
    [2, -1, 0, 1, 1, 0, -1, 2],
    [2, -1, 0, 1, 1, 0, -1, 2],
    [2, -1, 1, 0, 0, 1, -1, 2],
    [-3, -4, -1, -1, -1, -1, -4, -3],
    [4, -3, 2, 2, 2, 2, -3, 4]
]


class GameHeuristics():



    def _init_(self):
            coinParity_weight = 0.05
            mobility_weight = 0.35
            stability_weight = 0.2
            cornersCaptured_weight = 0.4



    def coinParity(self):
        print('in progress')


    def mobility(self, board):
        #counting the number of valid moves for each color
        white_actual_mobility = len(board.getValidMoves("W"))
        black_actual_mobility = len(board.getValidMoves("B"))
        if white_actual_mobility + black_actual_mobility == 0:
            mobility_value = 0

        mobility_value = 100*(white_actual_mobility - black_actual_mobility)/(white_actual_mobility + black_actual_mobility)

        return mobility_value


  #method is used to calculate the heuristic value based on the corner captured.
    def cornersCaptured(self):
        actual_corners_weight = 0.8
        potential_corners_weight = 0.2
        board_coins = self.board.getBoard()

        white_actual_corners_count = 0
        black_actual_corners_count = 0

        actualcornersCaptured_value=0

        if board_coins[0][0] == "W":
            white_actual_corners_count  += 1
        elif board_coins[0][0] == "B":
            black_actual_corners_count += 1

        if board_coins[0][7] == "W":
            white_actual_corners_count += 1
        elif board_coins[0][7] == "B":
            black_actual_corners_count += 1

        if board_coins[7][0] == "W":
            white_actual_corners_count += 1
        elif board_coins[7][0] == "B":
            black_actual_corners_count += 1

        if board_coins[7][7] == "W":
            white_actual_corners_count += 1
        elif board_coins[7][7] == "B":
            black_actual_corners_count += 1


        if white_actual_corners_count + black_actual_corners_count != 0:
            actualcornersCaptured_value = 100 * (white_actual_corners_count - black_actual_corners_count) / (white_actual_corners_count + black_actual_corners_count)

        potential_black_corners = 0
        potential_white_corners = 0
        potentailcornersCaptured_value=0

        white_valid_moves = board.getValidMoves("W")
        Black_valid_moves = board.getValidMoves("B")

    # Check potential corners for white
        for move in white_moves:
            if move == [0,0]:
                potential_white_corners += 1
            elif move == [0, 7]:
                potential_white_corners += 1
            elif move == [7, 0]:
                potential_white_corners += 1
            elif move == [7, 7]:
                potential_white_corners += 1

        # Check potential corners for black
        for move in black_moves:
            if move == [0, 0]:
                potential_black_corners += 1
            elif move == [0, 7]:
                potential_black_corners += 1
            elif move == [7, 0]:
                potential_black_corners += 1
            elif move == [7, 7]:
                potential_black_corners += 1

        if white_actual_corners_count + black_actual_corners_count != 0:
            potentailcornersCaptured_value = 100 * (potential_white_corners - potential_black_corners) / (potential_white_corners + potential_black_corners)

        corners_value = 100 * (actual_corners_weight * actualcornersCaptured_value + potential_corners_weight * potentailcornersCaptured_value)

        return corners_value



    def stability(self):
        print('in progress')

#method to Compute a heuristic value for an Othello board state based on a combination of factors,
#including piece count, mobility, stability, and corners captured.
    def combinedHeuristics(self, board):

        coinParity_value = coinParity_weight * self.coinParity(board)
        mobility_value = mobility_weight * self.mobility(board)
        stability_value = stability_weight * self.stability(board)
        cornersCaptured_value = cornersCaptured_weight * self.cornersCaptured(board)

        value = coinParity_value + mobility_value + stability_value + cornersCaptured_value

        return value
