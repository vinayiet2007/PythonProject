import logging
from logging.handlers import RotatingFileHandler
from common.ui.interfaces.iLogger import ILogger
import os
from pathlib import Path

class Logger(ILogger):
    project_root = Path(__file__).resolve().parent
    while project_root != project_root.root and not (project_root / ".git").exists():
        project_root = project_root.parent
    log_folder = os.path.join(project_root, "logs")
    os.makedirs(log_folder, exist_ok=True)
    log_file_path = os.path.join(log_folder, "project.log")
    logger = logging.getLogger("StaticLogger")
    logger.setLevel(logging.DEBUG)
    file_handler = RotatingFileHandler(log_file_path, maxBytes=20000, backupCount=5)
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

#########################################################
if __name__=='__main__':
    Logger.info("Button Clicked")
    Logger.warn("Button Not found")
    Logger.debug("Button is in debug mode")
    Logger.critical("Button is Critical to find")