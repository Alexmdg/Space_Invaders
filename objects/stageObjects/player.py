import math
import ujson
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


class Player(pygame.sprite.Group):
    class BasePlayer(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.transform.scale(settings.IMAGE_LOADER.base_player, (settings.UNITS_SIZE, settings.UNITS_SIZE))
            self.rect = pygame.Rect((settings.SCREEN_SIZE[0] / 2) - 12, settings.SCREEN_SIZE[1] - settings.UNITS_SIZE * 1.2, settings.UNITS_SIZE,
                                    settings.UNITS_SIZE)
    def __init__(self, hero):
        super().__init__()
        self.hero = hero
        self.dX = 0
        self.dY = 0
        self.alive = True
        player = self.BasePlayer()
        self.add(player)
        self.jump_cooldown = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and abs(self.dX) < self.hero.max_speed:
            self.dX -= 0.5
        if keys[pygame.K_RIGHT]and self.dX < self.hero.max_speed:
            self.dX += 0.5
        if keys[pygame.K_LEFT] and self.dX > -0.2:
            self.dX -= 0.6
        if keys[pygame.K_RIGHT] and self.dX < 0.2:
            self.dX += 0.6
        if keys[pygame.K_LEFT] == 0 and self.dX < 0:
            self.dX += 0.8
        if keys[pygame.K_RIGHT] == 0 and self.dX > 0:
            self.dX -= 0.8

        if self.sprites()[0].rect.y <= (settings.SCREEN_SIZE[1] - (1.8 * settings.UNITS_SIZE)) * self.hero.max_jump:
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
        self.sprites()[0].rect.move_ip(self.dX * self.hero.speed, -(self.dY))


class PlayerStats:
    def __init__(self, datas):
        self.level = datas['level']
        self.life = datas['life']
        self.max_speed = datas['max_speed']
        self.speed = datas['speed']
        self.max_jump = datas['max_jump']
        self.health = datas['health']
        self.shield = datas['shield']
        self.ammo_speed = datas['ammo_speed']
        self.ammo_type = datas['ammo_type']
        self.attack_rate = datas['attack_rate']
        self.freeze = datas['freeze']
        self.max_ammo = datas['max_ammo']
        self.damage = datas['damage']
        self.power_up = datas['power_up']
        self.light = datas['light']
        self.fire = datas['fire']
        self.ice = datas['ice']
        self.earth = datas['earth']
        self.stage_score = datas['stage_score']
        self.total_score = datas['total_score']
        self.kills = datas['kills']

    def save(self):
        datas = dict((key, value) for (key, value) in self.__dict__.items())
        main_logger.debug(f'{datas}')
        with open('hero.json', 'w') as f:
            f.truncate(0)
            ujson.dump(datas, f, indent=4)
        main_logger.success('Hero stats saved to "hero.json"')

    def reset(self):

        datas = {
                 "level": 1,
                 "life": 1,
                 "max_speed": 5,
                 "speed": 1,
                 "max_jump": 1,
                 "health": 1,
                 "shield": 0,
                 "ammo_speed": 1,
                 "ammo_type": 0,
                 "attack_rate": 1,
                 "freeze": 1,
                 "max_ammo": 0,
                 "damage": 10,
                 "power_up": 0,
                 "light": 0,
                 "fire": 0,
                 "ice": 0,
                 "earth": 0,
                 "stage_score": 0,
                 "total_score": 0,
                 "kills": 0
                }
        self.__init__(datas)
        with open('hero.json', 'w') as f:
            f.truncate(0)
            ujson.dump(datas, f, indent=4)
            main_logger.success('Hero stats has been reset')

    def update(self, power, sign):
        if sign == "+":
            if self.power_up >= 10:
                if power == 'Fire':
                    self.damage += (0.1*self.damage)
                    self.max_ammo += 1
                    self.attack_rate += (0.1*self.attack_rate)
                    self.fire += 1
                elif power == 'Light':
                    self.max_speed += (0.1 * self.max_speed)
                    self.speed += (0.05 * self.speed)
                    self.max_jump -= (0.05 * self.max_jump)
                    self.light += 1
                elif power == 'Ice':
                    self.shield += 1
                    self.freeze += (0.1 * self.freeze)
                    self.ammo_speed += (0.1 * self.ammo_speed)
                    self.ice += 1
                elif power == 'Earth':
                    self.ammo_type += 1
                    self.life += 1
                    self.earth += 1
                self.power_up -= 10
            else:
                pass
        if sign == '-':
            if type == 1:
                self.damage -= (0.1 * self.damage)
                self.max_ammo -= 1
                self.attack_rate -= (0.1 * self.attack_rate)
                self.fire -= 1
            elif type == 2:
                self.max_speed -= (0.1 * self.max_speed)
                self.speed -= (0.05 * self.speed)
                self.max_jump -= (0.05 * self.max_jump)
                self.light -= 1
            elif type == 3:
                self.shield -= 1
                self.freeze -= (0.1 * self.freeze)
                self.ammo_speed -= (0.1 * self.ammo_speed)
                self.ice -= 1
            elif type == 4:
                self.ammo_type -= 1
                self.life -= 1
                self.earth -= 1
            self.power_up += 10