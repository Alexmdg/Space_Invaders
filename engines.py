from objects import *


logger = createLogger(__name__)
logger.setLevel(logging.DEBUG)


class RenderEngine:

    objects = {}
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Invaders")
        backgroundImg = pygame.image.load(os.path.join('images', 'background.jpg'))
        self.background = pygame.transform.scale(backgroundImg, (800, 600))
        self.objects['player'] = Player()
        self.objects['enemies'] = OctoArmy(5, 12)
        self.objects['shots'] = Arrows()

    def showObjects(self):
        for entity in self.objects:
            self.objects[entity].show(self.objects['player'].rect)



class EventsEngine(RenderEngine):
    def __init__(self):
        super().__init__()

    def handleEvent(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            logger.debug(Fore.BLUE + 'User closed the game')
        else:
            self.objects['shots'].fireShot(self.objects['player'].rect, event)


class GameEngine(EventsEngine):
    def __init__(self):
        super().__init__()
        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()
        while self.running:
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():
               self.handleEvent(event)
            pygame.sprite.groupcollide(
                    self.objects['shots'],
                    self.objects['enemies'],
                    True, True)
            self.objects['enemies'].update()
            self.objects['player'].show()
            self.objects['shots'].update()

            pygame.display.update()
            self.clock.tick(34)

        pygame.quit()
        quit()