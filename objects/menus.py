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
        super().__init__(ratiox=0.786, ratioy=0.786)

        self.item_boxes[0].items.append(ItemBox('Buttons', side='Horizontal'))
        self.item_boxes[0].items.append(ItemBox('Datas', side='Horizontal'))
        self.add_button('Button', 'cancel', 'Cancel and go back', [CloseRenderEvents(), CloseRenderEvents()], xratio = 0.23, yratio=0.161, font_size=36)
        self.add_button('Button', 'save', 'Learn skills and continue', [CloseRenderEvents(), StartMenuEvents()], xratio = 0.23, yratio=0.161, font_size=36)
        self.search_itembox('Datas')
        self.targetbox.items.append(ItemBox('PowerUps'))
        self.targetbox.items.append(ItemBox('Skills'))
        self.add_button('PowerUps', 'powerList_title', 'POWER UP', xratio = 0.145, yratio=0.090, font_size=24)
        self.search_itembox('PowerUps')
        self.targetbox.items.append(ItemBox('Collected'))
        self.add_button('Collected', 'collected_PU', str(hero.power_up), xratio=0.145, yratio=0.090, font_size=24)
        self.targetbox.items.append(ItemBox('Fire'))
        self.targetbox.items.append(ItemBox('Light'))
        self.targetbox.items.append(ItemBox('Ice'))
        self.targetbox.items.append(ItemBox('Earth'))
        self.add_button('Fire', 'fire', str(hero.fire), xratio = 0.23, yratio=0.090)
        self.add_button('Light', 'light', str(hero.light), xratio = 0.23, yratio=0.090)
        self.add_button('Ice', 'ice', str(hero.ice), xratio = 0.23, yratio=0.090)
        self.add_button('Earth', 'earth', str(hero.earth), xratio = 0.23, yratio=0.090)
        for item_box in self.item_boxes[0].items[1].items[0].items[2:]:
            item_box.items.append(ItemBox(item_box.name+'_add', side='Horizontal'))
            self.add_button(item_box.name+'_add', '+', '+', [CloseRenderEvents(), CloseRenderEvents()], xratio=0.090, yratio=0.090, font_size=24)
            self.add_button(item_box.name+'_add', '-', '-', [CloseRenderEvents(), CloseRenderEvents()], xratio=0.090, yratio=0.090, font_size=24)
        self.search_itembox('Skills')
        self.targetbox.items.append(ItemBox('Row1', side='Horizontal'))
        self.targetbox.items.append(ItemBox('Row2', side='Horizontal'))
        self.targetbox.items.append(ItemBox('Row3', side='Horizontal'))
        a = 0.145
        b = 0.145
        self.add_button('Row1', 'level', f'level : {str(hero.level)}', xratio=0.236, yratio=b, font_size=36)
        self.search_itembox('Row1')
        self.targetbox.items.append(ItemBox('Row1_Col1', side='Horizontal'))
        self.add_button('Row1_Col1', 'kills', f'kills : {str(hero.kills)}', xratio=0.161, yratio=b, font_size=18)
        self.add_button('Row1_Col1', 'stage_score', f'stage_score : {str(hero.stage_score)}', xratio=0.161, yratio=b, font_size=18)
        self.add_button('Row1_Col1', 'total_score', f'total_score : {str(hero.total_score)}', xratio=0.161, yratio=b, font_size=18)
        self.add_button('Row2', 'max_speed', f'max_speed : {str(hero.max_speed)}', xratio=a, yratio=b, font_size=18)
        self.add_button('Row2', 'speed', f'Accel : {str(hero.level)}', xratio=a, yratio=b, font_size=18)
        self.add_button('Row2', 'max_jump', f'max_jump : {str(hero.max_jump)}', xratio=a, yratio=b, font_size=18)
        self.add_button('Row2', 'health', f'health : {str(hero.health)}', xratio=a, yratio=b, font_size=18)
        self.add_button('Row3', 'ammo_speed', f'ammo_speed : {str(hero.ammo_speed)}', xratio=a, yratio=b, font_size=18)
        self.add_button('Row3', 'attack_rate', f'attack_rate : {str(hero.attack_rate)}', xratio=a, yratio=b, font_size=18)
        self.add_button('Row3', 'max_ammo', f'max_ammo : {str(hero.max_ammo)}', xratio=a, yratio=b, font_size=18)
        self.add_button('Row3', 'damage', f'damage : {str(hero.damage)}', xratio=a, yratio=b, font_size=18)
        self.add_button('Row3', 'shield', f'shield : {str(hero.shield)}', xratio=a, yratio=b, font_size=18)

        self.create_pannels()

        # self.search_itembox('Row1_Col1')
        # self.targetbox.createPannel(space_between=0, transparent=True,
        #              bg_color=settings.Purple(0), bttn_color=settings.Purple(0))
        # self.search_itembox('Row1')
        # self.targetbox.createPannel(space_between=0, transparent=True,
        #                             bg_color=settings.Purple(0), bttn_color=settings.Purple(0))
        # self.search_itembox('Row2')
        # self.targetbox.createPannel(space_between=0, transparent=True,
        #                             bg_color=settings.Purple(0), bttn_color=settings.Purple(0))
        # self.search_itembox('Row3')
        # self.targetbox.createPannel(space_between=0, transparent=True,
        #                             bg_color=settings.Purple(0), bttn_color=settings.Purple(0))
        # self.search_itembox('Skills')
        # self.targetbox.createPannel(space_between=0, transparent=True,
        #                             bg_color=settings.Purple(0), bttn_color=settings.Purple(0))
        # self.search_itembox('Earth_add')
        # self.targetbox.createPannel(space_between=0, transparent=True,
        #                             bg_color=settings.Purple(0), bttn_color=settings.Purple(0))
        # self.search_itembox('Ice_add')
        # self.targetbox.createPannel(space_between=0, transparent=True,
        #                             bg_color=settings.Purple(0), bttn_color=settings.Purple(0))
        # self.search_itembox('Light_add')
        # self.targetbox.createPannel(space_between=0, transparent=True,
        #                             bg_color=settings.Purple(0), bttn_color=settings.Purple(0))
        # self.search_itembox('Fire_add')
        # self.targetbox.createPannel(space_between=0, transparent=True,
        #                             bg_color=settings.Purple(0), bttn_color=settings.Purple(0))
        # self.search_itembox('Earth')
        # self.targetbox.createPannel(space_between=0, transparent=True,
        #                             bg_color=settings.Purple(0), bttn_color=settings.Purple(0))
        # self.search_itembox('Ice')
        # self.targetbox.createPannel(space_between=0, transparent=True,
        #                             bg_color=settings.Purple(0), bttn_color=settings.Purple(0))
        # self.search_itembox('Light')
        # self.targetbox.createPannel(space_between=0, transparent=True,
        #                             bg_color=settings.Purple(0), bttn_color=settings.Purple(0))
        # self.search_itembox('Fire')
        # self.targetbox.createPannel(space_between=0, transparent=True,
        #                             bg_color=settings.Purple(0), bttn_color=settings.Purple(0))
        # self.search_itembox('Collected')
        # self.targetbox.createPannel(space_between=0, transparent=True,
        #                             bg_color=settings.Purple(0), bttn_color=settings.Purple(0))
        # self.search_itembox('PowerUps')
        # self.targetbox.createPannel(space_between=0, transparent=True,
        #                             bg_color=settings.Purple(0), bttn_color=settings.Purple(0))
        # self.search_itembox('Datas')
        # self.targetbox.createPannel(space_between=0, transparent=True,
        #                             bg_color=settings.Purple(0), bttn_color=settings.Purple(0))
        # self.search_itembox('Buttons')
        # self.targetbox.createPannel(space_between=0, transparent=True,
        #                             bg_color=settings.Purple(0), bttn_color=settings.Purple(0))
        # self.search_itembox('mainBox')
        # self.targetbox.createPannel(space_between=0, transparent=True,
        #                             bg_color=settings.Purple(0), bttn_color=settings.Purple(0))
        #
        # self.menu_body.image.blit(self.targetbox.image, self.targetbox.rect)



        # self.search_itembox('Datas')
        # self.targetbox.rect.centery = 0.145 * self.size[1]/2
        # self.targetbox.rect.centery = self.size[0]/2
        # self.image.blit(self.targetbox.image, self.targetbox.rect)
        # self.search_itembox('Buttons')
        # self.targetbox.rect.centery = 0.786 * self.size[1]/2
        # self.targetbox.rect.centery = self.size[0]/2
        # self.image.blit(self.targetbox.image, self.targetbox.rect)

        display_logger.success(f'HeroMenu init : OK')



        






