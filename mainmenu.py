import pygame_menu

### Main Menu Class ###
class MainMenu:
    def __init__(self,game_object):
        self.game_object = game_object

    def show_welcome_screen(self):
        menu = pygame_menu.Menu(
            'Welcome to othello',
            self.game_object.screen_width,
            self.game_object.screen_height,
            theme=pygame_menu.themes.THEME_SOLARIZED)
        # set menu font size

        # Add game mode selection
        menu.add.selector('Game Mode: ', [
            ('Player VS Player', 'VS Player'),
            ('Player VS AI', 'VS AI'),
            ('AI VS AI', 'AI VS AI')],
            onchange=self.game_object.set_game_mode,
            font_size=18)

        # Add difficulty selection
        menu.add.selector('Difficulty: ', [('Easy', 'easy'), ('Medium', 'medium'), ('Hard', 'hard')],
                          onchange=self.game_object.set_difficulty,
                          font_size=18)

        # Add start button
        menu.add.button('Start', self.game_object.start_game,
                        font_size=18)

        # Add quit button
        menu.add.button('Quit', pygame_menu.events.EXIT,
                        font_size=18)

        menu.mainloop(self.game_object.screen)

