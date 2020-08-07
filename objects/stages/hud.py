import pygame
import os
import math
from settings import *

# Icons and Images made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>

logger = createLogger(__name__)
logger.setLevel(logging.DEBUG)

class TopBar(pygame.Surface):
    def __init__(self, level):
        size = (SCREEN_SIZE[0], 21)
        super().__init__(size)
        self.rect = pygame.Rect(0, 0, SCREEN_SIZE[0], 25)
        self.fill(PURPLE)
        size = (SCREEN_SIZE[0] / 10, 21)
        level = TopBarInfoLabel(size, 0, f"Level = {level}")
        score = TopBarInfoLabel(size, 1, f"Score = 0")
        self.blit(level, (0, 0))
        self.blit(score, (SCREEN_SIZE[0] / 10, 0))

class TopBarInfoLabel(pygame.Surface):
    def __init__(self, size, pos, msg):
        super().__init__(size)
        self.rect = pygame.Rect(((size[0] * pos), 0), size)
        self.fill(PURPLE)
        self.size = size
        self.msg = msg
        # pygame.draw.line(self, BLACK, ((size[0] * pos), 0), ((size[0] * pos), size[1]), 3)
        pygame.draw.line(self, BLACK, (size[0], 0), (size[0], size[1]), 3)
        font = pygame.font.SysFont(None, 24)
        text_label = font.render(msg, True, GREY)
        text_rect = text_label.get_rect()
        text_rect.center = (size[0]/2, size[1]/2)
        self.blit(text_label, text_rect)
