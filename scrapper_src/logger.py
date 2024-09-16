import logging
import sys


def setup_logger():
    log_file = "log/scrapper_src.log"

    # put every stdout and stderr to log file and console
    # use logging module for it
    # create a logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # create a file handler
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)

    # create a stream handler
    sh = logging.StreamHandler(sys.stdout)
    sh.setLevel(logging.DEBUG)

    # create a formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # add formatter to handlers
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)

    # add handlers
    logger.addHandler(fh)
    logger.addHandler(sh)

    # append 80*= to log/scrapper_src with current time
    message = "START PROGRAM"
    logger.debug(f"{'='*80}")
    logger.debug(f"{message:^80}")
    logger.debug(f"{'='*80}")

    return logger
