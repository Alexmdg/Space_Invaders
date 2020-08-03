from engines.renders import *


class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Invaders")
        backgroundImg = pygame.image.load(os.path.join('../images', 'background.jpg'))
        self.background = pygame.transform.scale(backgroundImg, (800, 600))
        self.clock = pygame.time.Clock()

        self.running = True
        level1 = LevelsRender()
        while self.running:
            self.screen.blit(self.background, (0, 0))
            while level1.running:
                self.screen.blit(self.background, (0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        level1.running = False
                        logger.debug(Fore.BLUE + 'User closed the game')
                    else:
                        level1.handleEvent(event)
                pygame.sprite.groupcollide(
                    level1.objects['shots'],
                    level1.objects['enemies'],
                    True, True)
                level1.objects['enemies'].update()
                level1.objects['player'].show()
                level1.objects['shots'].update()
                pygame.display.update()
                self.clock.tick(34)

        pygame.quit()
        quit()
