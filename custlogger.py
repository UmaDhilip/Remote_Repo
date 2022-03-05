# importing module
import logging

def create_logger(filename='custlogger.log',loglevel=logging.DEBUG):
        logger_name = __name__
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)

        fhnd = logging.FileHandler(filename)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')
        fhnd.setFormatter(formatter)
        logger.addHandler(fhnd)

        return logger

#logger = create_logger()
#logger.error("msg")