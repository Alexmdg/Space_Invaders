from engines.renderEngines import *

main_logger, event_logger, rect_logger, display_logger = settings.create_loggers(__name__)
main_logger.setLevel(settings.logging.DEBUG)
event_logger.setLevel(settings.logging.DEBUG)
rect_logger.setLevel(settings.logging.DEBUG)
display_logger.setLevel(settings.logging.DEBUG)

class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(settings.SCREEN_SIZE)
        pygame.display.set_caption("Space Invaders")
        settings.IMAGE_LOADER = ImageLoader()
        self.clock = pygame.time.Clock()
        self.running = True
        self.main_loop()

    def main_loop(self):
        while self.running:
            menu = MenuRender(MainMenu())
            self.sub_loop(menu)
        pygame.quit()
        quit()

    def sub_loop(self, render):
        while render.is_running:
            self.handleEvents(render)
            render.update()
            self.update(render)


    def handleEvents(self, render):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                render.is_running = False
                main_logger.debug(settings.Fore.BLUE + 'User closed the game')
            elif event.type == menuEvents:
                if event.render == 2:
                    pass
                if event.render == 1:
                    self.menu.is_running = False
                    self.sub_loop(StageRender(settings.STAGES[event.object_to_render]))
            else:
                render.handleEvents(event)

    def update(self, render):
        self.screen.blit(render, (0, 0))
        pygame.display.update()
        self.clock.tick(settings.FPS)
