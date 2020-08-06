import multiprocessing
from engines.renderEngines import *


class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Space Invaders")
        self.clock = pygame.time.Clock()
        self.running = True

        while self.running:
            stage = StageRender(SCREEN_SIZE, "1")
            self.screen.blit(stage, (0, 0))
            while stage.running:
                self.handleEvents(stage)
                self.update(stage)
                stage.showObjects()
        pygame.quit()
        quit()

    def handleEvents(self, render):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                render.running = False
                logger.debug(Fore.BLUE + 'User closed the game')
            else:
                render.handleEvent(event)

    def update(self, render):
        self.screen.blit(render, (0, 0))
        pygame.display.update()
        self.clock.tick(FPS)

