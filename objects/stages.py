from objects.stageObjects.gameEntities import *
from objects.stageObjects.hud import *
from objects.graphics.animations import *


main_logger, event_logger, rect_logger, display_logger, sprite_logger = settings.create_loggers(__name__)
main_logger.setLevel(settings.logging.DEBUG)
event_logger.setLevel(settings.logging.DEBUG)
rect_logger.setLevel(settings.logging.DEBUG)
display_logger.setLevel(settings.logging.INFO)
sprite_logger.setLevel(settings.logging.DEBUG)

class Stage1:
    def __init__(self):
        self.topbar = TopBar('1')
        self.background = pygame.transform.scale(settings.IMAGE_LOADER.city_background, settings.SCREEN_SIZE)
        self.objects = {'player': [Player()],
                        'enemies': [EnnemyArmy(SpaceBlob, 5, 8, 70, '1')],
                        'shots': [Weapon(50)],
                        'deads': [Dying()]
                    }
        self.clock = pygame.time.Clock()
        self.time = 0
        self.count = 0
    def update(self):
        self.clock.tick()
        self.time += self.clock.get_time() / 1000
        display_logger.debug(f'self.time : {self.time}')
        if self.time >= 20 and self.count == 0:
            self.objects['enemies'].append(EnnemyArmy(SpaceBlob, 5, 8, 70, '1'))
            self.time = 0
            self.count = 1
        if self.time >= 20 and self.count == 1:
            self.objects['enemies'].append(EnnemyArmy(SpaceBlob, 3, 6, 70, '1'))
            self.time = 0
            self.count += 1
