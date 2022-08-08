# coding:utf8

"""
@author: Zhangao Lu
@contact: zlu2@laurentian.ca
@time: 2022/8/1
@description:
"""

import os
import sys
sys.path.append("../")
# print(os.getcwd())

from yolov5.detect import run


def start_detector():
    run(weights="yolov5s.pt", source=0, notification=True)


if __name__ == '__main__':
    start_detector()
