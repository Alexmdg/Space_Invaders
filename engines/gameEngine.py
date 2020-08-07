import multiprocessing
from engines.renderEngines import *


class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Space Invaders")
        settings.IMAGE_LOADER = ImageLoader()
        self.clock = pygame.time.Clock()
        self.running = True
        self.main_loop()

    def main_loop(self):
        while self.running:
            stage = StageRender(SCREEN_SIZE, "1")
            self.screen.blit(stage, (0, 0))
            while stage.running:
                self.handleEvents(stage)
                stage.showObjects()
                self.update(stage)
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

