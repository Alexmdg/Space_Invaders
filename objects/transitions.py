from objects.menuObjects.menuParts import *
from objects.menuObjects.menuEvents import *
import pygame.time
import math

main_logger, event_logger, rect_logger, display_logger, sprite_logger = settings.create_loggers(__name__)
main_logger.setLevel(settings.logging.DEBUG)
event_logger.setLevel(settings.logging.DEBUG)
rect_logger.setLevel(settings.logging.DEBUG)
display_logger.setLevel(settings.logging.DEBUG)
sprite_logger.setLevel(settings.logging.DEBUG)

class StageIntro:
    def __init__(self, stage):
        self.bg = Pannel((settings.SCREEN_SIZE[0] * 0.618, settings.SCREEN_SIZE[1] * 0.618))
        self.bg.image.convert_alpha()
        self.bg.image.set_alpha(100)
        self.bg.rect.centerx = settings.SCREEN_SIZE[0] / 2
        self.bg.rect.centery = settings.SCREEN_SIZE[1] / 2
        self.title = TextLabel((self.bg.rect[2] * 0.22, self.bg.rect[3] * 0.22), stage, 72, settings.YELLOW)
        self.title.rect.centerx = settings.SCREEN_SIZE[0] / 2
        self.title.rect.centery = (1.618 * settings.SCREEN_SIZE[1]) / 5
        self.desc = TextLabel((self.bg.rect[2] * 0.22, self.bg.rect[3] * 0.22), "Let's see what you can do", 36)
        self.desc.rect.centerx = settings.SCREEN_SIZE[0] / 2
        self.desc.rect.centery = (2.618 * settings.SCREEN_SIZE[1]) / 5
        self.counter = TextLabel((self.bg.rect[2] * 0.618, self.bg.rect[3] * 0.22), '3', 48)
        self.counter.rect.centerx = settings.SCREEN_SIZE[0] / 2
        self.counter.rect.centery = (3.618 * settings.SCREEN_SIZE[1] / 5)

        self.is_running = True
        self.clock = pygame.time.Clock()
        self.time = 0.00
        self.count = 3

    def update(self):
        display_logger.debug('transition update')
        if self.is_running:
            self.clock.tick()
            if self.clock.get_time() < 35:
                self.time += self.clock.get_time() / 1000
            display_logger.debug(
                    f'clock time: {self.clock.get_time()},\
                    self.time: {self.time},\
                    self.counter.font_size: {self.counter.font_size}\
                    self.count: {self.count}')
            if self.time >= 1:
                self.count -= 1
                self.time = 0
            if self.count >= 0:
                self.counter = TextLabel((self.bg.rect[2] * 0.618, self.bg.rect[3] * 0.22), str(self.count), int(124 * math.sin(self.time)))
                self.counter.rect.centerx = settings.SCREEN_SIZE[0] / 2
                self.counter.rect.centery = (3.618 * settings.SCREEN_SIZE[1] / 5)

            else:
                self.is_running = False
                self.time = 0
                self.count = 3


class StageOutro:
    def __init__(self):
        self.is_running = False
        self.ending = ''
        self.stage_ended = False
        self.bg = Pannel((settings.SCREEN_SIZE[0] * 0.618, settings.SCREEN_SIZE[1] * 0.618))
        self.bg.rect.centerx = settings.SCREEN_SIZE[0] / 2
        self.bg.rect.centery = settings.SCREEN_SIZE[1] / 2

        self.clock = pygame.time.Clock()
        self.time = 0.00
        self.count = 3

    def chose_ending(self, choice):
        self.ending = choice
        if choice == 'lose':
            self.bg.image.blit(pygame.transform.scale(settings.IMAGE_LOADER.dead_bg, (self.bg.rect[2], self.bg.rect[3])), (0, 0))
            self.bg.image.convert_alpha()
            self.bg.image.set_alpha(150)
            self.title = TextLabel((self.bg.rect[2] * 0.22, self.bg.rect[3] * 0.22), 'LOL...', 72)
            self.title.rect.centerx = settings.SCREEN_SIZE[0] / 2
            self.title.rect.centery = (1.618 * settings.SCREEN_SIZE[1]) / 5
            self.desc = TextLabel((self.bg.rect[2] * 0.22, self.bg.rect[3] * 0.22), 'imagine losing at lvl 1...', 36)
            self.desc.rect.centerx = settings.SCREEN_SIZE[0] / 2
            self.desc.rect.centery = (2.618 * settings.SCREEN_SIZE[1]) / 5
            # self.restart_button = Button((self.bg.rect[2] * 0.22, self.bg.rect[3] * 0.22), 'LOL you so dead...', 48)
            # self.desc.rect.centerx = settings.SCREEN_SIZE[0] / 2
            # self.desc.rect.centery = (2.618 * settings.SCREEN_SIZE[1]) / 5
            # self.quit_button = QuitButton((self.bg.rect[2] * 0.22, self.bg.rect[3] * 0.22), 'LOL you so dead...', 48)
            # self.desc.rect.centerx = settings.SCREEN_SIZE[0] / 2
            # self.desc.rect.centery = (2.618 * settings.SCREEN_SIZE[1]) / 5


    def update(self):
        display_logger.debug('outro dead transition update')
        if self.is_running:
            self.clock.tick()
            if self.clock.get_time() < 35:
                self.time += self.clock.get_time() / 1000
            display_logger.debug(
                    f'clock time: {self.clock.get_time()},\
                    self.time: {self.time},\
                    self.count: {self.count}')
            if self.time >= 1:
                self.count -= 1
                self.time = 0
            if self.count >= 0:
                # self.counter.label = self.counter.font.render(str(self.count), True, settings.GREY)
                # self.counter.rect.inflate_ip(math.cos(self.time), math.cos(self.time))
                pass
            else:
                self.is_running = False
                self.stage_ended = True
                self.time = 0
                self.count = 3
