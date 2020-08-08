import math
import settings
from objects.graphics.graphicObjects import *

# Icons and Images made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>


main_logger, event_logger, rect_logger, display_logger = settings.create_loggers(__name__)
main_logger.setLevel(settings.logging.DEBUG)
event_logger.setLevel(settings.logging.DEBUG)
rect_logger.setLevel(settings.logging.DEBUG)
display_logger.setLevel(settings.logging.DEBUG)

class Player(pygame.sprite.Group):
    class BasePlayer(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.transform.scale(settings.IMAGE_LOADER.base_player, (settings.UNITS_SIZE, settings.UNITS_SIZE))
            self.rect = pygame.Rect((settings.SCREEN_SIZE[0] / 2) - 12, settings.SCREEN_SIZE[1] - settings.UNITS_SIZE * 1.2, settings.UNITS_SIZE,
                                    settings.UNITS_SIZE)
    def __init__(self):
        super().__init__()
        self.max_speed = 5
        self.speed = 0
        self.health = 1
        self.shield = 0
        self.dX = 0
        self.dY = 0
        self.power_up = 0
        self.alive = True
        player = self.BasePlayer()
        self.add(player)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and abs(self.dX) < self.max_speed:
            self.dX -= 0.2
        if keys[pygame.K_RIGHT]and self.dX < self.max_speed:
            self.dX += 0.2
        if keys[pygame.K_LEFT] and self.dX > -0.2:
            self.dX -= 0.4
        if keys[pygame.K_RIGHT] and self.dX < 0.2:
            self.dX += 0.4
        if keys[pygame.K_LEFT] == 0 and self.dX < 0:
            self.dX += 0.6
        if keys[pygame.K_RIGHT] == 0 and self.dX > 0:
            self.dX -= 0.6
        if self.sprites()[0].rect.x < 0:
            self.sprites()[0].rect.x = 0
            self.dX = 0
        elif self.sprites()[0].rect.x > settings.SCREEN_SIZE[0] - settings.UNITS_SIZE:
            self.sprites()[0].rect.x = settings.SCREEN_SIZE[0] - settings.UNITS_SIZE
            self.dX = 0
        self.sprites()[0].rect.move_ip(self.dX + self.speed, 0)

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
        display_logger.debug(f"{self.sprites()}")

    def update(self):
        self.dXn_m1 = self.dXn
        self.dXn = ((settings.SCREEN_SIZE[0]-settings.UNITS_SIZE) / 100) * math.cos(pygame.time.get_ticks() / 700)
        if self.dXn * self.dXn_m1 < 0:
            self.dY = 0.5
        else:
            self.dY = 0
        rect_logger.debug(f'{self.dXn} | {self.dXn * self.dXn_m1} | {self.dY}')
        for enemy in self.sprites():
            enemy.rect.move_ip(self.difficulty['speedX'] * self.dXn, self.dY * self.difficulty['speedY'])

class SpaceOcto(pygame.sprite.Sprite):
    def __init__(self, rect):
        super().__init__()
        self.rect = pygame.Rect(rect)
        self.power_up = False
        self.size = rect[1]
        self.image = pygame.transform.scale(settings.IMAGE_LOADER.space_octo, self.size)
        self.X = 0
        self.Y = 0
        self.dX = 0
        self.dY = 0

class Weapon(pygame.sprite.Group):
    class Arrow(pygame.sprite.Sprite):
        def __init__(self, rect, surf):
            super().__init__()
            self.rect = rect
            self.image = surf
        def update(self):
            if self.rect.y <= 0:
                self.kill()
            else:
                self.rect.move_ip(0, self.groups()[0].ammo_speed)

    def __init__(self, ammo_size_factor):
        super().__init__()
        self.ammo_size = int((settings.UNITS_SIZE * ammo_size_factor) / 100)
        self.ammo_surf = pygame.transform.scale(settings.IMAGE_LOADER.arrow, (self.ammo_size, self.ammo_size))
        self.ammo_speed = -6.66
        self.attack_rate = 2
        self.max_ammo = 7
        self.damage = 1
        self.shot_fired = False

    def fireShot(self, player_rect, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if len(self.sprites()) < self.max_ammo:
                    if self.shot_fired is False:
                        shot = self.Arrow(pygame.Rect(player_rect.x, player_rect.y - 34, 15, 22), self.ammo_surf)
                        self.add(shot)
                        self.shot_fired = self.attack_rate

    def update(self):
        for ammo in self.sprites():
            ammo.update()
        if self.shot_fired > 0:
            self.shot_fired -= 1
        elif self.shot_fired == 0:
            self.shot_fired = False