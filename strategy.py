##############################################################################################################################
# Project Name :  Othello                                                                                                    #   
# File Name    :  strategy.py                                                                                                #
# Author       :  Hisham Yakan                                                                                               #
# Description  :  This file contains the strategy interface which is the base class for all the strategies used in the game. #
# Date         :  05/25/2023                                                                                                 #
#                                                                                                                            #                                 
##############################################################################################################################


# This is just an interface for the strategies (AlphaBetaPruning, MinMax)

from board import ReversiBoard

class Strategy:
    def __init__(self):
        pass
    
    def getBestMove(boardToGetBestMove : ReversiBoard,player,depth):
        pass
    def evaluateBoard(board: ReversiBoard,player):
        pass
    