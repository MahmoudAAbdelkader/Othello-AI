###############################################################################################################
# File: heuristics.py
# Authors: Nada Amgad , Nada Youssef
# Date: 2022-6-10
# Description: This file contains all the heuristics that will be used in the game.
##############################################################################################################
from board import boardobj
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

class GameHeuristics():
    def _init_(self):
       pass

    def coinParity(self):
        for row in board:
            for item in row:
                if (item == "B"):
                    B_coins = B_coins+1
                elif (item == "W"):
                    W_coins = W_coins+1

        if(B_coins > W_coins):
            coinParityWeight = 100 * ((B_coins - W_coins) / (B_coins + W_coins))
        else:
            coinParityWeight = 100*((W_coins-B_coins)/(W_coins+B_coins))

        return coinParityWeight

    def mobility(self):
        print('in progress')


    def cornersCaptured(self):
        print('in progress')


    def stability(self):
        print('in progress')


    def combinedHeuristics(self):
        print('in progress')