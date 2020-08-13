from .transitions import *
from objects.stages import *

main_logger, event_logger, rect_logger, display_logger, sprite_logger = settings.create_loggers(__name__)
main_logger.setLevel(settings.logging.INFO)
event_logger.setLevel(settings.logging.INFO)
rect_logger.setLevel(settings.logging.INFO)
display_logger.setLevel(settings.logging.INFO)
sprite_logger.setLevel(settings.logging.INFO)


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

        self.item_boxes[0].items.append(ItemBox('Datas'))
        self.item_boxes[0].items.append(ItemBox('Buttons', side='Horizontal'))
        self.add_button('Buttons', 'cancel', 'Cancel and go back', [CloseRenderEvents(), CloseRenderEvents()], xratio = 0.423, yratio=0.145, font_size=36)
        self.add_button('Buttons', 'save', 'Learn skills and continue', [CloseRenderEvents(), StartMenuEvents()], xratio = 0.423, yratio=0.145, font_size=36)
        self.search_itembox('Datas')
        self.targetbox.items.append(ItemBox('PowerUps', side='Horizontal'))
        self.targetbox.items.append(ItemBox('Skills'))
        self.add_button('PowerUps', 'powerList_title', 'POWER UP', xratio = 0.145, yratio=0.090, font_size=24)
        self.search_itembox('PowerUps')
        self.targetbox.items.append(ItemBox('Collected'))
        self.add_button('Collected', 'collected_PU', f'power ups : {hero.power_up}', xratio=0.145, yratio=0.090, font_size=24)
        self.targetbox.items.append(ItemBox('Fire'))
        self.targetbox.items.append(ItemBox('Light'))
        self.targetbox.items.append(ItemBox('Ice'))
        self.targetbox.items.append(ItemBox('Earth'))
        self.add_button('Fire', 'fire', str(hero.fire), xratio = 0.145, yratio=0.090)
        self.add_button('Light', 'light', str(hero.light), xratio = 0.145, yratio=0.090)
        self.add_button('Ice', 'ice', str(hero.ice), xratio = 0.145, yratio=0.090)
        self.add_button('Earth', 'earth', str(hero.earth), xratio = 0.145, yratio=0.090)
        n=1
        for item_box in self.item_boxes[0].items[0].items[0].items[2:]:
            item_box.items.append(ItemBox(item_box.name+'_add', side='Horizontal'))
            self.add_button(item_box.name+'_add', '+', '+', [PowerUpEvents(sender=n, action='+')], xratio=0.055, yratio=0.055, font_size=24)
            self.add_button(item_box.name+'_add', '-', '-', [PowerUpEvents(sender=n, action='-')], xratio=0.055, yratio=0.055, font_size=24)
        self.search_itembox('Skills')
        self.targetbox.items.append(ItemBox('Row1', side='Horizontal'))
        self.targetbox.items.append(ItemBox('Row2', side='Horizontal'))
        self.targetbox.items.append(ItemBox('Row3', side='Horizontal'))
        a = 0.241
        b = 0.090
        self.add_button('Row1', 'level', f'Level : {str(hero.level)}', xratio=0.236, yratio=b, font_size=42)
        self.search_itembox('Row1')
        self.targetbox.items.append(ItemBox('Row1_Col1', side='Horizontal'))
        self.add_button('Row1_Col1', 'kills', f'Kills : {str(hero.kills)}', xratio=0.145, yratio=0.090, font_size=28)
        self.add_button('Row1_Col1', 'stage_score', f'Stage_Score : {str(hero.stage_score)}', xratio=0.328, yratio=0.055, font_size=32)
        self.add_button('Row1_Col1', 'total_score', f'Total_Score : {str(hero.total_score)}', xratio=0.328, yratio=0.055, font_size=32)
        self.add_button('Row2', 'max_speed', f'Max Speed : {str(hero.max_speed)}', xratio=a, yratio=b, font_size=28)
        self.add_button('Row2', 'speed', f'Accel : {str(hero.level)}', xratio=a, yratio=b, font_size=28)
        self.add_button('Row2', 'max_jump', f'Max Jump : {str(hero.max_jump)}', xratio=a, yratio=b, font_size=28)
        self.add_button('Row2', 'health', f'Health : {str(hero.health)}', xratio=a, yratio=b, font_size=28)
        self.add_button('Row3', 'ammo_speed', f'Ammo Speed : {str(hero.ammo_speed)}', xratio=a, yratio=b, font_size=28)
        self.add_button('Row3', 'attack_rate', f'Attack Rate : {str(hero.attack_rate)}', xratio=a, yratio=b, font_size=28)
        self.add_button('Row3', 'max_ammo', f'Max Ammo : {str(hero.max_ammo)}', xratio=a, yratio=b, font_size=28)
        self.add_button('Row3', 'damage', f'Damage : {str(hero.damage)}', xratio=a, yratio=b, font_size=28)
        self.add_button('Row3', 'shield', f'Shield : {str(hero.shield)}', xratio=a, yratio=b, font_size=28)

        self.create_pannels()

        self.search_itembox('Skills')
        self.targetbox.createPannel(centerx=settings.SCREEN_SIZE[0] / 2, centery=settings.SCREEN_SIZE[1] / 2, space_between=4.61)
        self.targetbox.rect.x = 0
        self.targetbox.rect.y = 0
        self.search_itembox('Datas')
        self.targetbox.createPannel(centerx= settings.SCREEN_SIZE[0] / 2, centery = settings.SCREEN_SIZE[1] / 2, space_between=5.55)
        self.targetbox.rect.x = 0
        self.targetbox.rect.y = 0
        self.search_itembox('Buttons')
        self.targetbox.createPannel(centerx= settings.SCREEN_SIZE[0] / 2, centery = settings.SCREEN_SIZE[1] / 2, space_between=9.02)
        self.targetbox.rect.x = self.size[0] / 2
        self.targetbox.rect.y = 0
        self.item_boxes[0].createPannel(centerx= settings.SCREEN_SIZE[0] / 2, centery = settings.SCREEN_SIZE[1] / 2, space_between=9.02)
        self.item_boxes[0].rect.x = 0
        self.item_boxes[0].rect.y = 0.090*settings.SCREEN_SIZE[1]

        self.update()
        display_logger.success(f'HeroMenu init : OK')

    def update(self):
        def search_in(itembox):
            for item in itembox.items:
                if type(item) == ItemBox:
                    item.update()
                    rect_logger.debug(f"item {item.name}'s rect = {item.rect}")
                    search_in(item)
        for box in self.item_boxes:
            search_in(box)
            box.update()
            rect_logger.debug(f"item {box.name}'s rect = {box.rect}")
            self.menu_body.image.blit(box.image, box.rect)
            rect_logger.debug(f"menubody's rect = {self.menu_body.rect}")
            self.image.blit(self.background, (0, 0))
            self.image.blit(self.menu_body.image, self.menu_body.rect)






        






