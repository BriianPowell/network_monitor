# monitoring.py
import psutil
import logging
import logger

logger = logging.getLogger('hardware-monitor')

def start_monitoring():
  logger.info('\nBeginner Monitoring')
  for x in range(3):
    cpuArray = psutil.cpu_percent(interval=1,percpu=True)
    logger.info(cpuArray)


#psutil for network traffic monitoring
