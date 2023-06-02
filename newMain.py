
from board import ReversiBoard
from MinMax import getBestMove
from alphaBetaPruning import getBestMove  as alphaBetaPruningBestMove 
from alphaBetaPruning import getBestMoveWithMT

# Create main to test the board class
from random import randint


import time

# if __name__ == '__main__':
    
#     #Test the MinMax algorithm by making computer play against itself.
#     gameStart = time.time()
#     Gameboard = ReversiBoard()
#     player = "W"
#     Gameboard.print()
#     while(not Gameboard.isGameOver()):
#         print("Here 1")
#         #calculate the time taken by the computer to make a move.
#         start = time.time()
#         move = getBestMove(Gameboard,player,4)
#         end = time.time()
#         print("Time taken by the computer to make a move: ",end-start)
        
#         if move != None:
            
#             Gameboard.makeMove(player,move[0],move[1])

#             Gameboard.print()

#             player = "W" if player == "B" else "B"
#         else:
            
#             player = "W" if player == "B" else "B"
#             continue

    
#     gameEnd = time.time()
#     print("Time taken by the game: ",gameEnd-gameStart)        
#     print("Winner is: ",Gameboard.getWinner())




if __name__ == '__main__':
    
    #Test the MinMax algorithm by making computer play against itself.
    gameStart = time.time()
    Gameboard = ReversiBoard()
    player = "W"
    Gameboard.print()
    while(not Gameboard.isGameOver()):
        print("Here 1")
        #calculate the time taken by the computer to make a move.
        start = time.time()
        move = getBestMoveWithMT(Gameboard,player,8)
        end = time.time()
        print("Time taken by the computer to make a move: ",end-start)
        
        if move != None:
            
            Gameboard.makeMove(player,move[0],move[1])

            Gameboard.print()

            player = "W" if player == "B" else "B"
        else:
            
            player = "W" if player == "B" else "B"
            continue

    
    gameEnd = time.time()
    print("Time taken by the game: ",gameEnd-gameStart)        
    print("Winner is: ",Gameboard.getWinner())



















# if __name__ == '__main__':
    
#     #Test the MinMax algorithm by making computer play against itself.
#     gameStart = time.time()
#     Gameboard = ReversiBoard()
#     player = "W"
#     Gameboard.print()
#     while(not Gameboard.isGameOver()):
#         print("Here 1")
#         #calculate the time taken by the computer to make a move.
#         start = time.time()
#         move = getBestMove(Gameboard,player,7)
#         end = time.time()
#         print("Time taken by the computer to make a move: ",end-start)
        
#         if move == None:
#             break

#         Gameboard.makeMove(player,move[0],move[1])

#         Gameboard.print()

#         player = "W" if player == "B" else "B"

    
#     gameEnd = time.time()
#     print("Time taken by the game: ",gameEnd-gameStart)        
#     print("Winner is: ",Gameboard.getWinner())


# if __name__ == '__main__':
    
#     #Test the MinMax algorithm by making computer play against itself.
#     gameStart = time.time()
#     Gameboard = ReversiBoard()
#     player = "W"
#     Gameboard.print()
#     while(not Gameboard.isGameOver()):
#         print("Here 1")
#         #calculate the time taken by the computer to make a move.
#         start = time.time()
#         move = alphaBetaPruningBestMove(Gameboard,player,10)
#         end = time.time()
#         print("Time taken by the computer to make a move: ",end-start)
        
#         if move == None:
#             player = "W" if player == "B" else "B"
#             break

#         Gameboard.makeMove(player,move[0],move[1])

#         Gameboard.print()

        

    
#     gameEnd = time.time()
#     print("Time taken by the game: ",gameEnd-gameStart)        
#     print("Winner is: ",Gameboard.getWinner())
