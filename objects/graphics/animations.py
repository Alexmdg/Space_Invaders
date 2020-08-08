from pygame import transform
from pygame.sprite import Group
import settings
import random

class Dying(Group):
    def __init__(self):
        super().__init__()

    def died(self, unit):
        if random.randint(0, 48) == 0:
            unit.image = transform.scale(settings.IMAGE_LOADER.power_up, (int(0.618 * unit.size[0]), int(0.618 * unit.size[1])))
            unit.power_up = True
        else:
            unit.image = transform.scale(settings.IMAGE_LOADER.ink_stain, unit.size)
            unit.timer = int(0.618 * settings.FPS)
        self.add(unit)

    def update(self):
        for unit in self.sprites():
            if not unit.power_up:
                unit.dX -= 0.1
                unit.dY -= 0.1
                if unit.timer > 0:
                    if unit.rect[2] < 1.4 * unit.size[0]:
                        unit.rect.inflate_ip(0.1 * unit.size[0], 0.1 * unit.size[1])
                        unit.image = transform.scale(unit.image, (unit.rect[2], unit.rect[3]))
                    unit.rect.move_ip(unit.dX, unit.dY)
                    unit.timer -= 1
                if unit.timer == 0:
                    unit.kill()
            else:
                unit.dX = 1.3
                unit.X += unit.dX
                unit.dY = ((unit.X * unit.X)//100)-2
                if unit.rect[0] >= 0:
                    unit.rect.move_ip(unit.dX, unit.dY)
                else:
                    unit.kill()


class colickedButton:
    pass