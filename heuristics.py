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


    def mobility(self, board, player):
        mobility_value = 0
        #counting the number of valid moves for each color
        white_actual_mobility = len(board.getValidMoves("W"))
        black_actual_mobility = len(board.getValidMoves("B"))
        if white_actual_mobility + black_actual_mobility == 0:
            mobility_value = 0

        if(player == "W"):
            mobility_value = 100*(white_actual_mobility - black_actual_mobility)/(white_actual_mobility + black_actual_mobility)
        elif (player == "B"):
            mobility_value = 100*(black_actual_mobility - white_actual_mobility)/(black_actual_mobility + white_actual_mobility)

        return mobility_value


    #method is used to calculate the heuristic value based on the corner captured.
    def cornersCaptured(self,board ,player):

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
            if(player == "W"):
                actualcornersCaptured_value = 100 * (white_actual_corners_count - black_actual_corners_count) / (white_actual_corners_count + black_actual_corners_count)
            elif(player == "B"):
                actualcornersCaptured_value = 100 * (black_actual_corners_count - white_actual_corners_count) / (black_actual_corners_count + white_actual_corners_count)

        potential_black_corners = 0
        potential_white_corners = 0
        potentailcornersCaptured_value=0

        white_valid_moves = board.getValidMoves("W")
        Black_valid_moves = board.getValidMoves("B")

    # Check potential corners for white
        for move in white_valid_moves:
            if move == [0,0]:
                potential_white_corners += 1
            elif move == [0, 7]:
                potential_white_corners += 1
            elif move == [7, 0]:
                potential_white_corners += 1
            elif move == [7, 7]:
                potential_white_corners += 1

        # Check potential corners for black
        for move in Black_valid_moves:
            if move == [0, 0]:
                potential_black_corners += 1
            elif move == [0, 7]:
                potential_black_corners += 1
            elif move == [7, 0]:
                potential_black_corners += 1
            elif move == [7, 7]:
                potential_black_corners += 1

        if potential_black_corners + potential_white_corners != 0:
            if(player == "W"):
                potentailcornersCaptured_value = 100 * (potential_white_corners - potential_black_corners) / (potential_white_corners + potential_black_corners)
            elif(player == "B"):
                potentailcornersCaptured_value = 100 * (potential_black_corners - potential_white_corners) / (potential_black_corners + potential_white_corners)

        corners_value = 100 * (actual_corners_weight * actualcornersCaptured_value + potential_corners_weight * potentailcornersCaptured_value)

        return corners_value



    def stability(self,board,player):

        #flag to be updated
        #if the coin is stable it will be 1
        #if the coin is unstable it will be 0
        #if the coin is semi-stable it will be -1

        max_stable = 0
        min_stable = 0
        for row in board:
            for item in row:
                if(item == player):
                    #case 1: the coin is in the corner then it's definetly stable
                    if ((row == 0 or row == 7) and (item == 0 or item ==7)):
                        max_stable += 1
                    #if the coin is found in the edges of the board we need to check
                    #that it has an adjacent element of its color to be stable
                    elif (row == 0 or row == 7 or item == 0 or item == 7):
                        if(row == 7):
                            if(board[row-1][item]== player):  #check item at [6,any column]
                                max_stable += 1
                        if (row == 0):
                            if (board[row + 1][item] == player): #check item at [1,any column]
                                max_stable += 1
                        if (item == 7):
                            if (board[row][item-1] == player): #check item at [any row,6]
                                max_stable += 1
                        if (item == 0):
                            if (board[row][item+1] == player): #check item at [any row,1]
                                max_stable += 1


                                # W        #     W
                                # W "W"    # "W" W
                                # W        #     W
                    elif (((board[row-1][item-1]==player)and(board[row][item-1]==player)and(board[row+1][item-1]==player))or
                          ((board[row-1][item+1]==player)and(board[row][item+1]==player)and(board[row+1][item+1]==player))or
                          ((board[row-1][item]==player)and(board[row][item-1]==player)and(board[row+1][item]==player))or
                          (((board[row-1][item]==player)and(board[row][item+1]==player)and(board[row+1][item]==player)))):
                        max_stable += 1


                elif ((item != player) and (item != ' ')):
                    # case 1: the coin is in the corner then it's definetly stable
                    if ((row == 0 or row == 7) and (item == 0 or item == 7)):
                        min_stable += 1
                    # if the coin is found in the edges of the board we need to check
                    # that it has an adjacent element of its color to be stable
                    elif (row == 0 or row == 7 or item == 0 or item == 7):
                        if (row == 7):
                            if (board[row - 1][item] == ((item != player) and (item != ' '))):  # check item at [6,any column]
                                min_stable += 1
                        if (row == 0):
                            if (board[row + 1][item] == ((item != player) and (item != ' '))):  # check item at [1,any column]
                                min_stable += 1
                        if (item == 7):
                            if (board[row][item - 1] == ((item != player) and (item != ' '))):  # check item at [any row,6]
                                min_stable += 1
                        if (item == 0):
                            if (board[row][item + 1] == ((item != player) and (item != ' '))):  # check item at [any row,1]
                                min_stable += 1



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
