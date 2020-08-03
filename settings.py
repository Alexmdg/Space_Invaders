import logging
from colorama import Fore


LEVEL = {'1': 15,
         '2': 30,
         '3': 60}

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