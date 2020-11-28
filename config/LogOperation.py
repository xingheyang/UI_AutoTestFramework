# -*- coding = UTF-8 -*-
# Autohr   : yang
# File     : LogOperation.py
# project  : Python_project
# time     : 2020/11/16 16:57
# Describe : 日志的操作
# ---------------------------------------
import logging
import os
import sys

from config.UtilsOperation import getPorjectPath


class GetLogger:

    def __init__(self, log_path):
        """
        :param log_path: 日志文件的路径
        """
        self.file_name = getPorjectPath() + log_path
        self.logger = logging.getLogger()
        # 设置日志等级
        self.logger.setLevel(logging.INFO)
        # 设置日志的输出格式
        self.formatter = logging.Formatter('%(levelname)s - %(asctime)s - %(message)s')

    def _console(self, level, message):
        # 创建FileHandler对象，将日志写入到文件,a指追加日志到文件末尾
        fh = logging.FileHandler(self.file_name, mode='a', encoding='utf8')
        # 设置文件日志的等级
        fh.setLevel(logging.INFO)
        # 设置日志的格式与内容
        fh.setFormatter(self.formatter)
        # 添加内容到日志文件
        self.logger.addHandler(fh)
        # 创建StreamHandler对象，用于输出日志到控制台
        sh = logging.StreamHandler(sys.stdout)
        # 设置控制台输出的日志等级
        sh.setLevel(logging.INFO)
        # 设置控制台输出日志的内容格式
        sh.setFormatter(self.formatter)
        # 添加内容到控制台
        self.logger.addHandler(sh)
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        # 避免日志重复
        self.logger.removeHandler(fh)
        self.logger.removeHandler(sh)
        # 关闭日志文件
        fh.close()

    def info(self, message):
        message = "-" * 20 + " " + message + " " + "-" * 20
        self._console('info', message)

    def debug(self, message):
        message = "-" * 20 + " " + message + " " + "-" * 20
        self._console('debug', message)

    def warning(self, message):
        message = "-" * 20 + " " + message + " " + "-" * 20
        self._console('warning', message)

    def error(self, message):
        message = "-" * 20 + " " + message + " " + "-" * 20
        self._console('error', message)