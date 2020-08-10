from objects.menuObjects.menuParts import *
from objects.menuObjects.menuEvents import *
import pygame.time
import math

main_logger, event_logger, rect_logger, display_logger, sprite_logger = settings.create_loggers(__name__)
main_logger.setLevel(settings.logging.DEBUG)
event_logger.setLevel(settings.logging.INFO)
rect_logger.setLevel(settings.logging.DEBUG)
display_logger.setLevel(settings.logging.INFO)
sprite_logger.setLevel(settings.logging.DEBUG)

class StageIntro(Pannel):
    def __init__(self, stage, ratiox=0.423, ratioy=0.618):
        super().__init__((ratiox * settings.SCREEN_SIZE[0], ratioy * settings.SCREEN_SIZE[1]))
        self.image.convert_alpha()
        self.image.fill(settings.Purple(100))
        self.rect.centerx = settings.SCREEN_SIZE[0] / 2
        self.rect.centery = settings.SCREEN_SIZE[1] / 2
        self.title = TextLabel((self.rect[2] * 0.22, self.rect[3] * 0.22), stage, 72, settings.Yellow())
        self.title.rect.centerx = self.size[0] / 2
        self.title.rect.centery = (1.618 * self.size[1]) / 5
        self.desc = TextLabel((self.rect[2] * 0.22, self.rect[3] * 0.22), "Let's see what you can do", 36)
        self.desc.rect.centerx = self.size[0] / 2
        self.desc.rect.centery = (2.618 * self.size[1]) / 5
        self.counter = TextLabel((self.rect[2] * 0.618, self.rect[3] * 0.22), '3', 48)
        self.counter.rect.centerx = self.size[0] / 2
        self.counter.rect.centery = (4.618 * self.size[1]) / 5
        self.image.blit(self.title.label, self.title.rect)
        self.image.blit(self.desc.label, self.desc.rect)
        self.image.blit(self.counter.label, self.counter.rect)

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
                self.counter = TextLabel((self.rect[2] * 0.618, self.rect[3] * 0.22), str(self.count), int(124 * math.sin(self.time)))
                self.counter.rect.centerx = self.size[0] / 2
                self.counter.rect.centery = (3.618 * self.size[1] / 5)
                self.image.fill(settings.Purple(100))
                self.image.blit(self.title.label, self.title.rect)
                self.image.blit(self.desc.label, self.desc.rect)
                self.image.blit(self.counter.label, self.counter.rect)

            else:
                self.is_running = False
                self.time = 0
                self.count = 3


class StageOutro(Pannel):
    def __init__(self, level, stats, ratiox=0.786, ratioy=0.618):
        super().__init__((ratiox * settings.SCREEN_SIZE[0], ratioy * settings.SCREEN_SIZE[1]))
        self.image.convert_alpha()
        self.image.fill(settings.Purple(100))
        self.stats = stats
        self.is_running = False
        self.ending = ''
        self.stage_ended = False
        self.rect.centerx = settings.SCREEN_SIZE[0] / 2
        self.rect.centery = settings.SCREEN_SIZE[1] / 2

        self.buttons = ItemBox('mainBox', side='Horizontal')

    def chose_ending(self, choice):
        self.ending = choice
        if choice == 'lose':
            self.background = pygame.Surface(self.size)
            self.background.blit(
                pygame.transform.scale(settings.IMAGE_LOADER.dead_bg, (int(self.size[0]), int(self.size[1]))),
                (0, 0))
            self.background.convert_alpha()
            self.background.set_alpha(175)
            self.image.blit(self.background, (0, 0))
            self.title = TextLabel((self.rect[2] * 0.22, self.rect[3] * 0.22), 'LOL...', 72)
            self.title.rect.centerx = self.size[0] / 2
            self.title.rect.centery = (1.618 * self.size[1]) / 5
            self.desc = TextLabel((self.rect[2] * 0.22, self.rect[3] * 0.22), f'imagine losing at lvl 1...', 36)
            self.desc.rect.centerx = self.size[0] / 2
            self.desc.rect.centery = (2.618 * self.size[1]) / 5
            self.buttons.items.append(Button('levelRestart',
                                              (0.382 * self.size[0],
                                               0.161 * self.size[1]),
                                              "Try Again",
                                              48,
                                              MenuEventsRestartLevel()))
            self.buttons.items.append(Button('mainMenu',
                                             (0.382 * self.size[0],
                                              0.161 * self.size[1]),
                                             "Main Menu",
                                             48,
                                             MenuEventsMainMenu()))
            self.buttons.createPannel(self.size[0] / 2, self.size[1] * 0.786, space_between=5.57, transparent=True)
            self.image.blit(self.buttons.image, self.buttons.rect)

        elif choice == "win":
            self.background = pygame.Surface(self.size)
            self.background.blit(
                pygame.transform.scale(settings.IMAGE_LOADER.win_bg, (int(0.618 * self.size[0]), int(self.size[1]))),
                ((self.size[0] - (0.618 * self.size[0])) / 2, 0))
            self.background.convert_alpha()
            self.background.set_alpha(175)
            self.image.blit(self.background, (0, 0))
            self.title = TextLabel((self.rect[2] * 0.22, self.rect[3] * 0.22), 'Stage 1 complete', 72)
            self.title.rect.centerx = self.size[0] / 2
            self.title.rect.centery = (1.618 * self.size[1]) / 5
            self.desc = TextLabel((self.rect[2] * 0.22, self.rect[3] * 0.22), f'stats = {self.stats}', 36)
            self.desc.rect.centerx = self.size[0] / 2
            self.desc.rect.centery = (2.618 * self.size[1]) / 5
            self.buttons.items.append(Button('nextLevel',
                                              (0.268 * self.size[0],
                                               0.161 * self.size[1]),
                                              "Continue",
                                              48,
                                              MenuEventsNextLevel()))
            self.buttons.items.append(Button('heroMenu',
                                             (0.268 * self.size[0],
                                              0.161 * self.size[1]),
                                             "Hero Stats",
                                             48,
                                             MenuEventsHeroMenu()))
            self.buttons.items.append(Button('mainMenu',
                                             (0.268 * self.size[0],
                                              0.161 * self.size[1]),
                                             "Main Menu",
                                             48,
                                             MenuEventsMainMenu()))
            self.buttons.createPannel(self.size[0] / 2, self.size[1] * 0.786, space_between=5.57, transparent=True)
            self.image.blit(self.buttons.image, self.buttons.rect)

        self.image.blit(self.title.label, self.title.rect)
        self.image.blit(self.desc.label, self.desc.rect)

    def update(self):
        self.buttons.update()
        self.image.blit(self.buttons.image, self.buttons.rect)
        self.image.blit(self.title.label, self.title.rect)
        self.image.blit(self.desc.label, self.desc.rect)

