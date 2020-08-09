import math
import settings
import random
import pygame.rect
import pygame.sprite
import pygame.key


# Icons and Images made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>

main_logger, event_logger, rect_logger, display_logger, sprite_logger = settings.create_loggers(__name__)
main_logger.setLevel(settings.logging.DEBUG)
event_logger.setLevel(settings.logging.DEBUG)
rect_logger.setLevel(settings.logging.INFO)
display_logger.setLevel(settings.logging.INFO)
sprite_logger.setLevel(settings.logging.INFO)

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
        self.jump_cooldown = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and abs(self.dX) < self.max_speed:
            self.dX -= 0.5
        if keys[pygame.K_RIGHT]and self.dX < self.max_speed:
            self.dX += 0.5
        if keys[pygame.K_LEFT] and self.dX > -0.2:
            self.dX -= 0.6
        if keys[pygame.K_RIGHT] and self.dX < 0.2:
            self.dX += 0.6
        if keys[pygame.K_LEFT] == 0 and self.dX < 0:
            self.dX += 0.8
        if keys[pygame.K_RIGHT] == 0 and self.dX > 0:
            self.dX -= 0.8

        if self.sprites()[0].rect.y <= settings.SCREEN_SIZE[1] - (1.8 * settings.UNITS_SIZE):
            self.jump_cooldown = True
        if keys[pygame.K_SPACE] and not self.jump_cooldown:
            self.dY = 5
        if (keys[pygame.K_SPACE] == 0 and self.sprites()[0].rect.y < settings.SCREEN_SIZE[1] - (settings.UNITS_SIZE * 1.2) - 1)\
            or (self.jump_cooldown and self.sprites()[0].rect.y < settings.SCREEN_SIZE[1] - (settings.UNITS_SIZE * 1.2) - 1):
            self.dY -= 3
        if self.sprites()[0].rect.x < 0:
            self.sprites()[0].rect.x = 0
            self.dX = 0
        elif self.sprites()[0].rect.x > settings.SCREEN_SIZE[0] - settings.UNITS_SIZE:
            self.sprites()[0].rect.x = settings.SCREEN_SIZE[0] - settings.UNITS_SIZE
            self.dX = 0
        if self.sprites()[0].rect.y > settings.SCREEN_SIZE[1] - settings.UNITS_SIZE * 1.2:
            self.sprites()[0].rect.y = settings.SCREEN_SIZE[1] - settings.UNITS_SIZE * 1.2
            self.dY = 0
            self.jump_cooldown = False
        if self.sprites()[0].rect.y <= settings.SCREEN_SIZE[1] - (1.8 * settings.UNITS_SIZE):
            if self.dY > 0:
                self.dY = 0
            else:
                self.dY -= 1
        self.sprites()[0].rect.move_ip(self.dX + self.speed, -self.dY)


class EnnemyArmy(pygame.sprite.Group):
    def __init__(self, unit, rows, columns, unit_size_factor, level):
        super().__init__()
        self.unit_size = int((settings.UNITS_SIZE * unit_size_factor) / 100)
        self.dXn = 0
        self.dXn_m1 = 0
        self.dY = 0
        self.dYx = 0
        self.difficulty = settings.DIFFICULTY[level]
        self.clock = pygame.time.Clock()
        self.time = 0
        self.ennemy_type = unit
        sprite_logger.debug(f'self.ennemy-type: {self.ennemy_type}')
        for j in range(0, rows):
            for i in range(0, columns):
                enemy = unit(((0, 0), (self.unit_size, self.unit_size)))
                enemy.rect.center = ((settings.SCREEN_SIZE[0] // 2 ) + (self.unit_size // 4))\
                                    - (((1.25*self.unit_size)*(columns//2)) - ((1.25*self.unit_size) * i))\
                                    , (1.25*self.unit_size) + ((1.25*self.unit_size) * j)
                self.add(enemy)
        sprite_logger.debug(f"self.sprites(): {self.sprites()}")
        for enemy in self.sprites():
            if self.sprites().index(enemy) % 2 == 0:
                enemy.wave = 1

    def update(self):
        self.clock.tick()
        if self.clock.get_time() < 35:
            self.time += self.clock.get_time()
        display_logger.debug(f'clock time: {self.clock.get_time()}, self.time: {self.time}, self.dY: {self.dY}')
        if self.ennemy_type == SpaceBlob:
            sprite_logger.debug(f'enemies list : {self.sprites()}')
            for enemy in self.sprites():
                sprite_logger.debug(f'enemy index : {self.sprites().index(enemy)}')
                if enemy.wave == 0:
                    enemy.dXn_m1 = enemy.dXn
                    enemy.dXn = ((settings.SCREEN_SIZE[0] - settings.UNITS_SIZE) / 100) * math.cos(self.time / 1000)
                    if enemy.dXn * enemy.dXn_m1 < 0:
                        enemy.dY = 1
                    else:
                        enemy.dY = 0
                    rect_logger.debug(f'{enemy.dXn} | {enemy.dXn * enemy.dXn_m1} | {enemy.dY}')
                    enemy.dYx = ((settings.SCREEN_SIZE[1] - settings.UNITS_SIZE) / 55)\
                                * ((math.sin(self.time / 700))*(math.sin(self.time / 350)))
                    enemy.rect.move_ip(self.difficulty['speedX'] * enemy.dXn,
                                    (enemy.dYx * self.difficulty['speedX'])+(enemy.dY * self.difficulty['speedY'])+ 2)
                else:
                    enemy.dXn_m1 = enemy.dXn
                    enemy.dXn = ((settings.SCREEN_SIZE[0] - settings.UNITS_SIZE) / 100) * (-math.cos(self.time / 1000))
                    if enemy.dXn * enemy.dXn_m1 < 0:
                        enemy.dY = 1
                    else:
                        enemy.dY = 0
                    rect_logger.debug(f'{enemy.dXn} | {enemy.dXn * enemy.dXn_m1} | {enemy.dY}')
                    enemy.dYx = ((settings.SCREEN_SIZE[1] - settings.UNITS_SIZE) / 55)\
                                * ((math.sin(self.time / 700))*(math.sin(self.time / 350)))
                    enemy.rect.move_ip(self.difficulty['speedX'] * enemy.dXn,
                                       (enemy.dYx * self.difficulty['speedX']) + (enemy.dY * self.difficulty['speedY'])+ 2)
        else:
            self.dXn_m1 = self.dXn
            self.dXn = ((settings.SCREEN_SIZE[0] - settings.UNITS_SIZE) / 100) * math.cos(self.time / 700)
            if self.dXn * self.dXn_m1 < 0:
                self.dY = 1
            else:
                self.dY = 0
            rect_logger.debug(f'{self.dXn} | {self.dXn * self.dXn_m1} | {self.dY}')
            if self.ennemy_type == SpaceOcto:
                for enemy in self.sprites():
                    enemy.rect.move_ip(self.difficulty['speedX'] * self.dXn, self.dY * self.difficulty['speedY'])
            elif self.ennemy_type == SpaceGhost:
                for enemy in self.sprites():
                    if self.sprites().index(enemy) % 2 == 0 :
                        enemy.dYx = ((settings.SCREEN_SIZE[1] - settings.UNITS_SIZE) / 88) * math.cos(self.time/ 350)
                        enemy.rect.move_ip(self.difficulty['speedX'] * self.dXn,
                                        (enemy.dYx * self.difficulty['speedX'])+(self.dY * self.difficulty['speedY']))
                    else:
                        enemy.dYx = ((settings.SCREEN_SIZE[1] - settings.UNITS_SIZE) / 88) * math.cos(1750 + self.time/ 350)
                        enemy.rect.move_ip(self.difficulty['speedX'] * self.dXn,
                                        (enemy.dYx * self.difficulty['speedX'])+(self.dY * self.difficulty['speedY']))


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
        self.wave = 0

class SpaceGhost(pygame.sprite.Sprite):
    def __init__(self, rect):
        super().__init__()
        self.rect = pygame.Rect(rect)
        self.power_up = False
        self.size = rect[1]
        self.image = pygame.transform.scale(settings.IMAGE_LOADER.space_ghost, self.size)
        self.X = 0
        self.Y = 0
        self.dX = 0
        self.dY = 0
        self.dYx = 0
        self.wave = 0

class SpaceBlob(pygame.sprite.Sprite):
    def __init__(self, rect):
        super().__init__()
        self.rect = pygame.Rect(rect)
        self.power_up = False
        self.size = rect[1]
        self.image = pygame.transform.scale(settings.IMAGE_LOADER.space_blob, self.size)
        self.dX = 0
        self.X = 0
        self.Y = 0
        self.dY = 0
        self.dXn = 0
        self.dXn_m1 = 0
        self.dY = 0
        self.dYx = 0
        self.wave = 0

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
            if event.key == pygame.K_a:
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
