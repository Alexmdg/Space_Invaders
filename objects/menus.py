from .transitions import *
from objects.stages import *

main_logger, event_logger, rect_logger, display_logger, sprite_logger = settings.create_loggers(__name__)
main_logger.setLevel(settings.logging.DEBUG)
event_logger.setLevel(settings.logging.DEBUG)
rect_logger.setLevel(settings.logging.DEBUG)
display_logger.setLevel(settings.logging.DEBUG)
sprite_logger.setLevel(settings.logging.DEBUG)


class MainMenu():
    def __init__(self):
        self.is_running = True
        self.buttons= []
        self.body = Pannel(settings.SCREEN_SIZE)
        self.background = pygame.transform.scale(settings.IMAGE_LOADER.city_background, settings.SCREEN_SIZE)
        self.body.image.blit(self.background, (0, 0))
        self.menu_bg = Pannel((settings.SCREEN_SIZE[0] * 0.618, settings.SCREEN_SIZE[1] * 0.618))
        self.menu_bg.rect.centerx = settings.SCREEN_SIZE[0] / 2
        self.menu_bg.rect.centery = settings.SCREEN_SIZE[1] / 2
        self.menu_bg.image.fill(settings.PURPLE)
        self.start_button = Button((0.8 * self.menu_bg.size[0],
                                    0.1 * self.menu_bg.size[1]),
                                    'Start Game',
                                    24,
                                    MenuEventsStartGame())
        self.start_button.body.rect.centerx = settings.SCREEN_SIZE[0] / 2
        self.start_button.body.rect.centery = self.menu_bg.rect.y +  1.618 * (self.menu_bg.rect[3] / 5)
        self.buttons.append(self.start_button)
        self.quit_button = Button((0.8 * self.menu_bg.size[0],
                                   0.1 * self.menu_bg.size[1]),
                                   'Quit',
                                   24,
                                   MenuEventsQuitGame())
        self.quit_button.body.rect.centerx = settings.SCREEN_SIZE[0] / 2
        self.quit_button.body.rect.centery = self.menu_bg.rect.y +  3.82 * (self.menu_bg.rect[3] / 5)
        self.buttons.append(self.quit_button)
        self.clock = pygame.time.Clock()
        self.count = 3
        self.time = 0
        self.body.image.blit(self.menu_bg.image, self.menu_bg.rect)
        self.body.image.blit(self.start_button.body.image, self.start_button.body.rect)
        self.body.image.blit(self.quit_button.body.image, self.quit_button.body.rect)
    def update(self):
        pass

    def on_click(self, button):
        button.clicked()
        event_logger.debug('button clicked')
        self.is_running = False

# class PauseMenu():
#     def __init__(self):
#         self.is_running = True
#         self.body = Pannel(settings.SCREEN_SIZE)
#         self.background = pygame.transform.scale(settings.IMAGE_LOADER.city_background, settings.SCREEN_SIZE)
#         self.body.image.blit(self.background, (0, 0))
#         self.buttons = VerticalButtons((settings.SCREEN_SIZE[0] * 0.382, settings.SCREEN_SIZE[1] * 0.618))
#         self.buttons.body.rect.center = self.body.rect.center
#         self.buttons.add_button((0.8 * self.buttons.body.size[0],
#                                  0.1 * self.buttons.body.size[1]),
#                                 'Resume Game',
#                                 24,
#                                 PauseMenuEvents(0, 1, 1, 1))
#         self.buttons.add_button((0.8 * self.buttons.body.image.get_size()[0],
#                                  0.1 * self.buttons.body.image.get_size()[1]),
#                                 'quit',
#                                 24,
#                                 MainMenuEvents(0, 1, 1, 1))
#
#         self.body.image.blit(self.buttons.body.image, ((self.body.rect.centerx - self.buttons.body.size[0]/2),
#                                                        (self.body.rect.centery - self.buttons.body.size[1]/2)))

    # def on_click(self, button):
    #     button.clicked()
    #     event_logger.debug('button clicked')
    #     self.is_running = False

