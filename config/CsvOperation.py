# -*- coding = UTF-8 -*-
# Autohr   : yang
# File     : YamlOperation.py
# project  : Python_project
# time     : 2020/11/16 16:55
# Describe : yaml文件的操作
# ---------------------------------------
import csv
from config.UtilsOperation import getPorjectPath


class Csv_File_Operation:

    def __init__(self, csv_path):
        self.csv_path = getPorjectPath() + csv_path

    def read_csv(self):
        """读取CSV文件"""
        with open(self.csv_path, 'r', encoding='utf8')as fp:
            data_list = [i for i in csv.reader(fp)]
        return data_list
