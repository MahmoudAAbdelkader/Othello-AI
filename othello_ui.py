import random
import pygame
import sys
import cell
from player import AIPlayer, HumanPlayer
from board import ReversiBoard
from main_menu import MainMenu
from front_board import Board

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

### GameUI Class ###
class GameUI:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Initialize reversi engine
        self.reversi = ReversiBoard()

        # Set up the display
        self.ASPECT_RATIO = (8,10)

        # Initial size of the board & game window
        self.screen_width = 480
        self.screen_height = int(self.screen_width / self.ASPECT_RATIO[0] * self.ASPECT_RATIO[1])
        self.square_size = self.screen_width // 8
        self.board_size = self.screen_width
        self.statusbar_height = 2 * self.square_size
        self.statusbar_width = self.screen_width
        

        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()

        # Set up the board
        self.board = Board()
        self.board.set_valid_moves(self.reversi.getValidMoves('B'))

        # Set up the status bar
        self.statusbar = pygame.Surface(
            (self.statusbar_width, self.statusbar_height))
        self.statusbar.fill(pygame.Color('gray'))

        # Default game mode
        self.game_mode = "VS Player"
        self.difficulty = "easy"

    def update_screen_dimensions(self, width, height):
        self.screen_width = width
        self.screen_height = int(self.screen_width / self.ASPECT_RATIO[0] * self.ASPECT_RATIO[1])
        self.square_size = self.screen_width // 8
        self.board_size = self.screen_width
        self.statusbar_height = 2 * self.square_size
        self.statusbar_width = self.screen_width

    
    def statusbar_message(self, the_turn = "W", white_score = 2, black_score = 2):
        names = {"W": "White", "B": "Black", "Draw": "Draw"}
        font = pygame.font.Font(None, int(23 * self.statusbar_height // 120 ))
        if not self.reversi.isGameOver():
            message = font.render(
                f"{names[the_turn]}'s turn | White: {white_score} | Black: {black_score}", True, BLACK)
        else:
            if self.reversi.getWinner() == "Draw":
                message = font.render(
                    f"Game Over!\n{names[self.reversi.getWinner()]} | White: {white_score} | Black: {black_score}", True, BLACK)
            else:
                message = font.render(
                    f"Game Over!\n{names[self.reversi.getWinner()]} Wins! | White: {white_score} | Black: {black_score}", True, BLACK)
            
        message_rect = message.get_rect(
            center=(self.statusbar_width // 2, self.statusbar_height // 2))
        self.statusbar.fill(pygame.Color('gray'))
        self.statusbar.blit(message, message_rect)

        # add a botton in most top left corner
        home_button = pygame.Rect(0, 0, self.square_size, self.square_size)
        pygame.draw.rect(self.statusbar, pygame.Color('green'), home_button)
        home_button_text = font.render("Home", True, BLACK)
        home_button_text_rect = home_button_text.get_rect(
            center=(home_button.width // 2, home_button.height // 2))
        # Add stroke to the rectangle
        pygame.draw.rect(self.statusbar, BLACK, home_button, 1)
        self.statusbar.blit(home_button_text, home_button_text_rect)

        restart_button = pygame.Rect(0, self.square_size, self.square_size, self.square_size)
        pygame.draw.rect(self.statusbar, pygame.Color('orange'), restart_button)
        restart_button_text = font.render("Restart", True, BLACK)
        restart_button_text_rect = restart_button_text.get_rect(
            center=((restart_button.width // 2), (restart_button.height // 2) + self.square_size))
        pygame.draw.rect(self.statusbar, BLACK, restart_button, 1)
        self.statusbar.blit(restart_button_text, restart_button_text_rect)

        # add a botton in most top right corner
        # pygame.draw.rect(self.statusbar, WHITE, (0, 0, self.statusbar_width, self.statusbar_height), 2)

    def set_game_mode(self, value, game_mode):
        self.game_mode = game_mode

    def set_difficulty(self, value, difficulty):
        self.difficulty = difficulty

    # Drawing the board
    def draw_board(self):
        for row in range(8):
            for col in range(8):
                new_cell = cell.Cell(row, col, self.board.get_piece(row, col))
                new_cell.draw(self.screen, self.square_size)

    def update_ingame_dimensions(self, event):
        # Update the window dimensions while maintaining the aspect ratio
        window_width = event.w
        window_width = round(window_width / 8) * 8
        window_height = int(window_width / self.ASPECT_RATIO[0] * self.ASPECT_RATIO[1])
        
        self.screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
        self.update_screen_dimensions(window_width, window_height)
        self.draw_board()
        self.statusbar = pygame.Surface(
            (self.statusbar_width, self.statusbar_height))
        self.statusbar.fill(pygame.Color('gray'))

    def handle_mouse_click_pvp(self, event):
        x, y = event.pos
        col = x // self.square_size
        row = y // self.square_size
        
        self.player1.setLambda(lambda x:(row,col))
        self.player2.setLambda(lambda x:(row,col))

        if not(0 <= row < 8 and 0 <= col < 8):
            print("Invalid move")
        elif self.board.get_piece(row, col) == 'V':
            Board.BOARD[row][col] = self.current_player
            # sending the move to the reversi engine
            #self.reversi.makeMove(self.current_player, row, col)
            self.playerMap[self.current_player].makeAMove()

        self.current_player = self.reversi.whoseTurn
        

        # Updating the whole board
        self.board.set_board(self.reversi.getBoard())
        if self.reversi.whoseTurn == 'W' or self.reversi.whoseTurn == 'B':
            self.board.set_valid_moves(self.reversi.getValidMoves(self.current_player))
        self.draw_board()
        # Update the display
        self.statusbar_message()
        pygame.display.flip()

    # def handle_mouse_click_pva(self, event):
    #     x, y = event.pos
    #     col = x // self.square_size
    #     row = y // self.square_size
    #     if not(0 <= row < 8 and 0 <= col < 8):
    #         print("Invalid move")
    #     elif self.board.get_piece(row, col) == 'V':
    #         Board.BOARD[row][col] = self.current_player
    #         # sending the move to the reversi engine
    #         self.reversi.makeMove(self.current_player, row, col)

    #     self.current_player = self.reversi.whoseTurn



    #     self.player1.makeAMove()

    #     self.current_player = self.reversi.whoseTurn

    #     # checking the buttons
    #     if (row == 8) and (col == 0):
    #         # home button
    #         self.start()

    #     if (row == 9) and (col == 0):
    #         # restart button
    #         self.start_game()

    #     # Updating the whole board
    #     self.board.set_board(self.reversi.getBoard())
    #     if self.reversi.whoseTurn == 'W' or self.reversi.whoseTurn == 'B':
    #         self.board.set_valid_moves(self.reversi.getValidMoves(self.current_player))
    #     self.draw_board()

    def dummy_ai_move(self):
        # update the display
        pygame.display.flip()

        self.current_player = self.reversi.whoseTurn

        self.playerMap[self.current_player].makeAMove()

        print("AI MOVE DONE")

        self.reversi.print()

        
        # print("AI is thinking...")

        
        # ai_valid_moves = self.reversi.getValidMoves(self.current_player)
        # if len(ai_valid_moves) > 0:
        #     move = random.choice(ai_valid_moves)
        #     self.reversi.makeMove(self.current_player, move[0], move[1])
        # self.current_player = self.reversi.whoseTurn
        

        #     # Updating the whole board
        self.board.set_board(self.reversi.getBoard())
        if self.reversi.whoseTurn == 'W' or self.reversi.whoseTurn == 'B':
            self.board.set_valid_moves(self.reversi.getValidMoves(self.reversi.whoseTurn))
        self.draw_board()

    # The main game loop for each game mode
    # mode: PVP, PVA, AVA
    # if the current player is AI, call the dummy_ai_move function THAT NEEDS TO BE CHANGED
    # if the current player is human, wait for the mouse click
    def run(self, mode):
        # game loop
        while True:
            # show the status bar
            self.screen.blit(
                self.statusbar, (0, self.screen_height - self.statusbar_height))
            self.statusbar_message(self.current_player, self.reversi.getScore('W'), self.reversi.getScore('B'))
            
            # update the display
            pygame.display.flip()

            # Update the current player
            self.current_player = self.reversi.whoseTurn
            
            # If it's AI's turn, call the dummy_ai_move function
            if not(self.reversi.isGameOver()):
                if (mode == "PVA" and self.current_player == "W") or mode == "AVA":
                    
                    self.dummy_ai_move() 
                    
                    # pygame.display.flip()
                    #self.playerMap[self.reversi.getWhoseTurn()].makeAMove()
                    continue

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.VIDEORESIZE:
                    self.update_ingame_dimensions(event)
                
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # checking the buttons
                    x, y = event.pos
                    col = x // self.square_size
                    row = y // self.square_size
                    if (row == 8) and (col == 0):
                        # home button
                        self.start()

                    if (row == 9) and (col == 0):
                        # restart button
                        self.start_game()
                    if mode == 'PVP':
                        self.handle_mouse_click_pvp(event)
                        continue
                    elif mode == 'PVA':
                        if self.current_player == "B":
                            self.handle_mouse_click_pvp(event)
                            continue
                    elif mode == 'AVA':
                        pass
            
              
            self.clock.tick(60)

    # the main AVA game loop
    def run_ava(self):
        pass

    def start(self):
        # Reset the game mode to default
        self.game_mode = "VS Player"
        self.difficulty = "easy"
        # Update the screen
        pygame.display.set_caption("Othello")
        main_menu = MainMenu(self)
        main_menu.show_welcome_screen()

    def create_player(self, color, player_type):
        """Factory method to create a player object based on the given color and player type."""
        if player_type == 'human':
            return HumanPlayer(color, self.reversi)
            
        elif player_type == 'ai':
            return AIPlayer(color, self.reversi, self.difficulty)

    def start_game(self):
        """Starts the game with the selected game mode and players."""
        self.reversi.restart()
        self.board.reset_board()
        self.board.set_valid_moves(self.reversi.getValidMoves('B'))
        self.draw_board()
        pygame.display.flip()

        # Set current player to Black
        self.current_player = 'B'

        gameMode = ' '
        # Create players based on game mode using the factory method
        if self.game_mode == 'VS Player':
            self.player1 = self.create_player('B', 'human')
            self.player2 = self.create_player('W', 'human')
            gameMode = 'PVP'
            
        elif self.game_mode == 'VS AI':
            self.player1 = self.create_player('B', 'human')
            self.player2 = self.create_player('W', 'ai')
            gameMode = 'PVA'
            
        else:
            self.player1 = self.create_player('B', 'ai')
            self.player2 = self.create_player('W', 'ai')
            gameMode = 'AVA'
        
        self.playerMap = {'B': self.player1, 'W': self.player2}
        self.run(gameMode)

        # Quit Pygame
        pygame.quit()


if __name__ == '__main__':
    game = GameUI()
    game.start()
