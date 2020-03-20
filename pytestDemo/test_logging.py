import logging


def test_logging_demo():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.INFO)

    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("something is in warning mode")
    logger.error("A Major error has happend")
    logger.critical("Critical issue")