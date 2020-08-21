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


class Weapon(pygame.sprite.Group):
    class Ammo(pygame.sprite.Sprite):
        def __init__(self, rect, surf):
            super().__init__()
            self.rect = rect
            self.image = surf

        def update(self):
            if self.rect.y <= 0:
                self.kill()
            else:
                self.rect.move_ip(0, self.groups()[0].ammo_speed)


    def __init__(self, ammo_size_factor, hero):
        super().__init__()
        self.hero = hero
        self.levels = {
            '0': {'name': 'Arrow',
                  'image': 'settings.IMAGE_LOADER.arrow',
                  'size': 1,
                  'speed': -3.33,
                  'rate': 1.2,
                  'max_ammo': 6,
                  'damage': 5},
            '1': {'name': 'Rock',
                  'image': 'settings.IMAGE_LOADER.rock',
                  'size': 1.3,
                  'speed': -3.33,
                  'rate': 1.2,
                  'max_ammo': 5,
                  'damage': 5}
        }
        self.ammo_size = int((settings.UNITS_SIZE * ammo_size_factor) / 100) * self.levels[str(self.hero.earth)]['size']
        self.ammo_image = self.levels[str(self.hero.earth)]['image']
        self.ammo_surf = pygame.transform.scale(eval(self.ammo_image), (self.ammo_size, self.ammo_size))
        self.ammo_speed = self.levels[str(self.hero.earth)]['speed'] * self.hero.ammo_speed
        self.attack_rate = self.levels[str(self.hero.earth)]['rate'] * self.hero.attack_rate
        self.max_ammo = self.levels[str(self.hero.earth)]['max_ammo'] + self.hero.max_ammo
        self.damage = self.hero.damage
        self.shot_fired = False

    def fireShot(self, player_rect, event):
        if event.key == pygame.K_a:
            if len(self.sprites()) < self.max_ammo:
                if self.shot_fired is False:
                    shot = self.Ammo(pygame.Rect(player_rect.x, player_rect.y - player_rect[3], self.ammo_size, self.ammo_size), self.ammo_surf)
                    self.add(shot)
                    self.shot_fired = self.attack_rate

    def update(self):
        for ammo in self.sprites():
            ammo.update()
        if self.shot_fired > 0:
            self.shot_fired -= 0.1
        elif self.shot_fired <= 0:
            self.shot_fired = False