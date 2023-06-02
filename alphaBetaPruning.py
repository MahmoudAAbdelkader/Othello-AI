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
import math

# This method is used to evaluate the board for the given player.
# The evaluation function is the difference between the number of pieces of the given player and the number of pieces of the opponent.
#function Arguments:
#board: The current state of the game.
#player: The player for whom we are calculating the score W or B.

def evaluateBoard(board: ReversiBoard,player):
    if(player == "W"):
        return len(board.getLocations("W")) - len(board.getLocations("B"))
    else:
        return len(board.getLocations("B")) - len(board.getLocations("W"))
    
# This method is used to get the best move for the given player using alphabeta pruning algorithm.
def getBestMove(boardToGetBestMove : ReversiBoard,player,depth):
    
    if (boardToGetBestMove.isGameOver()):
        return None

    # Get all the valid moves for the given player.
    validMoves = boardToGetBestMove.getValidMoves(player)
    
    if(validMoves == []):
        return None
    # If there are no valid moves, then return None.
    bestMove = None
    bestScore = None
    
    # If there are valid moves, then find the best move using alphabeta pruning algorithm.

    for move in validMoves:
        

        newBoard = ReversiBoard()
        newBoard = boardToGetBestMove.getCopy()

        newBoard.makeMove(player,move[0],move[1])


        # print("Move: ",move)
        score = alphaBetaPruning(newBoard,player,depth-1,False,-math.inf,math.inf)
        # print("Score: ",score)
        if(bestScore == None or score > bestScore):
            bestScore = score
            bestMove = move
    return bestMove


# This method is used to implement the alphabeta pruning algorithm.
# function Arguments:
# board: The current state of the game.
# player: The player for whom we are calculating the score W or B.
# depth: The depth of the game tree.
# isMaximizingPlayer: A boolean value that indicates whether the current node is a maximizing node or not.
# alpha: The best value that the maximizing player can guarantee at that level or above.
# beta: The best value that the minimizing player can guarantee at that level or above.
def alphaBetaPruning(board :ReversiBoard,player,depth,isMaximizingPlayer,alpha,beta):
    
    # If the depth is 0 or the game is over, then return the score.
    if(depth == 0 or board.isGameOver()):
        return evaluateBoard(board,player)
    
    # Get all the valid moves for the given player.
    validMoves = board.getValidMoves(player)
    
    # If there are no valid moves, then return the score.
    if(validMoves == []):
        return alphaBetaPruning(board , board.getOpponent(player) , depth , not isMaximizingPlayer , alpha , beta)
    
    # If the current node is a maximizing node.
    if(isMaximizingPlayer):
        bestScore = -math.inf
        for move in validMoves:
            newBoard = ReversiBoard()
            newBoard = board.getCopy()
            newBoard.makeMove(player,move[0],move[1])
            score = alphaBetaPruning(newBoard,player,depth-1,False,alpha,beta)
            bestScore = max(bestScore,score)
            alpha = max(alpha,score)
            if(beta <= alpha):
                break
        return bestScore
    # If the current node is a minimizing node.
    else:
        bestScore = math.inf
        for move in validMoves:
            newBoard = ReversiBoard()
            newBoard = board.getCopy()
            newBoard.makeMove(player,move[0],move[1])
            score = alphaBetaPruning(newBoard,player,depth-1,True,alpha,beta)
            bestScore = min(bestScore,score)
            beta = min(beta,score)
            if(beta <= alpha):
                break
        return bestScore
    
    
    
import concurrent.futures

def getBestMoveWithMT(boardToGetBestMove: ReversiBoard, player, depth):
    
    if boardToGetBestMove.isGameOver():
        return None

    # Get all the valid moves for the given player.
    validMoves = boardToGetBestMove.getValidMoves(player)
    
    if not validMoves:
        return None

    bestMove = None
    bestScore = None

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []

        for move in validMoves:
            newBoard = ReversiBoard()
            newBoard = boardToGetBestMove.getCopy()
            newBoard.makeMove(player, move[0], move[1])

            # Submit each move computation as a separate thread
            futures.append(executor.submit(alphaBetaPruning, newBoard, player, depth - 1, False, -1000000, 1000000))

        # Retrieve the results from the completed threads
        for move, future in zip(validMoves, futures):
            score = future.result()

            if bestScore is None or score > bestScore:
                bestScore = score
                bestMove = move

    return bestMove

    
    