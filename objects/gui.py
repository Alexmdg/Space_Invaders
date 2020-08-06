import pygame
import os
import math
from settings import *

# Icons and Images made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>


logger = createLogger(__name__)
logger.setLevel(logging.DEBUG)


# class IGMenu(pygame.Surface):
#     def __init__(self, level):
#         size = (800, 21)
#         super().__init__(size)
#         self.rect = pygame.Rect(0, 0, 800, 25)
#         self.fill(PURPLE)
#         size = (76, 21)
#         level = TopBarInfoLabel(size, 0, f"Level = {level}")
#         score = TopBarInfoLabel(size, 1, f"Score = 0")
#         self.blit(level, (0, 0))
#         self.blit(score, (76, 0))
#
#
# def show_ingameMenu(event):
#     if event.type == pygame.KEYDOWN:
#         if event.key == pygame.K_ESCAPE:
