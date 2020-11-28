# -*- coding = UTF-8 -*-
# Autohr   : yang
# File     : YamlOperation.py
# project  : Python_project
# time     : 2020/11/16 16:55
# Describe : yaml文件的操作
# ---------------------------------------
import configparser
import os
import sys

from config.UtilsOperation import getPorjectPath


class Ini_File_Operation:

    @staticmethod
    def read_Ini():
        """读取INI文件"""
        Ini_Path = getPorjectPath() + r"\resources\conf\config.ini"
        config = configparser.ConfigParser()
        config.read(Ini_Path)
        return config
