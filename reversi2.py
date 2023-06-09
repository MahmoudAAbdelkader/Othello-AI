 ########################################################################################################################################
 # Project : Othello AI Player
 #########################################################################################################################################
 # Module: Reversi Board
 # File: board.py
 # Authors: Hussam Wael
 # Date: 2022-5-10
 # Description: This file contains the ReversiBoard class which is used to represent the board of the game.
 ########################################################################################################################################

from copy import deepcopy

# The ReversiBoard class is used to represent the board of the game.
class ReversiBoard:
    # The board is represented as a 2D array of characters.
    # Each character represents a cell in the board.
    # The characters can be " ", "W", or "B".
    # " " means the cell is empty.
    # "W" means the cell is occupied by a white piece.
    # "B" means the cell is occupied by a black piece.
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
    # The constructor of the ReversiBoard class.      
    def __init__(self):
        pass 

    # This private method is used to check if the given cell is inside the board or not.
    def __isInside(self,row : int ,col: int):
        return row >= 0 and row <= 7 and col >= 0 and col <= 7
    
    # This method is used to determine whether a cell has neighbours or not.
    def __hasNeighbours(self,row : int ,col: int):
        directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
        for direction in directions:
            newRow = row + direction[0]
            newCol = col + direction[1]
            if(self.__isInside(newRow,newCol) and self.board[newRow][newCol] != " "):
                return self.board[row][col] == ' '
        return False
    
    # This method is used to print the board on the console.
    def print(self):
        for row in self.board:
            print(row)

    # This method is used to reset the board to its initial state.
    def restart(self):
        self.board = [
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", "W", "B", " ", " ", " "],
    [" ", " ", " ", "B", "W", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "]
]
    # This method is used as a getter to the 2D array that represents the board.
    def getBoard(self):
        return deepcopy(self.board) # We use deepcopy to return a copy of the board, not a reference to it.
    
    # This method returns a list of tuples that represent the locations of the cells that are occupied by the given color.
    #Possible Colors: "W" or "B", otherwise it will throw an error.
    def getLocations(self,color : str):

        if(color not in ["W","B"]):
            raise Exception("Invalid Color! Color must be either 'W' or 'B'")
        
        locations = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == color:
                    locations.append([i,j])
        return locations
    
    # This method is used to check if the given move is valid or not.
    # Possible Colors: "W" or "B", otherwise it will throw an error.
    def isValidMove(self, color : str, row : int, col : int):

        #Check if the color is valid
        if(color not in ["W","B"]):
            raise Exception("Invalid Color! Color must be either 'W' or 'B'")
        
        #Check if the row and col are valid
        if(not self.__isInside(row,col)):
            raise Exception("Invalid row or col! row and col must be between 0 and 7")

        #Check if the cell is not empty
        if(self.board[row][col] != " "):
            return False

        #Check if the cell has neighbours
        if(not self.__hasNeighbours(row,col)):
            return False
        
        #Check if the move is valid in any direction
        directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]

        for direction in directions:
            newRow = row + direction[0]
            newCol = col + direction[1]

            otherColor = "W" if color == "B" else "B"

            #Looping until we find a cell with the same color as the given color
            while(self.__isInside(newRow,newCol) and self.board[newRow][newCol] == otherColor):
                newRow += direction[0]
                newCol += direction[1]
                if(self.__isInside(newRow,newCol) and self.board[newRow][newCol] == color):
                    return True
        
        #If we didn't find a cell with the same color as the given color, then the move is invalid. 
        return False

    #This method returns the valid moves for the given color.
    #Possible Colors: "W" or "B", otherwise it will throw an error.
    def getValidMoves(self, color : str):
        
        #Check if the color is valid
        if(color not in ["W","B"]):
            raise Exception("Invalid Color! Color must be either 'W' or 'B'")

        #Looping through the board to find the valid moves
        validMoves = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if(self.isValidMove(color,i,j)):
                    validMoves.append([i,j])
        return validMoves
    
    #This method is used to make a move on the board.
    def makeMove(self, color : str, row : int, col : int):

        #Check if the move is valid
        if(not self.isValidMove(color,row,col)):
            raise Exception("Invalid Move! The given move is not valid.")
        
        #Making the move
        self.board[row][col] = color
        directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]

        for direction in directions:
            newRow = row + direction[0]
            newCol = col + direction[1]

            otherColor = "W" if color == "B" else "B"

            #Looping until we find a cell with the same color as the given color
            while(self.__isInside(newRow,newCol) and self.board[newRow][newCol] == otherColor):
            
                newRow += direction[0]
                newCol += direction[1]
               
                if(self.__isInside(newRow,newCol) and self.board[newRow][newCol] == color): #If we found a cell with the same color as the given color
                    #Looping back to the original cell and flipping the pieces
                    while(newRow != row or newCol != col):
                        self.board[newRow][newCol] = color
                        newRow -= direction[0]
                        newCol -= direction[1]
                    break
                #Note: We cannot flip the pieces while looping forward because we don't know if we will find a cell with the same color as the given color or not.
                
        
    # This method is used to check the board is full or not.
    def isGameOver(self):
        WhiteValidMoves = self.getValidMoves("W")
        BlackValidMoves = self.getValidMoves("B")
        return len(WhiteValidMoves) == 0 and len(BlackValidMoves) == 0
    
    # This method is used to get the winner of the game.
    def getWinner(self):
        if(not self.isGameOver()):
            raise Exception("Game is not over yet!")
        else:
            WhiteLocations = self.getLocations("W")
            BlackLocations = self.getLocations("B")
            if(len(WhiteLocations) > len(BlackLocations)):
                return "W"
            elif(len(WhiteLocations) < len(BlackLocations)):
                return "B"
            else:
                return "Draw"
            
############################################################################################################################################################################
#                                   The following code is used to test the board class.                                                                                    #
############################################################################################################################################################################

