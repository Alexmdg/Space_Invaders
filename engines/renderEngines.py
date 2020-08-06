from objects.levels import *
from objects.hud import *


logger = createLogger(__name__)
logger.setLevel(logging.DEBUG)


class StageRender(pygame.Surface):
    objects = {}
    def __init__(self, size, level):
        super().__init__(size)
        topbar = TopBar(level)
        backgroundImg = pygame.image.load(os.path.join('images\\', '2834.jpg'))
        self.background = pygame.transform.scale(backgroundImg, SCREEN_SIZE).convert_alpha()
        self.blit(self.background, (0, 0))
        self.blit(topbar, (0, 0))
        self.objects['player'] = Player()
        self.objects['enemies'] = EnnemyArmy(5, 12, 70, '1')
        self.objects['shots'] = Arrows(50)
        self.running = True

    def showObjects(self):
        for object in self.objects:
            self.objects[object].update()
            for sprite in self.objects[object].sprites():
                self.blit(sprite.image, (sprite.rect[0], sprite.rect[1]))

    def handleEvent(self, event):
        self.objects['shots'].fireShot(self.objects['player'].sprites()[0].rect, event)
        pygame.sprite.groupcollide(
            self.objects['shots'],
            self.objects['enemies'],
            True, True)
        if pygame.sprite.spritecollideany(self.objects['player'].sprites()[0], self.objects['enemies']):
            self.running = False

class GUIRender:
    pass






