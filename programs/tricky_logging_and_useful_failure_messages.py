import logging
counter = []
def expensive():
    counter.append(1)
    return "details"
logger = logging.getLogger("tricky_logging")
logger.setLevel(logging.WARNING)
logger.debug("Value: %s", expensive())
print(len(counter))
