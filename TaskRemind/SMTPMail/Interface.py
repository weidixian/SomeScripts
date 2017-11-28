#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-11-27 下午5:27
# @Author  : weidixian
# @Site    : 
# @File    : Interface.py
# @Software: PyCharm

import smtplib
from email.mime.text import MIMEText
from email.header import Header


class Interface:
    def __init__(self):
        pass


def send_html_mail(mail_msg, receivers, from_header, to_header, subject):
    # 第三方 SMTP 服务
    mail_host = 'smtp.126.com'  # 设置服务器
    mail_user = 'weidixian@126.com'  # 用户名
    mail_pass = 'xxxxxxxx'  # 口令

    sender = 'weidixian@126.com'
    # receivers = ['weidixian@126.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText(mail_msg, 'html', 'utf-8')
    message['From'] = Header(from_header, 'utf-8')
    message['To'] = Header(to_header, 'utf-8')

    # 取当期时间
    # now = datetime.now()
    # currentime = now.strftime('%Y-%m-%d %H:%M:%S')
    # currentime = now.strftime('%Y-%m-%d')

    # subject = currentime + u' 【任务通知】任务评分登记表'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtp_obj = smtplib.SMTP()
        smtp_obj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtp_obj.login(mail_user, mail_pass)
        smtp_obj.sendmail(sender, receivers, message.as_string())
        print '邮件发送成功'
    except smtplib.SMTPException, e:
        print 'Error: 无法发送邮件'
        print str(e)
