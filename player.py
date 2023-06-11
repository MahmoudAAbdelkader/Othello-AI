 ########################################################################################################################################
 # Project : Othello AI Player
 #########################################################################################################################################
 # Module: Player
 # File: player.py
 # Authors: Hussam Wael
 # Date: 2022-6-10
 # Description: This file contains the player classes which are responsible for the player's moves and the AI's moves
 ########################################################################################################################################

# Importing the necessary modules
from board import ReversiBoard
from MinMax import MinMaxStrategy
from alphaBetaPruning import AlphaBetaPruningStrategy

############################################################################################################################################################################
#                                                    Player Class                                                                                                          #
############################################################################################################################################################################

class Player:
    #This is the base class for both types of players, which are the human player and the AI player

    # The constructor:
    # Sets the player's color and the board the player is playing on
    # If the color is not valid, it raises a ValueError
    # If the board is not in its initial state, it raises a ValueError
    def __init__(self, color:str, board : ReversiBoard):
       
       if(color not in ["W", "B"]): 
          raise ValueError("Invalid color")
       
       if(board.hasGameBegun()): 
          raise ValueError("Cannot play on a board that has already begun")
 
       self.color = color
       self.board = board #The board is set by reference to avoid copying the board and to allow the player to make changes to the board
       
       self.lambdaFunc = None
    
    # The method that returns the player's color
    def get_color(self):
        return self.color
    
    # The method that sets the player's color
    def set_color(self, color:str):
        if(color not in ["W", "B"]): 
          raise ValueError("Invalid color")
        self.color = color


    #This method serves as a base for the makeAMove method in the subclasses
    def makeAMove(self):
       pass

    def setLambda(self, lambdaFunc):
        self.lambdaFunc = lambdaFunc
############################################################################################################################################################################
#                                                 Human Player Class                                                                                                       #
############################################################################################################################################################################

class HumanPlayer(Player):
    # This class is responsible for the human player's moves
    
    # The constructor:
    # Sets the player's color and the board the player is playing on
    # If the color is not valid, it raises a ValueError
    # If the board is not in its initial state, it raises a ValueError
    def __init__(self, color:str, board : ReversiBoard):
        super().__init__(color, board) # Calling the base class constructor
        # self.lambdaFunc = None
    
    # This method is responsible for the human player's moves
    # If the move is invalid, it raises a ValueError
    # If the move is valid, it makes the move and returns the board
    def makeAMove(self):
        
       row,col = self.lambdaFunc(self)

       if(not self.board.isValidMove(self.color, row, col)):
          raise ValueError("Invalid move!")
       
       self.board.makeMove(self.color, row, col)

       return self.board

    # def setLambda(self, lambdaFunc):
    #     self.lambdaFunc = lambdaFunc
    
############################################################################################################################################################################
#                                                 AI Player Class                                                                                                       #
############################################################################################################################################################################

class AIPlayer(Player):
    # This class is responsible for the AI player's moves
    
    # The constructor:
    # Sets the player's color and the board the player is playing on
    # Sets the AI's difficulty
    # If the color is not valid, it raises a ValueError
    # If the board is not in its initial state, it raises a ValueError
    # If the difficulty is not valid, it raises a ValueError
    def __init__(self, color:str, board : ReversiBoard , difficulty:str = "easy"):
        super().__init__(color, board) # Calling the base class constructor
        
        #FIXME: Add the AI's strategy object here

        # Checking if the difficulty is valid
        if(difficulty.lower() not in ["easy", "medium", "hard"]):
           raise ValueError("Invalid difficulty")
        
        # Setting the difficulty
        self.difficulty = difficulty

    # This method sets the AI's difficulty
    # If the difficulty is not valid, it raises a ValueError
    def setDifficulty(self, difficulty:str):

        if(difficulty.lower() not in ["easy", "medium", "hard"]):
           raise ValueError("Invalid difficulty")
        
        self.difficulty = difficulty

    # This method returns the AI's difficulty
    def getDifficulty(self):
        return self.difficulty
    
    # This method is responsible for the AI player's moves
    # The AI strategy object is called here to find the best move and make it
    # This method is not supposed to take any arguments, so it raises a TypeError if any arguments are passed
    
    def makeAMove(self):
       
        #FIXME: Call the AI strategy object here
        validMoves = self.board.getValidMoves(self.color)

        difficultyToDepthMap = {"easy": 1, "medium": 3, "hard": 5}

        import time

        minimum_execution_time = 1

        # Get the current time
        start_time = time.time()
    
        bestMove = MinMaxStrategy.getBestMove(self.board, self.color, difficultyToDepthMap[self.difficulty])
        print("difficulty = ", self.difficulty, "depth = ", difficultyToDepthMap[self.difficulty], "bestMove = ", bestMove, "validMoves = ", validMoves, "color = ", self.color, "board = ", self.board, sep = "\n")
        end_time = time.time()

        # Calculate the execution time
        execution_time = end_time - start_time
        
        # If the execution time is less than the minimum execution time, sleep for the difference
        if(execution_time < minimum_execution_time):
            time.sleep(minimum_execution_time - execution_time)
        
        self.board.makeMove(self.color, bestMove[0], bestMove[1])



############################################################################################################################################################################
#                                                This is a simple test for the players classes                                                                             # 
############################################################################################################################################################################

import random

myBoard = ReversiBoard()

myBoard.setTheFirstPlayer("B")

myBoard.print()
print()


#Creating the players
player1 = HumanPlayer("B", myBoard)
player2 = AIPlayer("W", myBoard , "medium")

#Setting the human player's lambda function
getCoordinates = lambda player: random.choice(myBoard.getValidMoves(player.get_color()))

player1.setLambda(getCoordinates)


#Testing the players' colors
print(player1.get_color())
print(player2.get_color())
print()

#Players Map:
playersMap = {"B":player1, "W":player2}

listOfTurns = []
num = lambda x: 1 if x == "B" else 0
while(not myBoard.isGameOver()):
   
   whoseTurn = myBoard.getWhoseTurn()

   print("It's " + whoseTurn + "'s turn")
   listOfTurns.append(num(whoseTurn))
   playersMap[whoseTurn].makeAMove()

   myBoard.print()
   
   print()


print("Game Over!")
print("The winner is " + myBoard.getWinner())

   
print("Here is the list of turns: " , "\n", listOfTurns)
    
    
   
       