from pygame import Surface, Rect, draw, event, font
import pygame.transform
import settings

# Icons and Images made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>


main_logger, event_logger, rect_logger, display_logger, sprite_logger = settings.create_loggers(__name__)
main_logger.setLevel(settings.logging.DEBUG)
event_logger.setLevel(settings.logging.DEBUG)
rect_logger.setLevel(settings.logging.DEBUG)
display_logger.setLevel(settings.logging.DEBUG)
sprite_logger.setLevel(settings.logging.DEBUG)

class Pannel:
    def __init__(self, size):
        self.size = size
        self.image = Surface(size)
        self.rect = self.image.get_rect()

    def set_border_Color(self, color):
        draw.line(self.image, color, (0, 0), (self.size[0], 0), 3)
        draw.line(self.image, color, (0, 0), (0, self.size[1]), 3)
        draw.line(self.image, color, (self.size[0], self.size[1]), (self.size[0], 0), 3)
        draw.line(self.image, color, (self.size[0], self.size[1]), (0, self.size[1]), 3)


class Button(Pannel):
    def __init__(self, name, size, msg, font_size, event, font_color=settings.GREY):
        super().__init__(size)
        self.image.fill(settings.PURPLE)
        self.name = name
        self.text = TextLabel(size, msg, font_size, font_color)
        self.image.blit(self.text.label, self.text.rect)
        self.event = event

    def click_down(self):
        self.text.change_settings(font_size=self.text.font_size)
        self.image.blit(self.text.label, self.text.rect)

    def click_up(self):
        self.text.change_settings(font_size=self.text.font_size, font_color=settings.GREY)
        self.image.blit(self.text.label, self.text.rect)
        self.is_clicked = True
        event.post(self.event.event)


class TextLabel:
    def __init__(self, size, msg, font_size=24, color=settings.GREY):
        self.font_size = font_size
        self.msg = msg
        self.font = font.SysFont(None, self.font_size)
        self.label = self.font.render(msg, True, color)
        self.rect = self.label.get_rect()
        self.rect.center = (size[0] / 2, size[1] / 2)

    def change_settings(self, font_size=24, font_color=settings.YELLOW):
        self.font = font.SysFont(None, font_size)
        self.label = self.font.render(self.msg, True, font_color)


class ItemBoxList(Pannel):
    def __init__(self, name, side='Vertical'):
        self.name = name
        self.side = side
        self.items = []


    def createPannel(self, centerx, centery, space_between=0):
        self.space_between = space_between
        if self.side == 'Vertical':
            sizeX = 0
            sizeY = self.space_between * (len(self.items) - 1)
            for item in self.items:
                sizeX = max(sizeX, item.size[0])
                sizeY += item.size[1]

            super().__init__((sizeX, sizeY))
            self.image.fill(settings.PURPLE)
            self.rect.centerx = centerx
            self.rect.centery = centery

            pos = 0
            for item in self.items:
                item.rect.x = 0
                item.rect.y = pos
                pos += item.size[1] + self.space_between
                self.image.blit(item.image, item.rect)

    def update(self):
        self.image.fill(settings.PURPLE)
        for item in self.items:
            self.image.blit(item.image, item.rect)


class Menu(Pannel):
    def __init__(self, height_ratio=0.618, width_ratio=0.618):
        super().__init__(settings.SCREEN_SIZE)
        self.menu_body = Pannel((settings.SCREEN_SIZE[0] * height_ratio, settings.SCREEN_SIZE[1] * width_ratio))
        self.item_boxes = [ItemBoxList('mainBox')]

        self.is_running = True
        self.pos = 0
        self.background = pygame.transform.scale(settings.IMAGE_LOADER.city_background, settings.SCREEN_SIZE)
        self.image.blit(self.background, (0, 0))

        self.menu_body.rect.centerx = self.size[0] / 2
        self.menu_body.rect.centery = self.size[1] / 2
        self.menu_body.image.fill(settings.PURPLE)

        self.clock = pygame.time.Clock()
        self.count = 3
        self.time = 0
        self.image.blit(self.menu_body.image, self.menu_body.rect)


    def add_button(self, itemBox_name, name, label, event,
                   xratio=0.618, yratio=0.161,
                   font_size=48):

        button = Button(name,
                        (xratio * self.menu_body.size[0],
                         yratio * self.menu_body.size[1]),
                        label,
                        font_size,
                        event)
        for box in self.item_boxes:
            if box.name == itemBox_name:
                box.items.append(button)

    def update(self):

        for box in self.item_boxes:
            box.update()
            self.menu_body.image.blit(box.image, box.rect)
        self.image.blit(self.background, (0, 0))
        self.image.blit(self.menu_body.image, self.menu_body.rect)

    def click_down(self, button):
        button.click_down()

    def click_up(self, button):
        button.click_up()
        event_logger.debug('button clicked')
        self.is_running = False








