# coding:utf8

"""
@author: Zhangao Lu
@contact: zlu2@laurentian.ca
@time: 2022/8/7
@description:
"""
import os
import sys
sys.path.append("../")
# print(os.getcwd())


import time
import arrow
import pyminizip
import traceback
from os import walk
from main_utils.mail_tools import SendMail
from config import config


def email_sender():
    """Send captured pics via emails"""
    while 1:
        current_time = arrow.now()
        ten_minutes_ago = current_time.shift(minutes=-10)
        try:
            sm = SendMail(config.SENDER_MAIL_HOST, config.SENDER_MAIL_USER, config.SENDER_MAIL_PASS)

            images = []
            for (dirpath, dirnames, filenames) in walk("../screenshots"):
                for filename in filenames:
                    timestamp = float(filename.replace(".jpg", ""))
                    if current_time >= arrow.get(timestamp) >= ten_minutes_ago:
                        images.append(f"../screenshots/{filename}")
            print(current_time, len(images))
            if len(images) > 0:
                zip_file_path = f"../zip_files/{current_time.format('YYYY-MM-DD HH-mm-ss')}.zip"
                pyminizip.compress_multiple(images, [], zip_file_path, config.ZIP_PASS, 2)

                sm.send_mail_with_zipfile(f"{current_time.format('YYYY-MM-DD HH-mm-ss')} {len(images)} images", content="", to_list=[config.RECEIVER_MAIL_USER], zipfiles=[zip_file_path])
                if os.path.isfile(zip_file_path):
                    os.remove(zip_file_path)
            else:
                # sm.send_mail(f"{current_time.format('YYYY-MM-DD HH-mm-ss')} 0 image", content="no images", to_list=[config.RECEIVER_MAIL_USER])
                pass

            print("Send successfully!")

            for image in images:
                if os.path.isfile(image):
                    os.remove(image)
        except:
            print(traceback.format_exc())
            print(f"{current_time} Failed")
        time.sleep(60 * 10)


if __name__ == '__main__':
    email_sender()
