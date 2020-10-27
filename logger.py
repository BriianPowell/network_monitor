import logging
import sys

logger = logging.getLogger('hardware-monitor')
logger.setLevel(logging.DEBUG)
stdout = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%dT%H:%M:%S')
stdout.setFormatter(formatter)
logger.addHandler(stdout)