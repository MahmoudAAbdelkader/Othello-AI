##############################################################################################################################
# Project Name :  Othello                                                                                                    #   
# File Name    :  strategy.py                                                                                                #
# Author       :  Hisham Yakan                                                                                               #
# Description  :  This file contains the class that implements the MinMax algorithm. The class inherits from the Strategy    #
#                interface.                                                                                                  #
# Date         :  05/25/2023                                                                                                 #
#                                                                                                                            #                                 
##############################################################################################################################

# We need to implement the MinMax algorithm to determine the best move for the computer.
# The MinMax algorithm is a recursive algorithm that is used to choose an optimal move for a player assuming that the opponent is also playing optimally.
# The algorithm searches the game tree starting from the current state of the game and explores all the way down to the terminal states (i.e. states where the game is over).
# The algorithm then evaluates the terminal states using a heuristic function and propagates the values back up the tree.

# The following code is used to test the MinMax algorithm.

from strategy import Strategy
from board import ReversiBoard
import math
import heuristics
import time


maximixingPlayer = None

class MinMaxStrategy(Strategy):
    difficulty = None


    ##############################################################################################################################    
    
    # Method Name: evaluateBoard
    
    # Purpose: This method is used to evaluate the board for the given player.

    # Method Description:
    # This method is used to evaluate the board for the given player.
    # The evaluation function is the difference between the number of pieces of the given player and the number of pieces of the opponent.
    
    #function Arguments:
    #board: The current state of the game.
    #player: The player for whom we are calculating the score W or B.
    
    ##############################################################################################################################   

    def evaluateBoard(board: ReversiBoard,player):
        
        if(MinMaxStrategy.difficulty == "easy"):
            return board.getScore(maximixingPlayer) - board.getScore(board.getOpponent(maximixingPlayer))
        
        hueristicsObj = heuristics.GameHeuristics()
        coin_parity = hueristicsObj.coinParity(board,maximixingPlayer)
        
        mobility = hueristicsObj.mobility(board,maximixingPlayer)
        cornersCaptured = hueristicsObj.cornersCaptured(board,maximixingPlayer)
        stability = hueristicsObj.stability(board,maximixingPlayer)
        utility = hueristicsObj.utility(board,maximixingPlayer)
        
        combinedHeuristic = hueristicsObj.combinedHeuristics(board,maximixingPlayer)
        
        if(utility > 100 or utility < -100):
            raise Exception("Utility is greater than 100 or less than -100")
        
        if(coin_parity > 100 or coin_parity < -100):
            raise Exception("Coin Parity is greater than 100 or less than -100")
        
        if(stability > 100 or stability < -100):
            raise Exception("Stability is greater than 100 or less than -100")
        
        if(mobility > 100 or mobility < -100):
            raise Exception("Mobility is greater than 100 or less than -100")
        
        if(cornersCaptured > 100 or cornersCaptured < -100):
            raise Exception("Corners Captured is greater than 100 or less than -100")
        
        # return utility
        return combinedHeuristic
        
    #     return combinedHeuristic

    ##############################################################################################################################
    
    # Method Name: getBestMove
    
    # Purpose: This method is used to get the best move for the given player using MinMax algorithm.
    
    # Method Description:
    # This method is used to get the best move for the given player using MinMax algorithm. 
    
    #function Arguments:
    #board: The current state of the game.
    #player: The player for whom we are calculating the move W or  B.
    #depth: The depth of the game tree that we want to search.
    
    ##############################################################################################################################
    def getBestMove(boardToGetBestMove : ReversiBoard,player,depth):
        
        global maximixingPlayer
        print(f"Maximizing Player = {maximixingPlayer}")
        maximixingPlayer = player
        print(f"Maximizing Player = {maximixingPlayer}")
        super().getBestMove(boardToGetBestMove,player,depth)


        if (boardToGetBestMove.isGameOver()):
            return None

        # Get all the valid moves for the given player.
        validMoves = boardToGetBestMove.getValidMoves(player)
        
        if(validMoves == []):
            return None
        # If there are no valid moves, then return None.
        bestMove = None
        bestScore = None
        
        # If there are valid moves, then find the best move using MinMax algorithm.

        for move in validMoves:
            

            newBoard = ReversiBoard()
            newBoard = boardToGetBestMove.getCopy()
            # print(newBoard == boardToGetBestMove)
            # print(id(newBoard) == id(boardToGetBestMove))
            # print(id(newBoard.board) == id(boardToGetBestMove.board))
            newBoard.makeMove(player,move[0],move[1])
            # newBoard.print()
            # print("New Board: ")
            # boardToGetBestMove.print()

            # print("Move: ",move)
            score = MinMaxStrategy.minMax(newBoard,player,depth-1,False)
            # print("Score: ",score)


            if(bestScore == None or score > bestScore):
                bestScore = score
                bestMove = move
                

        return bestMove


    # This method is used to implement the MinMax algorithm.
    #Function Arguments:
    #board: The current state of the game.
    #player: The player for whom we are calculating the move W or  B.
    #depth: The depth of the game tree that we want to search.
    #maximizingPlayer: A boolean value that indicates whether we are calculating the move for the maximizing player or not.

    def minMax(boardtoGetMinMax : ReversiBoard ,player,depth,maximizingPlayer:bool):
        # print("Calculating best move for player: ",player," Depth: ",depth)
        
        # If the depth is 0 or the game is over, then we use the evaluation function to calculate the score.
        if(depth == 0 or boardtoGetMinMax.isGameOver() ):
            
            myeval =  MinMaxStrategy.evaluateBoard(boardtoGetMinMax,player)
            # print("Eval: ",myeval)
            return myeval

        if (boardtoGetMinMax.getValidMoves(player) == [] ):
            return MinMaxStrategy.minMax(boardtoGetMinMax , boardtoGetMinMax.getOpponent(player), depth, not maximizingPlayer)
            
            
        
        # If the current player is the maximizing player, then we want to maximize the score.
        if(maximizingPlayer):
            maxEval = -math.inf
            # print("Depth: ",depth)
            
            validMoves = boardtoGetMinMax.getValidMoves(player)
            # print("Valid Moves: ",validMoves)
            for move in validMoves:
                newBoard = boardtoGetMinMax.getCopy()
                newBoard.makeMove(player,move[0],move[1])
                eval = MinMaxStrategy.minMax(newBoard,player,depth-1,False)
                if(maxEval == None or eval > maxEval):
                    maxEval = eval
            return maxEval
        # If the current player is the minimizing player, then we want to minimize the score.
        else:
            minEval = math.inf
            validMoves = boardtoGetMinMax.getValidMoves(boardtoGetMinMax.getOpponent(player))
            # print("Valid Moves: ",validMoves)
            for move in validMoves:
                newBoard = boardtoGetMinMax.getCopy()
                newBoard.makeMove(boardtoGetMinMax.getOpponent(player),move[0],move[1])
                eval = MinMaxStrategy.minMax(newBoard,player,depth-1,True)
                if(minEval == None or eval < minEval):
                    minEval = eval
            return minEval