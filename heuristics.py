###############################################################################################################
# File: heuristics.py
# Authors: Nada Amgad , Nada Youssef
# Date: 2022-6-10
# Description: This file contains all the heuristics that will be used in the game.
############################################################################################################

# Demo for the board shape:
# 2D list where White is represented as W and Black is represented as B
#
# board = [
#     [" ", " ", " ", " ", " ", " ", " ", " "],
#     [" ", " ", " ", " ", " ", " ", " ", " "],
#     [" ", " ", " ", " ", " ", " ", " ", " "],
#     [" ", " ", " ", "W", "B", " ", " ", " "],
#     [" ", " ", " ", "B", "W", " ", " ", " "],
#     [" ", " ", " ", " ", " ", " ", " ", " "],
#     [" ", " ", " ", " ", " ", " ", " ", " "],
#     [" ", " ", " ", " ", " ", " ", " ", " "]
# ]


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
    # giving weights that will be used to calculate each heauristics according to the importance during playing
    coinParity_weight = 0.05
    mobility_weight = 0.35
    stability_weight = 0.2
    cornersCaptured_weight = 0.4
    def _init_(self):
       pass

    #ulternative function to calculate the utility value of heuristic
    #calculate the value based on adding together the weights of the squares in which the player’s coins are present.
    def utility(self,board ,player):
        #get the white coins locations
        white_locations = board.getLocations("W")
        #get the black coins locations
        black_locations = board.getLocations("B")
        #initialized white and black values
        white_coins_value =0
        black_coins_value =0
        #calculate the white coins values
        for location in white_locations:
            row, col = location
            white_coins_value += board_static_weights[row][col]
        #calculate the black coins values
        for location in black_locations:
            row, col = location
            black_coins_value += board_static_weights[row][col]
        #calculate white & black coins total utlity value
        white_utility_value = white_coins_value - black_coins_value
        black_utility_value = black_coins_value - white_coins_value

        #Scale the utility value to range from -100 to 100
        if(player == "W"):
            utility_scaled_value = 100 * (2 * (white_utility_value - black_utility_value) - (white_utility_value - black_utility_value - 2 * abs(white_utility_value))) / (white_utility_value - black_utility_value)

        elif(player == "B"):
            utility_scaled_value = 100 * (2 * (black_utility_value - white_utility_value) - (black_utility_value - white_utility_value - 2 * abs(black_utility_value))) / (black_utility_value - white_utility_value)

        return utility_scaled_value


    def coinParity(self, board, player):
        black_coins = 0
        white_coins = 0
        coinParityValue = 0
        # getting the current board
        board_coins = board.getBoard()

        #iterate through the whole board to count the number of black coins and white coins
        for row in board_coins: #rows
            for item in row: #columns (items)
                if (item == "B"):
                    black_coins = black_coins + 1
                elif (item == "W"):
                    white_coins = white_coins + 1

        #Assume that the max player plays with white coins
        #the value returned is in range of -100 to 100
        if(player == "W"):
            coinParityValue = 100 * ((white_coins - black_coins) / (white_coins + black_coins))
        elif(player == "B"):
            coinParityValue = 100 * ((black_coins - white_coins) / (black_coins + white_coins))


        return coinParityValue

    #method is used to calculate the heuristic value based on the mobility.
    def mobility(self, board, player):
        mobility_value = 0
        #counting the number of valid moves for each color
        white_actual_mobility = len(board.getValidMoves("W"))
        black_actual_mobility = len(board.getValidMoves("B"))
        #check the total moves value
        if white_actual_mobility + black_actual_mobility == 0:
            mobility_value = 0
        #calculate the mobility value
        if(player == "W"):
            mobility_value = 100*(white_actual_mobility - black_actual_mobility)/(white_actual_mobility + black_actual_mobility)
        elif (player == "B"):
            mobility_value = 100*(black_actual_mobility - white_actual_mobility)/(black_actual_mobility + white_actual_mobility)

        return mobility_value


    #method is used to calculate the heuristic value based on the corner captured.
    #by determining the actual captured corners and the potential captured corners
    def cornersCaptured(self,board ,player):
        #Actual captured corners
        #assign weights to actual and potential corners
        actual_corners_weight = 0.8
        potential_corners_weight = 0.2
        board_coins = self.board.getBoard()
        #initialize actual corners value for black and weight
        white_actual_corners_count = 0
        black_actual_corners_count = 0
        #initialize the total actual corners
        actualcornersCaptured_value=0
        #counting each captured corner for black and white_score
        #by checking each corner in the board
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

        #calculate the total actual corner value
        if white_actual_corners_count + black_actual_corners_count != 0:
            if(player == "W"):
                actualcornersCaptured_value = 100 * (white_actual_corners_count - black_actual_corners_count) / (white_actual_corners_count + black_actual_corners_count)
            elif(player == "B"):
                actualcornersCaptured_value = 100 * (black_actual_corners_count - white_actual_corners_count) / (black_actual_corners_count + white_actual_corners_count)

        #potential captured corners
        #initialize actual corners value for black and weight
        potential_black_corners = 0
        potential_white_corners = 0
        #initialize the total actual corners
        potentailcornersCaptured_value=0
        #get the valid next moves for each black and white
        white_valid_moves = board.getValidMoves("W")
        Black_valid_moves = board.getValidMoves("B")

    # Check and count potential corners for white
        for move in white_valid_moves:
            if move == [0,0]:
                potential_white_corners += 1
            elif move == [0, 7]:
                potential_white_corners += 1
            elif move == [7, 0]:
                potential_white_corners += 1
            elif move == [7, 7]:
                potential_white_corners += 1

        # Check and count potential corners for black
        for move in Black_valid_moves:
            if move == [0, 0]:
                potential_black_corners += 1
            elif move == [0, 7]:
                potential_black_corners += 1
            elif move == [7, 0]:
                potential_black_corners += 1
            elif move == [7, 7]:
                potential_black_corners += 1
        #calculate the total potential captured corners value
        if potential_black_corners + potential_white_corners != 0:
            if(player == "W"):
                potentailcornersCaptured_value = 100 * (potential_white_corners - potential_black_corners) / (potential_white_corners + potential_black_corners)
            elif(player == "B"):
                potentailcornersCaptured_value = 100 * (potential_black_corners - potential_white_corners) / (potential_black_corners + potential_white_corners)
        # calculate the total value of both actual and potential captured vlue
        corners_value = 100 * (actual_corners_weight * actualcornersCaptured_value + potential_corners_weight * potentailcornersCaptured_value)

        return corners_value


    def stability(self,board,player):

        print('in progress')
        return 1

    #method to Compute a heuristic value for an Othello board state based on a combination of factors,
    #including piece count, mobility, stability, and corners captured.
    def combinedHeuristics(self, board,player):

        coinParity_value = self.coinParity_weight * self.coinParity(board,player)
        mobility_value = self.mobility_weight * self.mobility(board,player)
        stability_value = self.stability_weight * self.stability(board,player)
        cornersCaptured_value = self.cornersCaptured_weight * self.cornersCaptured(board,player)

        value = coinParity_value + mobility_value + stability_value + cornersCaptured_value

        return value
