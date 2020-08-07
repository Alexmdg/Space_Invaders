from objects.stages.gameEntities import *
from objects.stages.hud import *
from objects.graphics.animations import Dying

logger = createLogger(__name__)
logger.setLevel(logging.INFO)


class StageRender(pygame.Surface):
    def __init__(self, size, level):
        super().__init__(size)
        self.topbar = TopBar(level)
        self.background = pygame.transform.scale(settings.IMAGE_LOADER.city_background, SCREEN_SIZE)
        self.blit(self.background, (0, 0))
        self.blit(self.topbar, (0, 0))
        self.objects = {'player':  Player(),
                        'enemies': EnnemyArmy(SpaceOcto, 5, 12, 70, level),
                        'shots': Weapon(50),
                        'deads': Dying()
                    }
        self.showObjects()
        self.running = True

    def showObjects(self):
        self.blit(self.background, (0, 0))
        self.blit(self.topbar, (0, 0))
        self.collisionHandler()
        for object in self.objects:
            self.objects[object].update()
            for sprite in self.objects[object].sprites():
                self.blit(sprite.image, (sprite.rect[0], sprite.rect[1]))

    def handleEvent(self, event):
        self.objects['shots'].fireShot(self.objects['player'].sprites()[0].rect, event)

    def collisionHandler(self):
        if pygame.sprite.spritecollideany(self.objects['player'].sprites()[0], self.objects['enemies']):
            self.running = False
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
    def __init__(self, size):
        super().__init__(size)






