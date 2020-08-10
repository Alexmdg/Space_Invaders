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
        self.add_button('mainBox', 'startGame', 'New Game', MenuEventsStartGame())
        self.add_button('mainBox', 'gameContinue', 'Continue Game', MenuEventsContinueGame())
        self.add_button('mainBox', 'quit', 'Quit Game', MenuEventsQuitGame())
        self.item_boxes[0].createPannel(self.menu_body.size[0] / 2, self.menu_body.size[1] / 2, space_between=5.57)
        self.update()

class PauseMenu(Menu):
    def __init__(self):
        super().__init__()
        self.add_button('mainBox', 'gameResume', 'Resume Game', MenuEventsResumeGame())
        self.add_button('mainBox', 'gameRestart', 'Restart Level', MenuEventsRestartLevel())
        self.add_button('mainBox', 'startGame', 'New Game', MenuEventsStartGame())
        self.add_button('mainBox', 'quit', 'Quit Game', MenuEventsQuitGame())
        self.item_boxes[0].createPannel(self.menu_body.size[0] / 2, self.menu_body.size[1] / 2, space_between=23.61)
        self.update()

class NextStageMenu(Menu):
    pass
