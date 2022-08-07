# coding:utf8

"""
@author: Zhangao Lu
@contact: zlu2@laurentian.ca
@time: 2022/8/2
@description:
"""


import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

from main_utils.io_tools import open_file


class SendMail(object):
    def __init__(self, mail_host, mail_user, mail_pass):
        self.mail_host = mail_host
        self.mail_user = mail_user
        self.mail_pass = mail_pass

        self.server = smtplib.SMTP_SSL(self.mail_host, 465)
        self.server.login(self.mail_user, self.mail_pass)

    def send_mail(self, sub, content, to_list):
        _sub = sub
        me = "guard" + "<" + self.mail_user + ">"
        msg = MIMEText(content, _subtype='plain', _charset='utf-8')
        msg['Subject'] = _sub
        msg['From'] = me
        msg['To'] = ";".join(to_list)
        self.server.sendmail(me, to_list, msg.as_string())

    def send_mail_with_image(self, sub, content, to_list, images):
        _sub = sub
        me = "guard" + "<" + self.mail_user + ">"
        msg = MIMEMultipart("related")
        msg['Subject'] = _sub
        msg['From'] = me
        msg['To'] = ";".join(to_list)
        for image_file in images:
            img = MIMEImage(open_file(image_file))
            img.add_header('content-disposition', 'attachment', filename=image_file)
            msg.attach(img)
        self.server.sendmail(me, to_list, msg.as_string())

    def send_mail_with_zipfile(self, sub, content, to_list, zipfiles):
        _sub = sub
        me = "guard" + "<" + self.mail_user + ">"
        msg = MIMEMultipart("related")
        msg['Subject'] = _sub
        msg['From'] = me
        msg['To'] = ";".join(to_list)
        for zipfile in zipfiles:
            zmsg = MIMEBase('application', 'zip')
            zmsg.set_payload(open_file(zipfile))
            encoders.encode_base64(zmsg)
            zmsg.add_header('Content-Disposition', 'attachment', filename="path.zip")
            msg.attach(zmsg)
        self.server.sendmail(me, to_list, msg.as_string())

    def __exit__(self):
        # self.server.close()
        self.server.quit()


if __name__ == '__main__':
    from config import config
    sm = SendMail(config.SENDER_MAIL_HOST, config.SENDER_MAIL_USER, config.SENDER_MAIL_PASS)
    # sm.send_mail("1", "233", [config.RECEIVER_MAIL_USER])

    from os import walk
    # f = []
    # for (dirpath, dirnames, filenames) in walk("../screenshots"):
    #     f.extend([f"../screenshots/{filename}" for filename in filenames])
    # print(f)
    # sm.send_mail_with_image("1", content=123, to_list=[config.RECEIVER_MAIL_USER], images=f)

    import pyminizip
    f = []
    for (dirpath, dirnames, filenames) in walk("../screenshots"):
        f.extend([f"../screenshots/{filename}" for filename in filenames])
        # f.extend(filenames)
    print(f)
    pyminizip.compress_multiple(f, [], "../screenshots/path.zip", "1234", 1)
    sm.send_mail_with_zipfile("1", content=123, to_list=[config.RECEIVER_MAIL_USER], zipfiles=["../screenshots/path.zip"])




