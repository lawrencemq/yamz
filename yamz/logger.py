import logging

FORMAT = '%(name)s - %(message)s'

logging.basicConfig(format=FORMAT)

logger = logging.getLogger("yamz")
logger.setLevel(logging.INFO)
