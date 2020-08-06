import logging
from colorama import Fore

SCREEN_SIZE = (960, 600)
UNITS_SIZE = (SCREEN_SIZE[0]*SCREEN_SIZE[0]) // 16000
FPS = 34

PURPLE = (89, 24, 204)
BLACK = (0, 0, 0)
GREY = (229, 222, 206)

DIFFICULTY = {
    '1': {'speedX': 1,
          'speedY': 15,
          'hp': 1},
    '2': {'speedX': 1,
          'speedY': 30,
          'hp': 1},
    '3': {'speedX': 1,
          'speedY': 60,
          'hp': 1},
    '4': {'speedX': 1.2,
          'speedY': 60,
          'hp': 1},
    '5': {'speedX': 1,
          'speedY': 30,
          'hp': 2},
    '6': {'speedX': 1.4,
          'speedY': 50,
          'hp': 1},
    '7': {'speedX': 1.4,
          'speedY': 50,
          'hp': 1},
    '8': {'speedX': 1.4,
          'speedY': 50,
          'hp': 1},
    '9': {'speedX': 1.4,
          'speedY': 50,
          'hp': 1},
    '10': {'speedX': 1.4,
          'speedY': 50,
          'hp': 1}
    }

####            Logging           ####
def createLogger(name, file=None,):
    logger = logging.getLogger(name)
    formatter = logging.Formatter(Fore.WHITE + '%(asctime)s:%(levelname)s:%(funcName)s:%(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    if file is True :
        filelogger = logging.getLogger(f"f_{name}")
        filehandler = logging.FileHandler(f"{name}.log")
        filehandler.setFormatter(formatter)
        filelogger.addHandler(filehandler)
        return logger, filelogger
    else:
        return logger