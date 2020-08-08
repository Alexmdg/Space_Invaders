from objects.stageObjects.gameEntities import *
from objects.stageObjects.hud import *
from objects.graphics.animations import *


main_logger, event_logger, rect_logger, display_logger, sprite_logger = settings.create_loggers(__name__)
main_logger.setLevel(settings.logging.DEBUG)
event_logger.setLevel(settings.logging.DEBUG)
rect_logger.setLevel(settings.logging.DEBUG)
display_logger.setLevel(settings.logging.DEBUG)
sprite_logger.setLevel(settings.logging.DEBUG)

class Stage1:
    def __init__(self):
        self.topbar = TopBar('1')
        self.background = pygame.transform.scale(settings.IMAGE_LOADER.city_background, settings.SCREEN_SIZE)
        self.objects = {'player': Player(),
                        'enemies': EnnemyArmy(SpaceGhost, 5, 12, 70, '1'),
                        'shots': Weapon(50),
                        'deads': Dying()
                    }
