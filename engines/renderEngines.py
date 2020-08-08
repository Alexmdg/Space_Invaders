from objects.stageObjects.gameEntities import *
from objects.stageObjects.hud import *
from objects.menus import *
from objects.graphics.animations import Dying


main_logger, event_logger, rect_logger, display_logger = settings.create_loggers(__name__)
main_logger.setLevel(settings.logging.DEBUG)
event_logger.setLevel(settings.logging.DEBUG)
rect_logger.setLevel(settings.logging.DEBUG)
display_logger.setLevel(settings.logging.DEBUG)


class StageRender(pygame.Surface):
    def __init__(self, size, level):
        super().__init__(size)
        self.topbar = TopBar(level)
        self.background = pygame.transform.scale(settings.IMAGE_LOADER.city_background, settings.SCREEN_SIZE)
        self.blit(self.background, (0, 0))
        self.blit(self.topbar, (0, 0))
        self.objects = {'player':  Player(),
                        'enemies': EnnemyArmy(SpaceOcto, 5, 12, 70, level),
                        'shots': Weapon(50),
                        'deads': Dying()
                    }
        self.update()
        self.is_running = True

    def update(self):
        self.blit(self.background, (0, 0))
        self.blit(self.topbar, (0, 0))
        self.collisionHandler()
        for object in self.objects:
            self.objects[object].update()
            for sprite in self.objects[object].sprites():
                self.blit(sprite.image, (sprite.rect[0], sprite.rect[1]))

    def handleEvents(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pass
        self.objects['shots'].fireShot(self.objects['player'].sprites()[0].rect, event)

    def collisionHandler(self):
        if pygame.sprite.spritecollideany(self.objects['player'].sprites()[0], self.objects['enemies']):
            self.is_running = False
        deaths = pygame.sprite.groupcollide(self.objects['shots'],
                                            self.objects['enemies'],
                                            True, True)
        power_up = pygame.sprite.spritecollideany(self.objects['player'].sprites()[0], self.objects['deads'])
        if power_up:
            self.objects['player'].power_up += 1
            power_up.kill()
        for arrow in deaths:
            for dead in deaths[arrow]:
                self.objects['deads'].died(dead)


class MenuRender(pygame.Surface):
    def __init__(self, menu):
        super().__init__(menu.body.size)
        self.is_running = True
        self.menu =  menu
        self.blit(self.menu.body.image, (0, 0))
        main_logger.debug('Display main menu : OK')

    def handleEvents(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            event_logger.debug(f'click : {event.type}, {event.pos}')

            for button in self.menu.buttons.buttons:
                event_logger.debug(f'button :{button.body.rect[0]}, {button.body.rect[0] + button.body.rect[3]}')
                if button.body.rect[0] <= event.pos[0] <= button.body.rect[0] + button.body.rect[3]\
                    and button.body.rect[1] <= event.pos[1] <= button.body.rect[1] + button.body.rect[4]:
                    self.menu.on_click(button)


    def update(self):
        pass















