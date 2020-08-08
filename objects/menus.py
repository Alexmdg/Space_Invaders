from objects.menuObjects.menuParts import *
from objects.menuObjects.menuEvents import *

main_logger, event_logger, rect_logger, display_logger = settings.create_loggers(__name__)
main_logger.setLevel(settings.logging.DEBUG)
event_logger.setLevel(settings.logging.DEBUG)
rect_logger.setLevel(settings.logging.DEBUG)
display_logger.setLevel(settings.logging.DEBUG)

class MainMenu():
    def __init__(self):
        self.is_running = True
        self.body = Pannel(settings.SCREEN_SIZE)
        self.background = pygame.transform.scale(settings.IMAGE_LOADER.city_background, settings.SCREEN_SIZE)
        self.body.image.blit(self.background, (0, 0))
        self.buttons = VerticalButtons((settings.SCREEN_SIZE[0] * 0.382, settings.SCREEN_SIZE[1] * 0.618))
        self.buttons.body.rect.center = self.body.rect.center
        self.buttons.add_button((0.8 * self.buttons.body.size[0],
                                 0.1 * self.buttons.body.size[1]),
                                'Start Game',
                                MainMenuEvents(1, 1))
        self.buttons.add_button((0.8 * self.buttons.body.image.get_size()[0],
                                 0.1 * self.buttons.body.image.get_size()[1]),
                                'quit',
                                MainMenuEvents(1, 1))

        self.body.image.blit(self.buttons.body.image, ((self.body.rect.centerx - self.buttons.body.size[0]/2),
                                                       (self.body.rect.centery - self.buttons.body.size[1]/2)))

    def on_click(self, button):
        button.clicked()
        event_logger.debug('button clicked')
        self.is_running = False