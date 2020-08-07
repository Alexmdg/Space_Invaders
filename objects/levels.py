import pygame
import os
import math
import settings
from .graphicObjects import *

# Icons and Images made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>


logger = settings.createLogger(__name__)
logger.setLevel(settings.logging.INFO)

class Player(pygame.sprite.Group):
    class BasePlayer(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.transform.scale(settings.GRAPHIC_OBJECTS.base_player, (settings.UNITS_SIZE, settings.UNITS_SIZE))
            self.rect = pygame.Rect((settings.SCREEN_SIZE[0] / 2) - 12, settings.SCREEN_SIZE[1] - settings.UNITS_SIZE * 1.2, settings.UNITS_SIZE,
                                    settings.UNITS_SIZE)
    def __init__(self):
        super().__init__()
        self.max_speed = 5
        self.max_ammo = 7
        self.damage = 1
        self.speed = 0
        self.alive = True
        player = self.BasePlayer()
        self.add(player)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and abs(self.speed) < self.max_speed:
            self.speed -= 0.2
        if keys[pygame.K_RIGHT]and self.speed < self.max_speed:
            self.speed += 0.2
        if keys[pygame.K_LEFT] and self.speed > -0.2:
            self.speed -= 0.4
        if keys[pygame.K_RIGHT] and self.speed < 0.2:
            self.speed += 0.4
        if keys[pygame.K_LEFT] == 0 and self.speed < 0:
            self.speed += 0.6
        if keys[pygame.K_RIGHT] == 0 and self.speed > 0:
            self.speed -= 0.6
        if self.sprites()[0].rect.x < 0:
            self.sprites()[0].rect.x = 0
            self.speed = 0
        elif self.sprites()[0].rect.x > 752:
            self.sprites()[0].rect.x = 752
            self.speed = 0
        self.sprites()[0].rect.move_ip(self.speed, 0)

class EnnemyArmy(pygame.sprite.Group):
    def __init__(self, unit, rows, columns, unit_size_factor, level):
        super().__init__()
        self.unit_size = int((settings.UNITS_SIZE * unit_size_factor) / 100)
        self.dXn = 0
        self.dXn_m1 = 0
        self.dY = 0
        self.difficulty = settings.DIFFICULTY[level]

        for j in range(0, rows):
            for i in range(0, columns):
                enemy = unit(((0, 0), (self.unit_size, self.unit_size)))
                enemy.rect.center = ((3*settings.SCREEN_SIZE[0] // 4 ) - (1.25*self.unit_size))\
                                    - (((1.25*self.unit_size)*(columns//2)) - ((1.25*self.unit_size) * i))\
                                    , (1.25*self.unit_size) + ((1.25*self.unit_size) * j)
                self.add(enemy)
        logger.debug(settings.Fore.MAGENTA + f"{self.sprites()}")

    def update(self):
        self.dXn_m1 = self.dXn
        self.dXn = ((settings.SCREEN_SIZE[0]-settings.UNITS_SIZE) / 100) * math.cos(pygame.time.get_ticks() / 700)
        if self.dXn * self.dXn_m1 < 0:
            self.dY = 1
        else:
            self.dY = 0
        logger.debug(settings.Fore.BLUE + f'{self.dXn} | {self.dXn * self.dXn_m1} | {self.dY}')
        for enemy in self.sprites():
            enemy.rect.move_ip(self.difficulty['speedX'] * self.dXn, self.dY * self.difficulty['speedY'])

class SpaceOcto(pygame.sprite.Sprite):
    def __init__(self, rect):
        super().__init__()
        self.rect = pygame.Rect(rect)
        self.size = rect[1]
        self.image = pygame.transform.scale(settings.GRAPHIC_OBJECTS.space_octo, self.size)
        self.dX = 0
        self.dY = 0

class Dying(pygame.sprite.Group):
        def __init__(self):
            super().__init__()

        def died(self, unit):
            unit.image = pygame.transform.scale(settings.GRAPHIC_OBJECTS.ink_stain, unit.size)
            unit.timer = int(0.618 * settings.FPS)
            self.add(unit)


        def update(self):
            for unit in self.sprites():
                unit.dX -= 0.1
                unit.dY -= 0.1
                if unit.timer > 0:
                    if unit.rect[2] < 1.4 * unit.size[0]:
                        unit.rect.inflate_ip(0.1 * unit.size[0], 0.1 * unit.size[1])
                        unit.image = pygame.transform.scale(unit.image, (unit.rect[2], unit.rect[3]))
                    unit.rect.move_ip(unit.dX, unit.dY)
                    unit.timer -= 1
                if unit.timer == 0:
                    unit.kill()


class Arrows(pygame.sprite.Group):
    class Arrow(pygame.sprite.Sprite):
        def __init__(self, rect, surf):
            super().__init__()
            self.rect = rect
            self.image = surf
            self.hit = False
        def update(self):
            if self.rect.y <= 0:
                self.kill()
            else:
                self.rect.move_ip(0, self.groups()[0].speed)


    def __init__(self, ammo_size_factor):
        super().__init__()
        self.ammo_size = int((settings.UNITS_SIZE * ammo_size_factor) / 100)
        self.ammo_surf = pygame.transform.scale(settings.GRAPHIC_OBJECTS.arrow, (self.ammo_size, self.ammo_size))
        self.speed = -6.66
        self.max_ammo = 7
        self.shot_fired = False

    def fireShot(self, player_rect, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if len(self.sprites()) < self.max_ammo and self.shot_fired is False:
                    shot = self.Arrow(pygame.Rect(player_rect.x, player_rect.y - 34, 15, 22), self.ammo_surf)
                    self.add(shot)
                    self.shot_fired = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.shot_fired = False



