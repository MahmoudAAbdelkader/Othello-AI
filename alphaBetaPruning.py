##############################################################################################################################
# Project Name :  Othello                                                                                                    #   
# File Name    :  alphaBetaPruning.py                                                                                        #
# Author       :  Hisham Yakan                                                                                               #
# Description  :  This file contains the class that implements the MinMax algorithm. The class inherits from the Strategy    #
#                interface.                                                                                                  #
# Date         :  05/25/2023                                                                                                 #
#                                                                                                                            #                                 
##############################################################################################################################




# We need to implement the alphabeta pruning algorithm to determine the best move for the computer.
# The alphabeta pruning algorithm is a recursive algorithm that is used to choose an optimal move for a player assuming that the opponent is also playing optimally.
# The algorithm searches the game tree starting from the current state of the game and explores all the way down to the terminal states (i.e. states where the game is over).

# The algorithm then evaluates the terminal states using a heuristic function and propagates the values back up the tree.

# The algorithm uses alpha and beta values to prune the branches of the game tree that cannot possibly yield a better move for the player.
# If the node is a maximizing node, then we update the alpha value.
# If the node is a minimizing node, then we update the beta value.
# If alpha >= beta, then we prune the branch.
# The following code is used to test the alphabeta pruning algorithm.

from board import ReversiBoard
from strategy import Strategy
import math
import heuristics


maximixingPlayer = None

class AlphaBetaPruningStrategy(Strategy):
    
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
    

    def __evaluateBoard(board: ReversiBoard,player):

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

        
    ##############################################################################################################################
        
        
    ##############################################################################################################################    
    # Method Name: getBestMove
    
    # Purpose: This method is used to get the best move for the given player using alphabeta pruning algorithm.
    
    # Method Description:    
    # This method is used to get the best move for the given player using alphabeta pruning algorithm.
    
    #function Arguments:
    #boardToGetBestMove: The current state of the game.
    #player: The player for whom we are calculating the score W or B.
    #depth: The depth of the game tree.
    
    ##############################################################################################################################    
    
    
    def getBestMove(boardToGetBestMove : ReversiBoard,player,depth):
        
        global maximixingPlayer
        # print(f"Maximizing Player = {maximixingPlayer}")
        maximixingPlayer = player
        # print(f"Maximizing Player = {maximixingPlayer}")
        # super().getBestMove(boardToGetBestMove,player,depth)
        
        # If the game is over, then return None.
        if (boardToGetBestMove.isGameOver()):
            return None

        # Get all the valid moves for the given player.
        validMoves = boardToGetBestMove.getValidMoves(player)
        
        # If there are no valid moves, then return None.
        if(validMoves == []):
            return None
        # If there are no valid moves, then return None.
        bestMove = None
        bestScore = None
        
        # If there are valid moves, then find the best move using alphabeta pruning algorithm.
        
        # For each valid move, create a new board and make the move on the new board.
        for move in validMoves:
            
            # Create a new board
            newBoard = ReversiBoard()
            newBoard = boardToGetBestMove.getCopy()

            # Make the move on the new board.
            newBoard.makeMove(player,move[0],move[1])
            

            # print("*****************************************************************************************************")
            # print("Player is : ", player)
            # print("Player opponent is : ", newBoard.getOpponent(player))
            # print(newBoard)
            # print(boardToGetBestMove)
            # # check if the object is deep copied or not
            # print(id(newBoard)== id(boardToGetBestMove))
            # print(id(newBoard.whoseTurn)== id(boardToGetBestMove.whoseTurn))
            # print("*****************************************************************************************************")
            
            
            # Call the alphabeta pruning algorithm to get the score for the move (The heuristics ).               
            score = AlphaBetaPruningStrategy.alphaBetaPruning(newBoard,boardToGetBestMove.getOpponent(player),depth-1,False,-math.inf,math.inf)
            
            # If the score is better than the best score, then update the best score and the best move.
            if(bestScore == None or score > bestScore):
                bestScore = score
                bestMove = move
        
        # Return the best move.        
        return bestMove
    
    ##############################################################################################################################
    
    

    ##############################################################################################################################    
    # Method Name: alphaBetaPruning
    
    # Purpose: This method is used to implement the alphabeta pruning algorithm.
    
    # Method Description:
    # This method is used to implement the alphabeta pruning algorithm to be used to determine the best move.
    
    # function Arguments:
    # board: The current state of the game.
    # player: The player for whom we are calculating the score W or B.
    # depth: The depth of the game tree.
    # isMaximizingPlayer: A boolean value that indicates whether the current node is a maximizing node or not.
    # alpha: The best value that the maximizing player can guarantee at that level or above.
    # beta: The best value that the minimizing player can guarantee at that level or above.
    
    ##############################################################################################################################
    
    def alphaBetaPruning(board :ReversiBoard,player,depth,isMaximizingPlayer,alpha,beta):
        
        # If the depth is 0 or the game is over, then return the score.
        if(depth == 0 or board.isGameOver()):
            return AlphaBetaPruningStrategy.__evaluateBoard(board,player)
        
        # Get all the valid moves for the given player.
        validMoves = board.getValidMoves(player)
        
        # If there are no valid moves, then return the score.
        if(validMoves == []):
            return AlphaBetaPruningStrategy.alphaBetaPruning(board , board.getOpponent(player) , depth , not isMaximizingPlayer , alpha , beta)
        
        # If the current node is a maximizing node.
        if(isMaximizingPlayer):
            
            # Initialize the best score of alpha to -infinity.
            bestScore = -math.inf
            
            # Loop through all the valid moves.
            for move in validMoves:
                
                # Create a new board.
                newBoard = ReversiBoard()
                newBoard = board.getCopy()
                
                # Make the move on the new board.
                newBoard.makeMove(player,move[0],move[1])
                
                # Call the alphabeta pruning algorithm to get the score for the move (The heuristics ).
                score = AlphaBetaPruningStrategy.alphaBetaPruning(newBoard,board.getOpponent(player),depth-1,False,alpha,beta)
                
                # Update the best score.
                bestScore = max(bestScore,score)
                
                # Update the alpha value.
                alpha = max(alpha,score)
                
                # If alpha >= beta, then prune the branch.
                if(beta <= alpha):
                    break
             
            # Return the best score.    
            return bestScore
        
        
        # If the current node is a minimizing node.
        else:
            # Initialize the best score of beta to infinity.
            bestScore = math.inf
            
            # Loop through all the valid moves.
            for move in validMoves:
                
                # Create a new board.
                newBoard = ReversiBoard()
                newBoard = board.getCopy()
                
                # Make the move on the new board.
                newBoard.makeMove(player,move[0],move[1])
                
                # Call the alphabeta pruning algorithm to get the score for the move (The heuristics ).
                score = AlphaBetaPruningStrategy.alphaBetaPruning(newBoard,board.getOpponent(player),depth-1,True,alpha,beta)
                
                # Update the best score to the minimum of the current best score and the score.
                bestScore = min(bestScore,score)
                
                # Update the beta value to the minimum of the current beta value and the score.
                beta = min(beta,score)
                
                # If alpha >= beta, then prune the branch.
                if(beta <= alpha):
                    break
                
            # Return the best score.
            return bestScore
        
        
        
        
    
    ##############################################################################################################################