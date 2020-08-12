from .transitions import *
from objects.stages import *

main_logger, event_logger, rect_logger, display_logger, sprite_logger = settings.create_loggers(__name__)
main_logger.setLevel(settings.logging.DEBUG)
event_logger.setLevel(settings.logging.DEBUG)
rect_logger.setLevel(settings.logging.DEBUG)
display_logger.setLevel(settings.logging.DEBUG)
sprite_logger.setLevel(settings.logging.DEBUG)


class MainMenuScene(Menu):
    def __init__(self):
        display_logger.success(f'MainMenuScene init : OK')
        super().__init__()
        self.add_button('mainBox', 'startGame', 'New Game', [CloseMenuEvents(), StartStageEvent()])
        self.add_button('mainBox', 'gameContinue', 'Continue Game', [CloseMenuEvents(), StartStageEvent(level=0)])
        self.add_button('mainBox', 'quit', 'Quit Game', [QuitGameEvents()])
        self.item_boxes[0].createPannel(self.menu_body.size[0] / 2, self.menu_body.size[1] / 2, space_between=5.57)
        self.update()

class PauseMenuScene(Menu):
    def __init__(self):
        display_logger.success(f'PauseMenuScene init : OK')
        super().__init__()
        self.close_stage = False
        self.add_button('mainBox', 'gameResume', 'Resume Game', [CloseMenuEvents(sender='PauseMenu')])
        self.add_button('mainBox', 'gameRestart', 'Restart Level', [CloseMenuEvents(sender='PauseMenu'),
                                                                    CloseStageEvents(sender='PauseMenu'),
                                                                    StartStageEvent(sender='PauseMenu', level=0)])
        self.add_button('mainBox', 'startGame', 'New Game', [CloseMenuEvents(sender='PauseMenu'),
                                                             CloseStageEvents(sender='PauseMenu'),
                                                             GetSetEvents(type='set', sender='PauseMenu',
                                                                          context="RestartGame"),
                                                             StartStageEvent(sender='PauseMenu', level=1)])
        self.add_button('mainBox', 'quit', 'Quit Game', [QuitGameEvents()])
        self.item_boxes[0].createPannel(self.menu_body.size[0] / 2, self.menu_body.size[1] / 2, space_between=5.57)
        self.update()

class HeroMenu(Menu):
    def __init__(self, hero):
        display_logger.success(f'HeroStatsScene init : OK')
        super().__init__(ratiox=0.786, ratioy=0.618)
        self.item_boxes[0].side = 'Horizontal'
        self.item_boxes.append(ItemBox('powerUps'))
        self.item_boxes.append(ItemBox('skills'))
        self.item_boxes.append(ItemBox('Fire'))
        self.item_boxes.append(ItemBox('Light'))
        self.item_boxes.append(ItemBox('Ice'))
        self.item_boxes.append(ItemBox('Earth'))
        self.item_boxes.append(ItemBox('Buttons'))

        for item_box in self.item_boxes[3:7]:
            self.item_boxes.items.append(ItemBox('buttons'))

            self.add_button(item_box.name, 'level', hero.datas[item_box.name])
            self.add_button(item_box.name, 'add+', '+')
            self.add_button(item_box.name, 'add-', '-')

        self.add_button('mainBox', 'cancel', 'Cancel and go back', [CloseMenuEvents(), StartMenuEvent()])
        self.add_button('mainBox', 'save', 'Learn skills and continue', [CloseMenuEvents(), StartMenuEvent()])
        self.add_button()

