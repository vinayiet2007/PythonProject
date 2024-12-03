import logging
from logging.handlers import RotatingFileHandler
from common.interfaces.iLogger import ILogger

class Logger(ILogger):
    logger = logging.getLogger("StaticLogger")
    logger.setLevel(logging.DEBUG)
    file_handler = RotatingFileHandler("../../logs/project.log", maxBytes=20000, backupCount=5)
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(filename)s:%(lineno)d - %(funcName)s - %(levelname)s - %(message)s')

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    @staticmethod
    def info(log_message:str):
        Logger.logger.info(log_message, stacklevel=2)

    @staticmethod
    def debug(log_message:str):
        Logger.logger.debug(log_message, stacklevel=3)

    @staticmethod
    def warn(log_message:str):
        Logger.logger.warning(log_message, stacklevel=3)

    @staticmethod
    def critical(log_message:str):
        Logger.logger.critical(log_message, stacklevel=3)


if __name__=='__main__':
    Logger.info("Button Clicked")
    Logger.warn("Button Not found")
    Logger.debug("Button is in debug mode")
    Logger.critical("Button is Critical to find")