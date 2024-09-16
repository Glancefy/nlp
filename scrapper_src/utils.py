import os
import time
from scrapper_src.logger import setup_logger


logger = setup_logger()


def debug_print(message, filename):
    log = f"[{time.strftime('%H:%M:%S'):>8}] {os.path.basename(filename).upper()}"
    log = f"{log:-<40}: {message}"
    logger.debug(log)
    return log
