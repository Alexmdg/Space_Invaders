from engines.renderEngines import *


class GameEngine:
    def __init__(self):
        global SCREEN_SIZE
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        SCREEN_SIZE = self.screen.get_size()
        pygame.display.set_caption("Space Invaders")
        self.clock = pygame.time.Clock()
        self.running = True

        while self.running:
            level = StageRender(SCREEN_SIZE, "1")
            self.screen.blit(level, (0, 0))
            while level.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        level.running = False
                        logger.debug(Fore.BLUE + 'User closed the game')
                    else:
                        level.handleEvent(event)
                level.showObjects()
                self.screen.blit(level, (0, 0))
                pygame.display.update()
                self.clock.tick(34)

        pygame.quit()
        quit()
