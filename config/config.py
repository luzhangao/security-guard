# coding:utf8

"""
@author: Zhangao Lu
@contact: zlu2@laurentian.ca
@time: 2022/8/2
@description:
"""

from decouple import config


SENDER_MAIL_HOST = config('SENDER_MAIL_HOST')
SENDER_MAIL_USER = config('SENDER_MAIL_USER')
SENDER_MAIL_PASS = config('SENDER_MAIL_PASS')

RECEIVER_MAIL_USER = config('RECEIVER_MAIL_USER')

ZIP_PASS = config('ZIP_PASS')

