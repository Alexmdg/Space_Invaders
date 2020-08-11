from objects.stageObjects.gameEntities import *
from objects.menuObjects.hud import *
from objects.graphics.animations import *
from .transitions import StageIntro, StageOutro


main_logger, event_logger, rect_logger, display_logger, sprite_logger = settings.create_loggers(__name__)
main_logger.setLevel(settings.logging.INFO)
event_logger.setLevel(settings.logging.INFO)
rect_logger.setLevel(settings.logging.INFO)
display_logger.setLevel(settings.logging.INFO)
sprite_logger.setLevel(settings.logging.INFO)

class StageScene():
    def __init__(self, stage, hero):
        self.is_running = True
        self.level = stage
        self.hero = hero
        self.topbar = TopBar(stage.level)
        self.background = pygame.transform.scale(settings.IMAGE_LOADER.city_background, settings.SCREEN_SIZE)
        self.objects = {'player': [Player(self.hero)],
                        'enemies': [eval(enemies) for enemies in self.level.initial_spawns],
                        'shots': [Weapon(50)],
                        'deads': [Dying()]
                    }
        sprite_logger.debug(f'{self.objects}')
        self.intro = StageIntro(stage.name)
        self.outro = StageOutro()
        self.clock = pygame.time.Clock()
        self.time = 0.00
        self.count = 0
        main_logger.success(f'Load StageScene {stage.level} : OK')

    def reset(self, stage, hero):
        try:
            self.is_running = None
            self.level = None
            self.hero = None
            self.topbar = None
            self.background = None
            self.objects = None
            self.intro = None
            self.outro = None
            self.clock = None
            self.time = None
            self.count = None
            sprite_logger.debug(f'{self.objects}')
            self.__init__(stage, hero)
            display_logger.success(f'StageScene has been reset. self.is_running = {self.is_running}')
        except:
            display_logger.exception('StageScene reset failled')
        return self

    def update(self):
        if self.is_running is True:
            if self.outro.stage_ended:
                self.is_running = False
            else:
                self.clock.tick()
                if self.clock.get_time() < 35:
                    self.time += self.clock.get_time() / 1000
                display_logger.debug(f'clock time: {self.clock.get_time()}, self.time: {self.time}, self.count: {self.count}')
                if self.count < self.level.waves:
                    if self.time >= self.level.spawn_delays[self.count]:
                        self.objects['enemies'].append(eval(self.level.spawns[self.count]))
                        self.time = 0
                        self.count += 1
                elif self.count == self.level.waves:
                    if self.time >= self.level.spawn_delays[self.count]:
                        self.outro.chose_ending('win')
                        self.outro.is_running = True

class Stages:
    def __init__(self):
        self.stages = [
            {
                'level': 1,
                'name': 'Stage 1',
                'waves': 0,
                'initial_spawns': ["EnnemyArmy(SpaceOcto, 5, 12, 70, '1')"],
                'spawns': [],
                'spawn_delays': [50],
                'difficulty': '1',
                'total_unit': 0,
            },
            {
                'level': 2,
                'name': 'Stage 2',
                'waves': 0,
                'initial_spawns': ["EnnemyArmy(SpaceOcto, 5, 12, 70, '1')"],
                'spawns': ["EnnemyArmy(SpaceGhost, 5, 8, 70, '1')",
                           "EnnemyArmy(SpaceBlob, 3, 6, 70, '1')"],
                'spawn_delays': [18, 18, 18],
                'difficulty': '1',
                'total_unit': 0,
            }
        ]

    def get_stage(self, level):
        try:
            for stage in self.stages:
                if self.stages.index(stage) == level-1:
                    self.level = stage['level']
                    self.name = stage['name']
                    self.waves = stage['waves']
                    self.initial_spawns = stage['initial_spawns']
                    self.spawns = stage['spawns']
                    self.spawn_delays = stage['spawn_delays']
                    self.difficulty = stage['difficulty']
                    self.total_unit = 0
                    for army in self.initial_spawns:
                        Earmy = eval(army)
                        self.total_unit += len(Earmy.sprites())
                    for army in self.spawns:
                        Earmy = eval(army)
                        self.total_unit += len(Earmy.sprites())
            main_logger.success(f'scenatio {self.name} init : OK')
        except:
            main_logger.exception("Couldn't get_stage")

        return self



