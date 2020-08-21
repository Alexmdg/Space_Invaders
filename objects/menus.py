from .transitions import *
from objects.stages import *
from prelog import CheckLog
from prelog import LEVELS as poglevel

log = CheckLog()
log.display.setLevel(settings.logging.ERROR)

class MainMenuScene(Menu):
    def __init__(self):
        with log.bugCheck(log.display, 'MainMenuScene init'):
            super().__init__()
            self.add_button('mainBox', 'startGame', 'New Game', [CloseRenderEvents(),
                                                                 GetSetEvents(action='get', context='StartGame'),
                                                                 StartStageEvents()])
            self.add_button('mainBox', 'gameContinue', 'Continue Game', [CloseRenderEvents(),
                                                                         GetSetEvents(action="get"),
                                                                         StartStageEvents()])
            self.add_button('mainBox', 'quit', 'Quit Game', [QuitGameEvents()])
            self.item_boxes[0].createPannel(self.menu_body.size[0] / 2, self.menu_body.size[1] / 2, space_between=5.57)
            self.update()

class PauseMenuScene(Menu):
    def __init__(self):
        with log.bugCheck(log.display, 'PauseMenuScene init'):
            super().__init__()
            self.close_stage = False
            self.add_button('mainBox', 'gameResume', 'Resume Game', [CloseRenderEvents()])
            self.add_button('mainBox', 'levelRestart', 'Restart Level', [CloseRenderEvents(),
                                                                        StartStageEvents(sender='PauseMenuScene')])
            self.add_button('mainBox', 'gameRestart', 'New Game', [CloseRenderEvents(sender='PauseMenuScene'),
                                                                 GetSetEvents(action='set', context="RestartGame"),
                                                                 GetSetEvents(action='get'),
                                                                 StartStageEvents(sender='PauseMenuScene')])
            self.add_button('mainBox', 'quit', 'Quit Game', [QuitGameEvents()])
            self.item_boxes[0].createPannel(self.menu_body.size[0] / 2, self.menu_body.size[1] / 2, space_between=5.57)
            self.update()

class HeroMenuScene(Menu):
    def __init__(self, hero):
        with log.bugCheck(log.display, 'HerMenuScene Init'):
            super().__init__(ratiox=0.786, ratioy=0.786)
            self.hero = hero
            self.item_boxes[0].items.append(ItemBox('Datas'))
            self.item_boxes[0].items.append(ItemBox('Buttons', side='Horizontal'))
            self.add_button('Buttons', 'cancel', 'Cancel and go back',
                            [CloseRenderEvents(sender='HeroMenuNext'),
                             StartStageEvents()],
                            xratio=0.423, yratio=0.145, font_size=36)
            self.add_button('Buttons', 'save', 'Learn skills and continue',
                            [GetSetEvents(action='set', context='ContinueGame'),
                             CloseRenderEvents(sender='HeroMenuBack'),
                             GetSetEvents(action='get'),
                             StartStageEvents()],
                            xratio=0.423, yratio=0.145, font_size=36)
            self.search_itembox('Datas')
            self.targetbox.items.append(ItemBox('PowerUps', side='Horizontal'))
            self.targetbox.items.append(ItemBox('Skills'))
            self.add_button('PowerUps', 'powerList_title', 'POWER UP', xratio=0.145, yratio=0.090, font_size=24)
            self.search_itembox('PowerUps')
            self.targetbox.items.append(ItemBox('Collected'))
            self.add_button('Collected', 'collected_PU', f'power ups : {self.hero.power_up}',
                            xratio=0.145, yratio=0.090, font_size=24)
            self.targetbox.items.append(ItemBox('Fire'))
            self.targetbox.items.append(ItemBox('Light'))
            self.targetbox.items.append(ItemBox('Ice'))
            self.targetbox.items.append(ItemBox('Earth'))
            self.add_button('Fire', 'fire', str(self.hero.fire), xratio=0.145, yratio=0.090)
            self.add_button('Light', 'light', str(self.hero.light), xratio=0.145, yratio=0.090)
            self.add_button('Ice', 'ice', str(self.hero.ice), xratio=0.145, yratio=0.090)
            self.add_button('Earth', 'earth', str(self.hero.earth), xratio=0.145, yratio=0.090)
            for item_box in self.item_boxes[0].items[0].items[0].items[2:]:
                item_box.items.append(ItemBox(item_box.name+'_add', side='Horizontal'))
                self.add_button(item_box.name+'_add', '+', '+', [PowerUpEvents(sender=item_box.name, action='+')], xratio=0.055, yratio=0.055, font_size=24)
                self.add_button(item_box.name+'_add', '-', '-', [PowerUpEvents(sender=item_box.name, action='-')], xratio=0.055, yratio=0.055, font_size=24)
            self.search_itembox('Skills')
            self.targetbox.items.append(ItemBox('Row1', side='Horizontal'))
            self.targetbox.items.append(ItemBox('Row2', side='Horizontal'))
            self.targetbox.items.append(ItemBox('Row3', side='Horizontal'))
            a = 0.241
            b = 0.090
            self.add_button('Row1', 'level', f'Level : {str(self.hero.level)}', xratio=0.236, yratio=b, font_size=42)
            self.search_itembox('Row1')
            self.targetbox.items.append(ItemBox('Row1_Col1', side='Horizontal'))
            self.add_button('Row1_Col1', 'kills', f'Kills : {str(self.hero.kills)}', xratio=0.145, yratio=0.090, font_size=28)
            self.add_button('Row1_Col1', 'stage_score', f'Stage_Score : {str(self.hero.stage_score)}', xratio=0.328, yratio=0.055, font_size=32)
            self.add_button('Row1_Col1', 'total_score', f'Total_Score : {str(self.hero.total_score)}', xratio=0.328, yratio=0.055, font_size=32)
            self.add_button('Row2', 'max_speed', f'Max Speed : {str(self.hero.max_speed)}', xratio=a, yratio=b, font_size=28)
            self.add_button('Row2', 'speed', f'Accel : {str(self.hero.level)}', xratio=a, yratio=b, font_size=28)
            self.add_button('Row2', 'max_jump', f'Max Jump : {str(self.hero.max_jump)}', xratio=a, yratio=b, font_size=28)
            self.add_button('Row2', 'health', f'Health : {str(self.hero.health)}', xratio=a, yratio=b, font_size=28)
            self.add_button('Row3', 'ammo_speed', f'Ammo Speed : + {str(10 * self.hero.ammo_speed)}%', xratio=a, yratio=b, font_size=28)
            self.add_button('Row3', 'attack_rate', f'Attack Rate : + {str(10 * round(self.hero.attack_rate, 1))}%', xratio=a, yratio=b, font_size=28)
            self.add_button('Row3', 'max_ammo', f'Max Ammo : {str(self.hero.max_ammo)}', xratio=a, yratio=b, font_size=28)
            self.add_button('Row3', 'damage', f'Damage : {str(self.hero.damage)}', xratio=a, yratio=b, font_size=28)
            self.add_button('Row3', 'shield', f'Shield : {str(self.hero.shield)}', xratio=a, yratio=b, font_size=28)

            self.create_pannels()

            self.search_itembox('Skills')
            self.targetbox.createPannel(centerx=settings.SCREEN_SIZE[0] / 2, centery=settings.SCREEN_SIZE[1] / 2, space_between=4.61)
            self.targetbox.rect.x = 0
            self.targetbox.rect.y = 0
            self.search_itembox('Datas')
            self.targetbox.createPannel(centerx=settings.SCREEN_SIZE[0] / 2, centery = settings.SCREEN_SIZE[1] / 2, space_between=5.55)
            self.targetbox.rect.x = 0
            self.targetbox.rect.y = 0
            self.search_itembox('Buttons')
            self.targetbox.createPannel(centerx=settings.SCREEN_SIZE[0] / 2, centery = settings.SCREEN_SIZE[1] / 2, space_between=9.02)
            self.targetbox.rect.x = self.size[0] / 2
            self.targetbox.rect.y = 0
            self.item_boxes[0].createPannel(centerx=settings.SCREEN_SIZE[0] / 2, centery = settings.SCREEN_SIZE[1] / 2, space_between=9.02)
            self.item_boxes[0].rect.x = 0
            self.item_boxes[0].rect.y = 0.090*settings.SCREEN_SIZE[1]

            self.update()

    def update(self):
        def search_in(itembox):
            with log.bugCheck(log.display, 'Search_in'):
                for item in itembox.items:
                    if type(item) == ItemBox:
                        item.update()
                        log.display.spc_dbg(f"item {item.name}'s rect = {item.rect}")
                        search_in(item)
        with log.bugCheck(log.display, 'Update'):
            for box in self.item_boxes:
                search_in(box)
                box.update()
                log.display.spc_dbg(f"item {box.name}'s rect = {box.rect}")
                self.menu_body.image.blit(box.image, box.rect)
                log.display.spc_dbg(f"menubody's rect = {self.menu_body.rect}")
                self.image.blit(self.background, (0, 0))
                self.image.blit(self.menu_body.image, self.menu_body.rect)

    def update_all_infos(self):
        self.__init__(self.hero)








        






