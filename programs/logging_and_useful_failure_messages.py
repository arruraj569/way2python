import logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger("automation")
expected, actual = 201, 201
logger.info("create user: expected=%s actual=%s", expected, actual)
assert actual == expected, f"create user returned {actual}; expected {expected}"
