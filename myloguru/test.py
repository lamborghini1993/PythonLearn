
import time
import sys

from loguru import logger

logger.add("test1.log", rotation="5 seconds", retention=3)
logger.add("test2.log", rotation="1 KB", retention=3)

flag = sys.argv[1]

for i in range(123):
    time.sleep(0.1)
    logger.info(f"send {flag} message {i}")

