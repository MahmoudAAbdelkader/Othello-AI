import pygame_menu

### Main Menu Class ###
class MainMenu:
    def __init__(self,game_object):
        self.game_object = game_object
        self.menu = None
        self.difficulty_selector = None

    def show_welcome_screen(self):
        self.menu = pygame_menu.Menu(
            'Welcome to Othello!',
            self.game_object.screen_width,
            self.game_object.screen_height,
            theme=pygame_menu.themes.THEME_SOLARIZED)
        # set menu font size
        self.font_size = 28 * self.game_object.screen_width // 480

        # Add game mode selection
        self.menu.add.selector('Game Mode: ', [
            ('Player VS AI', 'VS AI'),
            ('Player VS Player', 'VS Player'),
            ('AI VS AI', 'AI VS AI')],
            onchange = self.on_game_mode_selected, font_size=self.font_size)

        # Add difficulty selection
        self.difficulty_selector = self.menu.add.selector('Difficulty: ', [('Easy', 'easy'), ('Medium', 'medium'), ('Hard', 'hard')],
                          onchange=self.game_object.set_difficulty,
                          font_size=self.font_size)

        # Add start button
        self.menu.add.button('Start', self.game_object.start_game,
                        font_size=self.font_size)

        # Add quit button
        self.menu.add.button('Quit', pygame_menu.events.EXIT,
                        font_size=self.font_size)

        self.menu.mainloop(self.game_object.screen)

    def on_game_mode_selected(self, _, value):
        
        # set game mode
        self.game_object.set_game_mode(value)
        
        # hide difficulty selector if game mode is VS Player
        if value == 'VS Player':
            self.difficulty_selector.hide()
        else:
            self.difficulty_selector.show()
        
        

