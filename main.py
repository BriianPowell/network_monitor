import logging
import logger

from monitoring import start_monitoring

logger = logging.getLogger('hardware-monitor')

def main():
  start_monitoring()


if __name__ == '__main__':
  main()