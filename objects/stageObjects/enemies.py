import math
import settings
import pygame.rect
import pygame.sprite
import pygame.key

main_logger, event_logger, rect_logger, display_logger, sprite_logger = settings.create_loggers(__name__)
main_logger.setLevel(settings.logging.INFO)
event_logger.setLevel(settings.logging.INFO)
rect_logger.setLevel(settings.logging.INFO)
display_logger.setLevel(settings.logging.INFO)
sprite_logger.setLevel(settings.logging.INFO)

class EnemyArmy(pygame.sprite.Group):
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
        self.enemy_type = unit
        sprite_logger.debug(f'self.enemy-type: {self.enemy_type}')
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
        if self.enemy_type == SpaceBlob:
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
                                       (enemy.dYx * self.difficulty['speedX']) + (enemy.dY * self.difficulty['speedY']) + 2)
        else:
            self.dXn_m1 = self.dXn
            self.dXn = ((settings.SCREEN_SIZE[0] - settings.UNITS_SIZE) / 100) * math.cos(self.time / 700)
            if self.dXn * self.dXn_m1 < 0:
                self.dY = 1
            else:
                self.dY = 0
            rect_logger.debug(f'{self.dXn} | {self.dXn * self.dXn_m1} | {self.dY}')
            if self.enemy_type == SpaceOcto:
                for enemy in self.sprites():
                    enemy.rect.move_ip(self.difficulty['speedX'] * self.dXn, self.dY * self.difficulty['speedY'])
            elif self.enemy_type == SpaceGhost:
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
        self.pu_chances = 40
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
        self.pu_chances = 15
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
        self.pu_chances = 50
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


class AlienLaser(pygame.sprite.Sprite):
    def __init__(self):
        self.size = settings.UNITS_SIZE
        self.image = pygame.transform.scale(settings.IMAGE_LOADER.alien_laser, self.size)
        self.rect = pygame.Rect(-settings.UNITS_SIZE, settings.SCREEN_SIZE[1])