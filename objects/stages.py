from objects.stageObjects.gameEntities import *
from objects.stageObjects.hud import *
from objects.graphics.animations import *
from objects.menuObjects.menuParts import *


main_logger, event_logger, rect_logger, display_logger, sprite_logger = settings.create_loggers(__name__)
main_logger.setLevel(settings.logging.DEBUG)
event_logger.setLevel(settings.logging.DEBUG)
rect_logger.setLevel(settings.logging.DEBUG)
display_logger.setLevel(settings.logging.DEBUG)
sprite_logger.setLevel(settings.logging.DEBUG)

class Stage1:
    def __init__(self):
        self.topbar = TopBar('1')
        sprite_logger.succes('Load topbar : OK')
        self.background = pygame.transform.scale(settings.IMAGE_LOADER.city_background, settings.SCREEN_SIZE)
        sprite_logger.succes('Load background : OK')
        self.intro = Pannel((settings.SCREEN_SIZE[0] * 0.618, settings.SCREEN_SIZE[1] * 0.618))
        self.intro.image.convert_alpha()
        self.intro.image.set_alpha(100)
        sprite_logger.succes('Load intro background : OK')
        self.intro.rect.centerx = settings.SCREEN_SIZE[0] / 2
        self.intro.rect.centery = settings.SCREEN_SIZE[1] / 2
        self.title = TextLabel((self.intro.rect[2] * 0.22, self.intro.rect[3] * 0.22), 'Stage 1', 48)
        self.title.rect.centerx = settings.SCREEN_SIZE[0] / 2
        self.title.rect.centery = (2 * settings.SCREEN_SIZE[1]) / 5
        sprite_logger.succes('Load intro title : OK')
        self.counter = TextLabel((self.intro.rect[2] * 0.618, self.intro.rect[3] * 0.22), '3', 48)
        self.counter.rect.centerx = settings.SCREEN_SIZE[0] / 2
        self.counter.rect.centery = (3 * settings.SCREEN_SIZE[1] / 5)
        sprite_logger.succes('Load counter : OK')
        self.intro_is_running = True
        sprite_logger.succes('into_is_running = True : OK')

        self.objects = {'player': [Player()],
                        'enemies': [EnnemyArmy(SpaceOcto, 5, 12, 70, '1')],
                        'shots': [Weapon(50)],
                        'deads': [Dying()]
                    }

        self.clock = pygame.time.Clock()
        self.time = 0.00
        self.intro_count = 3
        self.count = 0
        sprite_logger.succes('Load Stage 1 : OK')

    def update(self):
        main_logger.succes(f'stage update init : OK {self.intro_is_running}')
        self.clock.tick()
        if self.clock.get_time() < 35:
            self.time += self.clock.get_time() / 1000
        display_logger.debug(f'clock time: {self.clock.get_time()}, self.time: {self.time}, self.intro_count: {self.intro_count}, self.count: {self.count}')
        if self.intro_is_running is True:
            if self.time >= 1:
                self.intro_count -= 1
                self.time = 0
            if self.intro_count >= 0:
                self.runIntro(str(self.intro_count))
            else:
                self.intro_is_running = False
                self.time = 0
                self.intro_count = 3
        else:
            if self.time >= 15 and self.count == 0:
                self.objects['enemies'].append(EnnemyArmy(SpaceGhost, 5, 8, 70, '1'))
                self.time = 0
                self.count = 1
            if self.time >= 10 and self.count == 1:
                self.objects['enemies'].append(EnnemyArmy(SpaceBlob, 3, 6, 70, '1'))
                self.time = 0
                self.count += 1

    def runIntro(self, count):
        self.counter.label = self.counter.font.render(count, True, settings.GREY)
        self.counter.rect.inflate_ip(math.cos(self.time / 7000), math.cos(self.time / 7000))


