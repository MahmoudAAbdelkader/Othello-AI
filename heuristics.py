###############################################################################################################
# File: heuristics.py
# Authors: Nada Amgad , Nada Youssef
# Date: 2022-6-10
# Description: This file contains all the heuristics that will be used in the game.
############################################################################################################
from board import ReversiBoard

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
    # giving weights that will be used to calculate each heuristics according to the importance during playing
    #maximum weight given to "corners captured" followed by "mobility"
    #then "Stability" and finally "coin parity" as it does not affect much
    coinParity_weight = 0.1
    mobility_weight = 0.40
    stability_weight = 0.05
    cornersCaptured_weight = 0.45  #one of the most important heuristics so we assigned to it the maximum weight
    def _init_(self):
        pass


    #alternative function to calculate the utility value of heuristic
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

        if(white_utility_value == black_utility_value):
            return 0

        #Scale the utility value to range from -100 to 100
        if(player == "W"):
            if (white_utility_value>14):
                white_utility_value=14
            elif(white_utility_value<-14):
                white_utility_value=-14
            utility_scaled_value = (100*white_utility_value)/14

        elif(player == "B"):
            if (black_utility_value>14):
                black_utility_value=14
            elif(black_utility_value<-14):
                black_utility_value=-14
            utility_scaled_value = (100*black_utility_value)/14

        return utility_scaled_value



    #This method is used to calculate the heuristics based on the coin parity
    #The player who has the most coins on the board has higher value
    def coinParity(self, board : ReversiBoard, player):
        black_coins = 0
        white_coins = 0
        coinParityValue = 0

        # getting the current board
        board_coins = board.getBoard()

        #iterate through the whole board to count the number of black coins and white coins
        for row in board_coins: #rows
            for item in row: #columns (items)
                if (item == "B"):
                    #counting the black coins
                    black_coins = black_coins + 1
                elif (item == "W"):
                    # counting the white coins
                    white_coins = white_coins + 1

        #Assume that the max player plays with white coins
        #the value returned is in range of -100 to 100
        if(player == "W"):
            coinParityValue = 100 * ((white_coins - black_coins) / (white_coins + black_coins))
        elif(player == "B"):
            coinParityValue = 100 * ((black_coins - white_coins) / (black_coins + white_coins))


        return coinParityValue


    #method is used to calculate the heuristic value based on the mobility.
    def mobility(self, board : ReversiBoard, player):
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
    def cornersCaptured(self,board:ReversiBoard ,player):
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
        corners_value = (actual_corners_weight * actualcornersCaptured_value + potential_corners_weight * potentailcornersCaptured_value)

        return corners_value

    # This method is used to calculate the heuristic value based on the stability of the coin
    def stability(self,board : ReversiBoard ,player):

        #flags to be updated
        #if the coin is stable it will be incremented by 1
        #if the coin is semi-stable it will be 0
        #if the coin is unstable it will be decremented by -1
        max_player_stability_value = 0
        min_player_stability_value = 0

        #get the current board in the game
        board_stability = board.getBoard()

        for row in range (8): #iterating through rows
            for item in range (8): #iterating through col to get the items
                if(board_stability[row][item] == "W"):

                    #Case 1: the coin is in the corner then it's definetly stable

                    if ((row == 0 or row == 7) and (item == 0 or item ==7)):
                        max_player_stability_value += 1

                    #Case 2: if the coin is found in the edges of the board we need to check
                    #that it has an adjacent element of its color to be stable

                    elif (row == 0 or row == 7 or item == 0 or item == 7):
                        if(row == 7):
                            if(board_stability[row-1][item]== "W"):  #check item at [6,any column]
                                max_player_stability_value += 1
                        if (row == 0):
                            if (board_stability[row + 1][item] == "W"): #check item at [1,any column]
                                max_player_stability_value += 1
                        if (item == 7):
                            if (board_stability[row][item-1] == "W"): #check item at [any row,6]
                                max_player_stability_value += 1
                        if (item == 0):
                            if (board_stability[row][item+1] == "W"): #check item at [any row,1]
                                max_player_stability_value += 1


                    # Sample for the cases that can be stable in case max player is W
                    # W        #     W     #    W     #   W
                    # W "W"    # "W" W     # W "W"    #  "W" W
                    # W        #     W     #    W     #   W
                    #
                    elif (((board_stability[row-1][item-1]=="W")and(board_stability[row][item-1]=="W")and(board_stability[row+1][item-1]=="W"))and
                          ((board_stability[row-1][item+1]=="W")and(board_stability[row][item+1]=="W")and(board_stability[row+1][item+1]=="W"))and
                          ((board_stability[row-1][item]=="W")and(board_stability[row+1][item]=="W"))
                    ):
                        max_player_stability_value += 1

                    #checking if the coin can be unstable in future moves
                    elif any(board_stability[i][j] == " " for i in range(row - 1, row + 2) for j in range(item - 1, item + 2)):
                        max_player_stability_value += 0

                    #any case other than those handled before will be unstable
                    else:
                        max_player_stability_value -= 1


                elif (board_stability[row][item] == "B"):

                    # case 1: the coin is in the corner then it's definetly stable

                    if ((row == 0 or row == 7) and (item == 0 or item == 7)):
                        min_player_stability_value += 1

                    # if the coin is found in the edges of the board we need to check
                    # that it has an adjacent element of its color to be stable

                    elif (row == 0 or row == 7 or item == 0 or item == 7):
                        if (row == 7):
                            if (board_stability[row - 1][item] == "B"):  # check item at [6,any column]
                                min_player_stability_value += 1
                        if (row == 0):
                            if (board_stability[row + 1][item] == "B"):  # check item at [1,any column]
                                min_player_stability_value += 1
                        if (item == 7):
                            if (board_stability[row][item - 1] == "B"):  # check item at [any row,6]
                                min_player_stability_value += 1
                        if (item == 0):
                            # == ((item != player) and (item != ' ')) may be needed
                            if (board_stability[row][item + 1] == "B"):  # check item at [any row,1]
                                min_player_stability_value += 1

                    #Sample for the cases that can be stable in case min player is B
                    # B        #     B     #    B     #   B
                    # B "B"    # "B" B     # B "B"    #  "B" B
                    # B        #     B     #    B     #   B

                    elif (((board_stability[row-1][item-1] == "B")and(board_stability[row][item-1] == "B")and(board_stability[row+1][item-1] == "B"))and
                          ((board_stability[row-1][item+1] == "B")and(board_stability[row][item+1] == "B")and(board_stability[row+1][item+1] == "B"))and
                          ((board_stability[row-1][item] == "B")and(board_stability[row+1][item] == "B"))):
                        min_player_stability_value += 1

                    #checking if the coin will be unstabel in future moves

                    elif any(board_stability[i][j] == " " for i in range(row - 1, row + 2) for j in range(item - 1, item + 2)):
                        min_player_stability_value += 0

                    #any case other than those handled before will be unstable
                    else:
                        min_player_stability_value -= 1

        # max_player_stability_value = max_stable + max_unstable + max_semistable
        # min_player_stability_value = min_stable + min_unstable + min_semistable

        if ((max_player_stability_value + min_player_stability_value) != 0):
            if(player == "W"):
                Stability_heuristic_value = 100 * ((max_player_stability_value - min_player_stability_value ) /(abs(max_player_stability_value) + abs(min_player_stability_value)))
            if(player == "B"):
                Stability_heuristic_value = 100 * ((min_player_stability_value - max_player_stability_value ) /(abs(min_player_stability_value) + abs(max_player_stability_value)))

        else:
            Stability_heuristic_value = 0

        return Stability_heuristic_value


    #method to Compute a heuristic value for an Othello board state based on a combination of factors,
    #including piece count, mobility, stability, and corners captured.
    def combinedHeuristics(self, board: ReversiBoard,player):

        coinParity_value = self.coinParity_weight * self.coinParity(board,player)
        mobility_value = self.mobility_weight * self.mobility(board,player)
        stability_value = self.stability_weight * self.stability(board,player)
        cornersCaptured_value = self.cornersCaptured_weight * self.cornersCaptured(board,player)

        value = coinParity_value + mobility_value + stability_value + cornersCaptured_value

        return value

    ###############################################################################################################
    # Testing the heuristic functions
    ###############################################################################################################

board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],

         [' ', ' ', ' ', ' ', ' ', 'W', ' ', ' '],

         [' ', ' ', 'W', 'W', 'W', 'B', ' ', ' '],

         [' ', ' ', 'B', 'W', 'B', ' ', ' ', ' '],

         [' ', ' ', 'B', 'B', 'W', ' ', ' ', ' '],

         [' ', ' ', 'B', ' ', ' ', ' ', ' ', ' '],

         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],

         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
reversi_board = ReversiBoard()
reversi_board.board = board

reversi_board.whoseTurn = 'W'

reversi_board.print()

heuristic = GameHeuristics()

value = heuristic.stability(reversi_board, 'W')

print("Stability heuristic value: ", value)


