import pygame
import sys
import pygame_menu
from player import AIPlayer, HumanPlayer
from reversi2 import ReversiBoard

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

### Board Class ###


class Board:
    def __init__(self):
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
        self.board[3][3] = 'W'
        self.board[3][4] = 'B'
        self.board[4][3] = 'B'
        self.board[4][4] = 'W'

        self.white_count = 2
        self.black_count = 2


    def set_board(self, new_board):
        self.board = new_board

    def get_piece(self, row, col):
        return self.board[row][col]

    def set_piece(self, row, col, piece):
        self.board[row][col] = piece

    def get_valid_moves(self, color):
        # TODO: Implement the logic for getting a list of valid moves
        pass

    def count_pieces(self):
        # TODO: Implement the logic for counting the number of pieces of each color
        pass

    def is_game_over(self):
        # TODO: Implement the logic for determining if the game is over
        pass

    def get_white_count(self):
        self.white_count = 0
        for row in self.board:
            for col in row:
                if col == 'W':
                    self.white_count += 1
        return self.white_count

    def get_black_count(self):
        self.black_count = 0
        for row in self.board:
            for col in row:
                if col == 'B':
                    self.black_count += 1
        return self.black_count

    def set_valid_moves(self, valid_moves):
        for i in valid_moves:
            self.board[i[0]][i[1]] = 'V'

### Cell Class ###


class cell:
    def __init__(self, row, col, state):
        self.row = row
        self.col = col
        self.state = state
        self.color = (0, 144, 103)

    def draw(self, screen, square_size):
        x = self.col * square_size
        y = self.row * square_size
        # Drawing the square
        pygame.draw.rect(screen, self.color, (x, y, square_size, square_size))
        # Drawing the frame
        pygame.draw.rect(screen, (50, 50, 50),
                         (x, y, square_size, square_size), 1)
        if self.state == 'W':
            pygame.draw.circle(screen, WHITE, (x + square_size //
                               2, y + square_size // 2), square_size // 2 - 5)
            self.is_clickable = False
        elif self.state == 'B':
            pygame.draw.circle(screen, BLACK, (x + square_size //
                               2, y + square_size // 2), square_size // 2 - 5)
            self.is_clickable = False
        elif self.state == 'V':
            # draw hollow circle
            pygame.draw.circle(screen, BLACK, (x + square_size //
                               2, y + square_size // 2), square_size // 2 - 5, 1)


### GameUI Class ###
class GameUI:
    def __init__(self):
        # Initialize Pygame
        pygame.init()


        # Initialize reversi engine
        self.reversi = ReversiBoard()

        # Set up the display
        self.square_size = 60
        self.board_size = 8 * self.square_size
        self.statusbar_height = 2 * self.square_size
        self.statusbar_width = self.board_size
        self.screen_width = self.board_size
        self.screen_height = self.board_size + self.statusbar_height
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
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

    def statusbar_message(self, the_turn, white_score, black_score):
        font = pygame.font.Font(None, 36)
        message = font.render(
            f"{the_turn}'s turn | White: {white_score} | Black: {black_score}", True, BLACK)
        message_rect = message.get_rect(
            center=(self.statusbar_width // 2, self.statusbar_height // 2))
        self.statusbar.fill(pygame.Color('gray'))
        self.statusbar.blit(message, message_rect)

    # Setting the main menu
    def show_welcome_screen(self):
        menu = pygame_menu.Menu(
            'Welcome to othello',
            self.screen_width,
            self.screen_height,
            theme=pygame_menu.themes.THEME_SOLARIZED)
        # set menu font size

        # Add game mode selection
        menu.add.selector('Game Mode: ', [
            ('Player VS Player', 'VS Player'),
            ('Player VS AI', 'VS AI'),
            ('AI VS AI', 'AI VS AI')],
            onchange=self.set_game_mode,
            font_size=18)

        # Add difficulty selection
        menu.add.selector('Difficulty: ', [('Easy', 'easy'), ('Medium', 'medium'), ('Hard', 'hard')],
                          onchange=self.set_difficulty,
                          font_size=18)

        # Add start button
        menu.add.button('Start', self.start_game,
                        font_size=18)

        # Add quit button
        menu.add.button('Quit', pygame_menu.events.EXIT,
                        font_size=18)

        menu.mainloop(self.screen)

    def set_game_mode(self, value, game_mode):
        self.game_mode = game_mode
        print(self.game_mode)

    def set_difficulty(self, value, difficulty):
        self.difficulty = difficulty
        print(self.difficulty)

    # Drawing the board

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                new_cell = cell(row, col, self.board.get_piece(row, col))
                new_cell.draw(self.screen, self.square_size)

    # The main game loop
    def run(self):
        # game loop
        while True:
            # show the status bar
            self.screen.blit(
                self.statusbar, (0, self.screen_height - self.statusbar_height))
            self.statusbar_message(self.current_player, self.board.get_white_count(), self.board.get_black_count())
            
            # update the display
            pygame.display.flip()




            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    col = x // self.square_size
                    row = y // self.square_size
                    if 0 <= row < 8 and 0 <= col < 8:
                        if self.board.get_piece(row, col) == 'V':
                            self.board.board[row][col] = self.current_player


                            # sending the move to the reversi engine
                            self.reversi.makeMove(self.current_player, row, col)


                            pygame.display.flip()
                            if self.current_player == self.player1.get_color():
                                self.current_player = self.player2.get_color()
                            else:
                                self.current_player = self.player1.get_color()

                            
                            # Updating the whole board
                            self.board.set_board(self.reversi.getBoard())
                            self.board.set_valid_moves(self.reversi.getValidMoves(self.current_player))

                            self.draw_board()

                            
            self.clock.tick(60)

    def start(self):
        # Update the screen
        pygame.display.set_caption("Othello")
        self.show_welcome_screen()

    def start_game(self):
        self.draw_board()
        pygame.display.flip()
        # Run the game loop
        if self.game_mode == "VS AI":
            # Set up the AI player
            ai_player = AIPlayer('W')
            # Run the game in VS AI mode
            self.current_player = self.player1
            self.run()
        else:
            # Set up the human players
            self.player1 = HumanPlayer('B')
            self.player2 = HumanPlayer('W')
            # Run the game in VS Player mode
            self.current_player = self.player1.get_color()
            self.run()

        # Quit Pygame
        pygame.quit()


if __name__ == '__main__':
    game = GameUI()
    game.start()
