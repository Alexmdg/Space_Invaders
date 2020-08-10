from .menuParts import *
import settings

# Icons and Images made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>

main_logger, event_logger, rect_logger, display_logger, sprite_logger = settings.create_loggers(__name__)
main_logger.setLevel(settings.logging.DEBUG)
event_logger.setLevel(settings.logging.DEBUG)
rect_logger.setLevel(settings.logging.DEBUG)
display_logger.setLevel(settings.logging.DEBUG)
sprite_logger.setLevel(settings.logging.DEBUG)

class TopBar(Pannel):
    def __init__(self, level):
        super().__init__((settings.SCREEN_SIZE[0], 0.0618 * settings.SCREEN_SIZE[1]))
        self.image.fill(settings.Purple(200))
        self.labels = []
        self.pos = 0
        self.level = self.add_label('level', f"Level = {level}")
        self.score = self.add_label('score', f"Score = 0")
        self.image.convert_alpha()
        self.image.set_alpha(200)

    def add_label(self, name, msg,
                 size=(0.144 * settings.SCREEN_SIZE[0], 0.144 * settings.SCREEN_SIZE[1]),
                 font_size=24, font_color=settings.YELLOW):
        new_label = TopBarInfoLabel(name, msg, size=size, font_size=font_size, font_color=font_color)
        self.labels.append(new_label)
        for label in self.labels:
            label.rect.centerx = self.pos + label.size[0]/2
            label.rect.centery = self.rect.centery
            self.pos += label.size[0]
        return new_label

    def update(self):
        for label in self.labels:
            self.image.blit(label.image, label.rect)



class TopBarInfoLabel(Pannel):
    def __init__(self, name, msg,
                 size=(0.144 * settings.SCREEN_SIZE[0], 0.144 * settings.SCREEN_SIZE[1]),
                 font_size=24, font_color=settings.YELLOW):
        super().__init__(size)
        self.name = name
        self.text = TextLabel(size, msg, font_size=font_size, color=font_color)
        self.image.blit(self.text.label, self.text.rect)
        self.set_border_Color(settings.YELLOW)


        # self.rect = pygame.Rect(((size[0] * pos), 0), size)
        # self.fill(settings.PURPLE)
        # self.size = size
        # self.msg = msg
        # pygame.draw.line(self, settings.BLACK, (size[0], 0), (size[0], size[1]), 3)
        # font = pygame.font.SysFont(None, 24)
        # text_label = font.render(msg, True, settings.GREY)
        # text_rect = text_label.get_rect()
        # text_rect.center = (size[0]/2, size[1]/2)
        # self.blit(text_label, text_rect)
