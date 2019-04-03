"""
日志模块
"""
import logging
logging.Formatter

logging.basicConfig(level=logging.DEBUG, filename='demo10.log', format='%(lineno)d-%(levelname)s-%(asctime)s')
logging.error("errorinfo:32323")
logging.info("info:223")
logging.warning("warn:212")







