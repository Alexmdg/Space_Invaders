import pygame
import os
import math
from settings import *

# Icons and Images made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>


logger = createLogger(__name__)
logger.setLevel(logging.DEBUG)

class Player(pygame.sprite.Group):
    class BasePlayer(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.transform.scale(
                pygame.image.load(os.path.join('images\\', 'soldier.png')).convert_alpha(),
                (UNITS_SIZE, UNITS_SIZE)
            )
            self.rect = pygame.Rect((SCREEN_SIZE[0] / 2) - 12, SCREEN_SIZE[1] - UNITS_SIZE * 1.2, UNITS_SIZE,
                                    UNITS_SIZE)
    def __init__(self):
        super().__init__()
        self.surf = pygame.transform.scale(
                            pygame.image.load(os.path.join('images\\', 'soldier.png')).convert_alpha(),
                            (UNITS_SIZE, UNITS_SIZE)
                        )

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
    class SpaceOcto(pygame.sprite.Sprite):
        def __init__(self, rect, surf):
            super().__init__()
            self.rect = pygame.Rect(rect)
            self.image = surf

    def __init__(self, rows, columns, unit_size_factor, level):
        super().__init__()
        self.unit_size = int((UNITS_SIZE * unit_size_factor) / 100)
        self.unit_surf = pygame.transform.scale(
                    pygame.image.load(os.path.join('images\\', 'ennemy.png')).convert_alpha(),
                    (self.unit_size, self.unit_size)
                )
        self.dXn = 0
        self.dXn_m1 = 0
        self.dY = 0
        self.difficulty = DIFFICULTY[level]

        for j in range(0, rows):
            for i in range(0, columns):
                enemy = self.SpaceOcto(((0, 0), (UNITS_SIZE, UNITS_SIZE)), self.unit_surf)
                enemy.rect.center = ((3*SCREEN_SIZE[0] // 4 ) - (1.25*self.unit_size))\
                                    - (((1.25*self.unit_size)*(columns//2)) - ((1.25*self.unit_size) * i))\
                                    , (1.25*self.unit_size) + ((1.25*self.unit_size) * j)
                self.add(enemy)
        logger.debug(Fore.MAGENTA + f"{self.sprites()}")


    def update(self):
        self.dXn_m1 = self.dXn
        self.dXn = ((SCREEN_SIZE[0]-UNITS_SIZE) / 100) * math.cos(pygame.time.get_ticks() / 700)
        if self.dXn * self.dXn_m1 < 0:
            self.dY = 1
        else:
            self.dY = 0
        logger.debug(Fore.BLUE + f'{self.dXn} | {self.dXn * self.dXn_m1} | {self.dY}')
        for enemy in self.sprites():
            enemy.rect.move_ip(self.difficulty['speedX'] * self.dXn, self.dY * self.difficulty['speedY'])


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
        self.ammo_size = int((UNITS_SIZE * ammo_size_factor) / 100)
        self.ammo_surf = pygame.transform.scale(
                            pygame.image.load(os.path.join('images\\', 'spear.png')).convert_alpha(),
                            (self.ammo_size, self.ammo_size)
                    )
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



