"""
python内置模块--日志文件
"""

# 1.logging模块的使用（只将error日志信息输出到文件，info以上信息输出到控制台）

# 1.导入模块
import logging

# 2.创建日志模块
loginLogger = logging.getLogger('main')
# 设置等级
loginLogger.setLevel(logging.INFO)
# 3.创建日志输出类型
fileHandler = logging.FileHandler('loginLogger.txt', encoding='utf-8')
# 4.指定日志格式
fileHandler.setFormatter(logging.Formatter('%(name)s-%(levelno)s-%(lineno)d- %(asctime)s-%(message)s'))

# 输出到控制台
streamHanlder = logging.StreamHandler()
streamHanlder.setLevel(logging.INFO)
streamHanlder.setFormatter(logging.Formatter('%(name)s-%(levelno)s-%(lineno)d- %(asctime)s-%(message)s'))

# 5.将日志处理方法添加到日志工具
loginLogger.addHandler(fileHandler)
loginLogger.addHandler(streamHanlder)


loginLogger.debug('debug')
loginLogger.info('info')
loginLogger.warning('warning')
loginLogger.error('error创建')




