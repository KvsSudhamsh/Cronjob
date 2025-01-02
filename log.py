import logging

def logger(name=None):
    log = logging.getLogger(name)
    log.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fileHandler = logging.FileHandler('log.txt')
    fileHandler.setLevel(logging.INFO)
    fileHandler.setFormatter(formatter)
    log.addHandler(fileHandler)
    return log
