from pygame import Surface, Rect, draw, event, font
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
        self.rect = Rect((0, 0), size)
        self.rect.center = (size[0]/2, size[1]/2)

    def set_border_Color(self, color):
        draw.line(self.image, color, (0, 0), (self.size[0], 0), 3)
        draw.line(self.image, color, (0, 0), (0, self.size[1]), 3)
        draw.line(self.image, color, (self.size[0], self.size[1]), (self.size[0], 0), 3)
        draw.line(self.image, color, (self.size[0], self.size[1]), (0, self.size[1]), 3)


# class VerticalButtons:
#     def __init__(self, size):
#         self.buttons = []
#         self.body = Pannel(size)
#         self.body.image.fill(settings.PURPLE)
#         self.body.set_border_Color(settings.YELLOW)
#
#     def add_button(self, size, msg, font_size, event):
#         self.body.image.fill(settings.PURPLE)
#         self.body.set_border_Color(settings.YELLOW)
#         button = Button(size, msg, font_size, event)
#         self.buttons.append(button)
#         list_size = self.body.size[1]
#         space_between = (list_size - sum([elem.body.size[1] for elem in self.buttons]))/(len(self.buttons)+1)
#         for elem in self.buttons:
#             elem.body.rect.center = ((self.body.size[0] / 2)-(elem.body.size[0]/2), (self.buttons.index(elem) * space_between) + space_between)
#             self.body.image.blit(elem.body.image, elem.body.rect.center)


class Button:
    def __init__(self, size, msg, font_size, event):
        self.body = Pannel(size)
        self.body.image.fill(settings.PURPLE)
        self.body.set_border_Color(settings.YELLOW)
        self.text = TextLabel(size, msg, font_size)
        self.body.image.blit(self.text.label, self.text.rect)
        self.is_clicked = False
        self.event = event

    def clicked(self):
        self.is_clicked = True
        self.body.set_border_Color(settings.ORANGE)
        event.post(self.event.event)


class TextLabel:
    def __init__(self, size, msg, font_size):
        self.font_size = font_size
        self.msg = msg
        self.font = font.SysFont(None, self.font_size)
        self.label = self.font.render(msg, True, settings.GREY)
        self.rect = self.label.get_rect()
        self.rect.center = (size[0] / 2, size[1] / 2)




