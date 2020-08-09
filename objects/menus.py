from .transitions import *
from objects.stages import *

main_logger, event_logger, rect_logger, display_logger, sprite_logger = settings.create_loggers(__name__)
main_logger.setLevel(settings.logging.DEBUG)
event_logger.setLevel(settings.logging.DEBUG)
rect_logger.setLevel(settings.logging.DEBUG)
display_logger.setLevel(settings.logging.DEBUG)
sprite_logger.setLevel(settings.logging.DEBUG)


class MainMenu(Menu):
    def __init__(self):
        super().__init__()
        self.start_button = Button((0.618 * self.menu_bg.size[0],
                                    0.161 * self.menu_bg.size[1]),
                                    'Start Game',
                                    48,
                                    MenuEventsStartGame())
        self.start_button.body.rect.centerx = settings.SCREEN_SIZE[0] / 2
        self.start_button.body.rect.centery = self.menu_bg.rect.y + 1.618 * (self.menu_bg.rect[3] / 5)
        self.buttons.append(self.start_button)
        self.quit_button = Button((0.618 * self.menu_bg.size[0],
                                   0.161 * self.menu_bg.size[1]),
                                   'Quit',
                                   48,
                                   MenuEventsQuitGame())
        self.quit_button.body.rect.centerx = settings.SCREEN_SIZE[0] / 2
        self.quit_button.body.rect.centery = self.menu_bg.rect.y + 3.382 * (self.menu_bg.rect[3] / 5)
        self.buttons.append(self.quit_button)
        for button in self.buttons:
            self.body.image.blit(button.body.image, button.body.rect)


class PauseMenu(Menu):
    def __init__(self):
        super().__init__()
        self.resume_button = Button((0.618 * self.menu_bg.size[0],
                                    0.161 * self.menu_bg.size[1]),
                                   'Resume Game',
                                   48,
                                   MenuEventsResumeGame())
        self.resume_button.body.rect.centerx = settings.SCREEN_SIZE[0] / 2
        self.resume_button.body.rect.centery = self.menu_bg.rect.y + 1.618 * (self.menu_bg.rect[3] / 5)
        self.buttons.append(self.resume_button)
        self.quit_button = Button((0.618 * self.menu_bg.size[0],
                                   0.161 * self.menu_bg.size[1]),
                                  'Quit',
                                  48,
                                  MenuEventsQuitGame())
        self.quit_button.body.rect.centerx = settings.SCREEN_SIZE[0] / 2
        self.quit_button.body.rect.centery = self.menu_bg.rect.y + 3.382 * (self.menu_bg.rect[3] / 5)
        self.buttons.append(self.quit_button)
        for button in self.buttons:
            self.body.image.blit(button.body.image, button.body.rect)


class NextStageMenu(Menu):
    pass
