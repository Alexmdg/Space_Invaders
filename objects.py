import pygame
import os
import math
from settings import *

# Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>


logger = createLogger(__name__)
logger.setLevel(logging.DEBUG)

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.img = pygame.transform.scale(
                            pygame.image.load(os.path.join('images', 'soldier.png')).convert_alpha(),
                            (48, 48)
                        )
        self.rect = pygame.Rect(370, 515, 48, 48)
        self.speed = 0
        self.alive = True

    def show(self):
        self._movePlayer()
        pygame.display.get_surface().blit(self.img, (self.rect))

    def _movePlayer(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speed -= 0.16
        if keys[pygame.K_RIGHT]:
            self.speed += 0.16
        if keys[pygame.K_LEFT] and self.speed > -0.2:
            self.speed -= 0.38
        if keys[pygame.K_RIGHT] and self.speed < 0.2:
            self.speed += 0.38
        if keys[pygame.K_LEFT] == 0 and self.speed < 0:
            self.speed += 0.5
        if keys[pygame.K_RIGHT] == 0 and self.speed > 0:
            self.speed -= 0.5
        if self.rect.x < 0:
            self.rect.x = 0
            self.speed = 0
        elif self.rect.x > 752:
            self.rect.x = 752
            self.speed = 0
        self.rect.move_ip(self.speed, 0)


class OctoArmy(pygame.sprite.Group):
    class SpaceOcto(pygame.sprite.Sprite):
        def __init__(self, rect):
            super().__init__()
            self.rect = rect

    def __init__(self, rows, columns):
        super().__init__()
        self.img = pygame.transform.scale(
            pygame.image.load(os.path.join('images', 'ennemy.png')).convert_alpha(),
            (36, 36)
        )
        self.dXn = 0
        self.dXn_m1 = 0
        self.dY = 0
        self.level = LEVEL['1']

        for j in range(0, rows):
            for i in range(0, columns):
                enemy = self.SpaceOcto(pygame.Rect(203 + (48 * i), 50 + (46 * j),
                                                          36, 36))
                self.add(enemy)
        logger.debug(Fore.MAGENTA + f"{self.sprites()}")

    def update(self):
        self.dXn_m1 = self.dXn
        self.dXn = 5.55 * math.cos(pygame.time.get_ticks() / 700)
        if self.dXn * self.dXn_m1 < 0:
            self.dY = 1
        else:
            self.dY = 0
        logger.debug(Fore.BLUE + f'{self.dXn} | {self.dXn * self.dXn_m1} | {self.dY}')
        for enemy in self.sprites():
            pygame.display.get_surface().blit(self.img, enemy.rect)
            enemy.rect.move_ip(self.dXn, self.dY * self.level)


class Arrows(pygame.sprite.Group):
    class Arrow(pygame.sprite.Sprite):
        def __init__(self, rect):
            super().__init__()
            self.rect = rect
            self.hit = False
        def update(self):
            if self.rect.y <= 0:
                self.kill()
            try:
                pygame.display.get_surface().blit(self.groups()[0].img, self.rect)
                self.rect.move_ip(0, self.groups()[0].speed)
            except:
                pass

    def __init__(self):
        super().__init__()
        self.img = pygame.transform.scale(
                            pygame.image.load(os.path.join('images', 'spear.png')).convert_alpha(),
                            (15, 22)
                    )
        self.speed = -6.66
        self.shot_fired = False

    def fireShot(self, player_rect, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if len(self.sprites()) < 12 and self.shot_fired is False:
                    shot = self.Arrow(pygame.Rect(player_rect.x, player_rect.y - 34, 15, 22))
                    self.add(shot)
                    self.shot_fired = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.shot_fired = False



