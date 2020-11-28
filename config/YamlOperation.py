# -*- coding = UTF-8 -*-
# Autohr   : yang
# File     : YamlOperation.py
# project  : Python_project
# time     : 2020/11/16 16:55
# Describe : yaml文件的操作
# ---------------------------------------

import yaml
from config.UtilsOperation import getPorjectPath


class YamlOperation:

    def __init__(self, yaml_path):
        self.yaml_path = getPorjectPath() + yaml_path

    def read_yaml(self):
        """读取yaml文件"""
        with open(self.yaml_path, 'r', encoding='UTF-8')as fp:
            yaml_data = yaml.safe_load(fp)
        return yaml_data
