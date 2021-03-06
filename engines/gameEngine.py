from engines.renderEngines import *
from graphics.graphicObjects import *
import ujson

from objects.stageObjects.player import PlayerStats

main_logger, event_logger, rect_logger, display_logger, sprite_logger = settings.create_loggers(__name__)
main_logger.setLevel(settings.logging.DEBUG)
event_logger.setLevel(settings.logging.INFO)
rect_logger.setLevel(settings.logging.INFO)
display_logger.setLevel(settings.logging.INFO)
sprite_logger.setLevel(settings.logging.DEBUG)

class GameEngine:
    def __init__(self):
        main_logger.success("Game init: OK")
        pygame.init()
        self.screen = pygame.display.set_mode(settings.SCREEN_SIZE)
        pygame.display.set_caption("Space Invaders")
        settings.IMAGE_LOADER = ImageLoader()
        self.clock = pygame.time.Clock()
        self.is_running = True
        # with open('hero.json') as f:
        #     stats = ujson.load(f)
        # self.hero = PlayerStats(stats)
        self.stages = Stages()
        # self.stages.get_stage(self.hero.level)
        self.next_scene = MainMenuScene()
        self.next_render = MenuRender(self.next_scene)
        self.number = 0
        self.main_loop()

    def main_loop(self):
        while self.is_running:
            main_logger.success("Main loop init: OK")
            depth = 0
            self.number += 1
            self.sub_loop(self.next_render, depth, self.number)
            if self.number > 15:
                self.is_running = False
        main_logger.success('Game end')
        pygame.quit()
        quit()

    def sub_loop(self, render, depth, number):
        depth += 1
        main_logger.debug(f"Sub loop {depth-1} : {number} for {type(render)} with scene {type(render.scene)} init: OK")
        while render.is_running:
            self.handleEvents(render)
            render.update()
            self.update(render)
            display_logger.debug(f'{type(render)}:is running = {render.is_running}')
            if render.is_paused:
                pause = MenuRender(PauseMenuScene())
                number = 0
                end_stage = self.sub_loop(pause, depth, number)
                if end_stage is True:
                    render.scene.is_running = False
                render.is_paused = False
                main_logger.success("Game Resumed")
        if type(render.scene) == PauseMenuScene:
            return render.scene.close_stage
        main_logger.debug(f"Sub loop {depth - 1} : {number} for {type(render)} with scene {type(render.scene)} end: OK")

    def handleEvents(self, render):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                render.is_running = False
                event_logger.success('User closed the game in a barbaric way')
                pygame.quit()
                quit()
            elif event.type == quit_game_Events:
                event_logger.success("Event 'QuitGame' Received")
                render.is_running = False
                self.is_running = False
            elif event.type == start_stage_Events:
                event_logger.success("Event 'StartStage' Received")
                if event.sender == 'PauseMenuScene':
                    render.scene.close_stage = True
                self.next_scene = eval(event.scene)(self.stages.get_stage(self.hero.level), self.hero)
                self.next_render = eval(event.render)(self.next_scene)
                self.next_render.reset(self.next_scene, self.hero)
            elif event.type == start_menu_Events:
                event_logger.success("Event 'Display Menu' Received")
                if event.scene == 'HeroMenuScene':
                    with open('hero.json') as f:
                        stats = ujson.load(f)
                    self.hero = PlayerStats(stats)
                    self.next_scene = eval(event.scene)(self.hero)
                else:
                    self.next_scene = eval(event.scene)()
                self.next_render = eval(event.render)(self.next_scene)
            elif event.type == close_render_Events:
                event_logger.success(f"Event 'Close Render' for {event.render}-{event.scene} Received")
                render.is_running = False
            elif event.type == power_up_Events:
                event_logger.success(f"Event 'PowerUp Event' : {event.sender}{event.action} Received")
                render.scene.hero.update(event.sender, event.action)
                render.scene.update_all_infos()
            elif event.type == set_and_get_Events:
                event_logger.success("Event 'Get or Set game data' Received")
                if event.action == 'get':
                    with open('hero.json') as f:
                        stats = ujson.load(f)
                    self.hero = PlayerStats(stats)
                    if event.context == 'StartGame':
                        self.hero.reset()
                if event.action == 'set':
                    if event.context == 'RestartGame':
                        render.scene.hero.reset()
                    elif event.context == 'LevelUp':
                        render.scene.hero.level += 1
                    elif event.context == 'ContinueGame':
                        render.scene.hero.kills = 0
                    render.scene.hero.save()
            else:
                render.handleEvents(event)

    def update(self, render):
        self.screen.blit(render, (0, 0))
        pygame.display.update()
        self.clock.tick(settings.FPS)

