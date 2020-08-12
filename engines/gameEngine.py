from engines.renderEngines import *
from objects.graphics.graphicObjects import *
import ujson

main_logger, event_logger, rect_logger, display_logger, sprite_logger = settings.create_loggers(__name__)
main_logger.setLevel(settings.logging.DEBUG)
event_logger.setLevel(settings.logging.INFO)
rect_logger.setLevel(settings.logging.INFO)
display_logger.setLevel(settings.logging.INFO)
sprite_logger.setLevel(settings.logging.INFO)

class GameEngine:
    def __init__(self):
        main_logger.success("Game init: OK")
        pygame.init()
        self.screen = pygame.display.set_mode(settings.SCREEN_SIZE)
        pygame.display.set_caption("Space Invaders")
        settings.IMAGE_LOADER = ImageLoader()
        self.clock = pygame.time.Clock()
        self.is_running = True
        with open('hero.json') as f:
            stats = ujson.load(f)
        self.hero = PlayerStats(stats)
        self.stages = Stages()
        self.stages.get_stage(self.hero.level)
        self.stage = StageRender(settings.SCREEN_SIZE, StageScene(self.stages.get_stage(self.hero.level), self.hero))
        self.menu = MenuRender(MainMenuScene())
        self.next_scene = 'menu'
        self.number = 0
        self.main_loop()

    def main_loop(self):
        while self.is_running:
            main_logger.success("Main loop init: OK")
            depth = 0
            self.number += 1
            if self.next_scene == 'stage':
                self.stage = self.stage.reset(settings.SCREEN_SIZE, StageScene(self.stages.get_stage(self.hero.level), self.hero), self.hero)
                self.sub_loop(self.stage, depth, self.number)
            elif self.next_scene == 'menu':
                self.sub_loop(self.menu, depth, self.number)
            if self.number > 15:
                self.is_running = False
        main_logger.success('Game end')
        pygame.quit()
        quit()

    def sub_loop(self, render, depth, number):
        depth += 1
        try:
            main_logger.success(
                f"Sub loop {depth - 1} : {number} for {type(render)} with scene {type(render.stage)} init: OK")
        except:
            main_logger.debug(f"Sub loop {depth-1} : {number} for {type(render)} with scene {type(render.menu)} init: OK")
        while render.is_running:
            self.handleEvents(render)
            render.update()
            self.update(render)
            display_logger.debug(f'{type(render)}:is running = {render.is_running}')
            if render.is_paused:
                self.menu = MenuRender(PauseMenuScene())
                number = 0
                end_stage = self.sub_loop(self.menu, depth, number)
                if end_stage is True:
                    render.stage.is_running = False
                    # pygame.event.post(MenuEventsCloseStage().event)
                render.is_paused = False
                main_logger.success("Game Resumed")
        if type(render) == MenuRender:
            if type(render.menu) == PauseMenuScene:
                return render.menu.close_stage
        try:
            main_logger.debug(
                f"Sub loop {depth - 1} : {number} for {type(render)} with scene {type(render.stage)} end: OK")
        except:
            main_logger.debug(
                f"Sub loop {depth - 1} : {number} for {type(render)} with scene {type(render.menu)} end: OK")


    def handleEvents(self, render):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                render.is_running = False
                event_logger.success('User closed the game')
                pygame.quit()
                quit()
            elif event.type == quit_game_Events:
                event_logger.success("Event 'QuitGame' Received")
                render.is_running = False
                self.is_running = False
            elif event.type == start_stage_Events:
                event_logger.success("Event 'StartStage' Received")
            elif event.type == close_stage_Events:
                event_logger.success("Event 'CloseStage' Received")
            elif event.type == set_and_get_Events:
                event_logger.success("Event 'Get or Set game data' Received")
            elif event.type == start_menu_Events:
                event_logger.success("Event 'Display Menu' Received")
            elif event.type == close_menu_Events:
                event_logger.success("Event 'Close Menu' Received")

            else:
                render.handleEvents(event)

    def update(self, render):
        self.screen.blit(render, (0, 0))
        pygame.display.update()
        self.clock.tick(settings.FPS)

