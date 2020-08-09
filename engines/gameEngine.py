from engines.renderEngines import *
from objects.graphics.graphicObjects import *

main_logger, event_logger, rect_logger, display_logger, sprite_logger = settings.create_loggers(__name__)
main_logger.setLevel(settings.logging.DEBUG)
event_logger.setLevel(settings.logging.DEBUG)
rect_logger.setLevel(settings.logging.DEBUG)
display_logger.setLevel(settings.logging.DEBUG)
sprite_logger.setLevel(settings.logging.DEBUG)

class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(settings.SCREEN_SIZE)
        pygame.display.set_caption("Space Invaders")
        settings.IMAGE_LOADER = ImageLoader()
        self.clock = pygame.time.Clock()
        self.menu = None
        self.stage = None
        self.is_running = True
        self.main_loop()


    def main_loop(self):
        while self.is_running:
            self.menu = MenuRender(MainMenu())
            self.sub_loop(self.menu)
        pygame.quit()
        quit()

    def sub_loop(self, render):
        while render.is_running:
            self.handleEvents(render)
            render.update()
            self.update(render)
            if render.is_paused:
                self.menu = MenuRender(PauseMenu())
                self.sub_loop(self.menu)
                render.is_paused = False


    def handleEvents(self, render):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                render.is_running = False
                main_logger.succes('User closed the game')
                pygame.quit()
                quit()
            elif event.type == menuEvents:
                if event.action == 'Quit':
                    render.is_running = False
                    self.is_running = False
                    main_logger.succes('User closed the game')
                    pygame.quit()
                    quit()
                elif event.action == 'start_g':
                    render.is_running = False
                    self.sub_loop(StageRender(settings.SCREEN_SIZE, Stage(Level1())))
                elif event.action == 'ResumeGame':
                    render.is_running = False

            else:
                render.handleEvents(event)

    def update(self, render):
        self.screen.blit(render, (0, 0))
        pygame.display.update()
        self.clock.tick(settings.FPS)

