import logging
from colorama import Fore


DIFFICULTY = {
    '1': {'speedX': 1,
          'speedY': 15,
          'hp': 1},
    '2': {'speedX': 1.2,
          'speedY': 30,
          'hp': 1},
    '3': {'speedX': 1.4,
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