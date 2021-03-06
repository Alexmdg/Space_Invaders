import logging
from colorama import Fore

####            Logging           ####

class MyFormater(logging.Formatter):
    def __init__(self, fmt = Fore.WHITE + '%(asctime)s:%(levelname)s:%(name)s:%(funcName)s:%(message)s' + Fore.RESET):
        super().__init__(fmt)

class MyLogger(logging.Logger):
    def __init__(self, name, file=False, fmt=Fore.WHITE + '%(created)f:MainLogger:%(levelname)s:%(name)s:%(funcName)s:%(message)s' + Fore.RESET):
        super().__init__(name)
        formatter = MyFormater(fmt)
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        self.addHandler(handler)
        if file is True :
            filelogger = logging.getLogger(f"f_{name}")
            filehandler = logging.FileHandler(f"{name}.log")
            filehandler.setFormatter(formatter)
            filelogger.addHandler(filehandler)

    def success(self, message):
        self.info(Fore.GREEN + message)


def create_loggers(name, file=False):
    main_logger = MyLogger(name, file, fmt=Fore.BLUE + '%(created)f:Main Logger:%(levelname)s:%(name)s:%(funcName)s:%(message)s' + Fore.RESET)
    event_logger = MyLogger(name, file, fmt=Fore.YELLOW + '%(created)f:Event Logger:%(levelname)s:%(name)s:%(funcName)s:%(message)s' + Fore.RESET)
    rect_logger = MyLogger(name, file, fmt=Fore.MAGENTA + '%(created)f:Rect Logger:%(levelname)s:%(name)s:%(funcName)s:%(message)s' + Fore.RESET)
    display_logger = MyLogger(name, file, fmt=Fore.LIGHTMAGENTA_EX + '%(created)f:Display Logger:%(name)s:%(levelname)s:%(funcName)s:%(message)s' + Fore.RESET)
    sprite_logger = MyLogger(name, file, fmt=Fore.CYAN + '%(created)f:Sprite Logger:%(levelname)s:%(name)s:%(funcName)s:%(message)s' + Fore.RESET)
    return main_logger, event_logger, rect_logger, display_logger, sprite_logger

####            Graphic Options          ####

SCREEN_SIZE = (960, 600)
UNITS_SIZE = int((SCREEN_SIZE[0]*SCREEN_SIZE[1]) // 10000)
FPS = 34

def Purple(a=255): return (89, 24, 204, a)
def Black(a=255): return (0, 0, 0, a)
def Red(a=255): return (243, 39, 22, a)
def Grey(a=255): return(229, 222, 206, a)
def Yellow(a=255): return(245, 191, 48, a)
def Orange(a=255): return(249, 157, 45, a)
def White(a=255): return(255, 255, 255, a)

PURPLE = Purple()
BLACK = Black()
GREY = Grey()
YELLOW = Yellow()
ORANGE = Orange()

IMAGE_LOADER = None


####            Gameplay Settings           ####

DIFFICULTY = {
    '1': {'speedX': 1,
          'speedY': 28,
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

