from objects.stageObjects.gameEntities import *
from objects.stageObjects.hud import *
from objects.graphics.animations import *
from .transitions import StageIntro, StageOutro


main_logger, event_logger, rect_logger, display_logger, sprite_logger = settings.create_loggers(__name__)
main_logger.setLevel(settings.logging.DEBUG)
event_logger.setLevel(settings.logging.DEBUG)
rect_logger.setLevel(settings.logging.DEBUG)
display_logger.setLevel(settings.logging.INFO)
sprite_logger.setLevel(settings.logging.DEBUG)

class Stage:
    def __init__(self, level):
        self.is_running = True
        self.level = level
        self.topbar = TopBar(level.level)
        self.background = pygame.transform.scale(settings.IMAGE_LOADER.city_background, settings.SCREEN_SIZE)
        self.intro = StageIntro(level.name)
        self.outro = StageOutro()
        self.objects = {'player': [Player()],
                        'enemies': self.level.initial_spawns,
                        'shots': [Weapon(50)],
                        'deads': [Dying()]
                    }
        self.clock = pygame.time.Clock()
        self.time = 0.00
        self.count = 0
        main_logger.succes('Load Stage 1 : OK')

    def update(self):
        if self.outro.stage_ended:
            self.is_running = False
        else:
            self.clock.tick()
            if self.clock.get_time() < 35:
                self.time += self.clock.get_time() / 1000
            display_logger.debug(f'clock time: {self.clock.get_time()}, self.time: {self.time}, self.count: {self.count}')
            if self.count < self.level.waves:
                if self.time >= self.level.spawn_delays[self.count]:
                    self.objects['enemies'].append(self.level.spawns[self.count])
                    self.time = 0
                    self.count += 1
                else:
                    pass

class Level1:
    def __init__(self):
        self.level = '1'
        self.name = 'Stage 1'
        self.waves = 2
        self.initial_spawns = [EnnemyArmy(SpaceOcto, 5, 12, 70, '1')]
        self.spawns = [EnnemyArmy(SpaceGhost, 5, 8, 70, '1'),
                       EnnemyArmy(SpaceBlob, 3, 6, 70, '1')]
        self.spawn_delays = [18, 18]
        self.difficulty = '1'
        self.player_stats = {}