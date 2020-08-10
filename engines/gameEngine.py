from engines.renderEngines import *
from objects.graphics.graphicObjects import *
import ujson

main_logger, event_logger, rect_logger, display_logger, sprite_logger = settings.create_loggers(__name__)
main_logger.setLevel(settings.logging.INFO)
event_logger.setLevel(settings.logging.INFO)
rect_logger.setLevel(settings.logging.INFO)
display_logger.setLevel(settings.logging.INFO)
sprite_logger.setLevel(settings.logging.INFO)

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
        with open('hero.json') as f:
            stats = ujson.load(f)
        self.hero = PlayerStats(stats)
        self.stages = Stages()
        self.main_loop()


    def main_loop(self):
        main_logger.success("Main loop init: OK")
        while self.is_running:
            self.menu = MenuRender(MainMenu())
            self.sub_loop(self.menu)
        main_logger.success('User closed the game')
        pygame.quit()
        quit()

    def sub_loop(self, render):
        main_logger.success(f"Sub loop for {type(render)} init: OK")
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
                event_logger.success('User closed the game')
                pygame.quit()
                quit()
            elif event.type == menuEvents:
                if event.action == 'Quit':
                    render.is_running = False
                    self.is_running = False
                    event_logger.success('User closed the game')
                    pygame.quit()
                    quit()
                elif event.action == 'StartGame':
                    render.is_running = False
                    self.stages.get_stage(self.hero.level)
                    event_logger.success(f"Event 'StartGame' received: Startig sub_loop on StageRender(stage = Stage({self.hero.level})")
                    self.sub_loop(StageRender(settings.SCREEN_SIZE, Stage(self.stages, self.hero)))
                elif event.action == 'ResumeGame':
                    render.is_running = False
                elif event.action == 'MainMenu':
                    render.is_running = False
                    self.sub_loop(MenuRender(MainMenu()))
                elif event.action == 'RestartLevel':
                    pass
                elif event.action == 'NextLevel':
                    pass
                elif event.action == 'HeroMenu':
                    pass
            else:
                render.handleEvents(event)

    def update(self, render):
        self.screen.blit(render, (0, 0))
        pygame.display.update()
        self.clock.tick(settings.FPS)

