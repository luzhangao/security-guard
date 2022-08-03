# coding:utf8

"""
@author: Zhangao Lu
@contact: zlu2@laurentian.ca
@time: 2022/8/2
@description:
"""


import smtplib
from email.mime.text import MIMEText


class SendMail(object):
    def __init__(self, mail_host, mail_user, mail_pass):
        self.mail_host = mail_host
        self.mail_user = mail_user
        self.mail_pass = mail_pass

        self.server = smtplib.SMTP_SSL(self.mail_host, 465)
        self.server.login(self.mail_user, self.mail_pass)

    def send_mail(self, sub, content, to_list):
        _sub = sub
        me = "monitor" + "<" + self.mail_user + ">"
        msg = MIMEText(content, _subtype='plain', _charset='utf-8')
        msg['Subject'] = _sub
        msg['From'] = me
        msg['To'] = ";".join(to_list)
        self.server.sendmail(me, to_list, msg.as_string())

    def __exit__(self):
        # self.server.close()
        self.server.quit()


if __name__ == '__main__':
    from config import config
    sm = SendMail(config.SENDER_MAIL_HOST, config.SENDER_MAIL_USER, config.SENDER_MAIL_PASS)
    sm.send_mail("1", "233", [config.RECEIVER_MAIL_USER])
