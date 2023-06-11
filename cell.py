import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Cell:
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
