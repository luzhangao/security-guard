# coding:utf8

"""
@author: Zhangao Lu
@contact: zlu2@laurentian.ca
@time: 2022/8/1
@description:
"""

from yolov5.detect import run


def foo():
    run(weights="yolov5s.pt", source=0, notification=True)


if __name__ == '__main__':
    foo()
