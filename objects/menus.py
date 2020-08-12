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
        self.add_button('mainBox', 'startGame', 'New Game', [CloseRenderEvents(), StartStageEvents()])
        self.add_button('mainBox', 'gameContinue', 'Continue Game', [CloseRenderEvents(), StartStageEvents(level=0)])
        self.add_button('mainBox', 'quit', 'Quit Game', [QuitGameEvents()])
        self.item_boxes[0].createPannel(self.menu_body.size[0] / 2, self.menu_body.size[1] / 2, space_between=5.57)
        self.update()

class PauseMenuScene(Menu):
    def __init__(self):
        display_logger.success(f'PauseMenuScene init : OK')
        super().__init__()
        self.close_stage = False
        self.add_button('mainBox', 'gameResume', 'Resume Game', [CloseRenderEvents(sender='PauseMenu')])
        self.add_button('mainBox', 'levelRestart', 'Restart Level', [CloseRenderEvents(sender='PauseMenu'),
                                                                    CloseRenderEvents(sender='PauseMenu'),
                                                                    StartStageEvents(sender='PauseMenu', level=0)])
        self.add_button('mainBox', 'gameRestart', 'New Game', [CloseRenderEvents(sender='PauseMenu'),
                                                             GetSetEvents(type='set', sender='PauseMenu',
                                                                          context="RestartGame"),
                                                             StartStageEvents(sender='PauseMenu', level=1)])
        self.add_button('mainBox', 'quit', 'Quit Game', [QuitGameEvents()])
        self.item_boxes[0].createPannel(self.menu_body.size[0] / 2, self.menu_body.size[1] / 2, space_between=5.57)
        self.update()

class HeroMenu(Menu):
    def __init__(self, hero):
        display_logger.success(f'HeroStatsScene init : OK')
        super().__init__(ratiox=0.786, ratioy=0.618)
        self.item_boxes[0].side = 'Horizontal'

        self.item_boxes.items.append(ItemBox('Buttons'))
        self.add_button('Buttons', 'cancel', 'Cancel and go back', [CloseMenuEvents(), StartMenuEvent()])
        self.add_button('Buttons', 'save', 'Learn skills and continue', [CloseMenuEvents(), StartMenuEvent()])

        self.item_boxes[0].items.append(ItemBox('PowerUps'))
        self.add_button('PowerUps', 'powerList_title', 'POWER UP')
        self.item_boxes[0][0].items.append(ItemBox('Collected'))
        self.item_boxes[0][0].items.append(ItemBox('Fire'))
        self.item_boxes[0][0].items.append(ItemBox('Light'))
        self.item_boxes[0][0].items.append(ItemBox('Ice'))
        self.item_boxes[0][0].items.append(ItemBox('Earth'))
        self.add_button('Fire', 'powerUp_title', hero.fire)
        self.add_button('light', 'powerUp_title', hero.light)
        self.add_button('fire', 'powerUp_title', hero.ice)
        self.add_button('earth', 'powerUp_title', hero.earth)
        for item_box in self.item_boxes[0][0].items[1:]:
            item_box.items.append(ItemBox(item_box.name+'_add', side='Horizontal'))
            self.add_button(item_box.name+'_add', '+', '+', [CloseMenuEvents(), StartMenuEvent()])
            self.add_button(item_box.name+'_add', '-', '-', [CloseMenuEvents(), StartMenuEvent()])

        self.item_boxes[0].items.append(ItemBox('Skills'))

        






