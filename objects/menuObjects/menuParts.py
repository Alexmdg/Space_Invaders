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

class Menu:
    def __init__(self, height_ratio=0.618, width_ratio=0.618):
        self.is_running = True
        self.buttons = []
        self.body = Pannel(settings.SCREEN_SIZE)
        self.background = pygame.transform.scale(settings.IMAGE_LOADER.city_background, settings.SCREEN_SIZE)
        self.body.image.blit(self.background, (0, 0))
        self.menu_bg = Pannel((settings.SCREEN_SIZE[0] * height_ratio, settings.SCREEN_SIZE[1] * width_ratio))
        self.menu_bg.rect.centerx = settings.SCREEN_SIZE[0] / 2
        self.menu_bg.rect.centery = settings.SCREEN_SIZE[1] / 2
        self.menu_bg.image.fill(settings.PURPLE)
        self.clock = pygame.time.Clock()
        self.count = 3
        self.time = 0
        self.body.image.blit(self.menu_bg.image, self.menu_bg.rect)
        for button in self.buttons:
            self.body.image.blit(button.body.image, button.body.rect)

    def update(self):
        self.body.image.blit(self.menu_bg.image, self.menu_bg.rect)
        for button in self.buttons:
            self.body.image.blit(button.body.image, button.body.rect)

    def click_down(self, button):
        button.click_down()

    def click_up(self, button):
        button.click_up()
        event_logger.debug('button clicked')
        self.is_running = False

class Pannel:
    def __init__(self, size):
        self.size = size
        self.image = Surface(size)
        self.rect = Rect((0, 0), size)
        self.rect.center = (size[0]/2, size[1]/2)

    def set_border_Color(self, color):
        draw.line(self.image, color, (0, 0), (self.size[0], 0), 3)
        draw.line(self.image, color, (0, 0), (0, self.size[1]), 3)
        draw.line(self.image, color, (self.size[0], self.size[1]), (self.size[0], 0), 3)
        draw.line(self.image, color, (self.size[0], self.size[1]), (0, self.size[1]), 3)


class Button:
    def __init__(self, size, msg, font_size, event, font_color=settings.YELLOW):
        self.body = Pannel(size)
        self.body.image.fill(settings.PURPLE)
        self.text = TextLabel(size, msg, font_size, font_color)
        self.body.image.blit(self.text.label, self.text.rect)
        self.event = event

    def click_down(self):
        self.text.change_settings(font_size=self.text.font_size)

        self.body.image.blit(self.text.label, self.text.rect)

    def click_up(self):
        self.text.change_settings(font_size=self.text.font_size, font_color=settings.YELLOW)
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

    def change_settings(self, font_size=24, font_color=settings.GREY):
        self.font = font.SysFont(None, font_size)
        self.label = self.font.render(self.msg, True, font_color)





