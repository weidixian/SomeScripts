#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-11-27 下午12:06
# @Author  : weidixian@126.com
# @Site    :
# @File    : main.py
# @Software: PyCharm
from datetime import datetime

import HTML

import SMTPMail.Interface as smtpMailInterface
import Task.Interface


def filter_tasks(filename, filter_defintion):
    """
        filter tasks by the follow defintion
        1 = task_in_3_days      三天内到期的任务
        2 = task_is_today       今天需要检验的任务
        3 = task_over_day       过了检验期还没有检验的任务
    """
    task_interface = Task.Interface.Interface()
    task_list = task_interface.get_all_task_in_list(filename)
    rs_list = []

    cdate = datetime.now().strftime('%Y/%m/%d')
    cdate = datetime.strptime(cdate, '%Y/%m/%d')  # 今天当前日期
    for i in range(len(task_list)):
        # print task_list[i]
        if i == 0:
            rs_list.append(task_list[i])
        # get not null row and task is not completed
        elif task_list[i][2] != '' and task_list[i][10] == '':
            # 过了检验期
            end_date = datetime.strptime(task_list[i][7], '%Y/%m/%d')  # 任务结束日期
            delta = end_date - cdate
            if filter_defintion == 1:
                if 3 > delta.days >= 0:
                    rs_list.append(task_list[i])
            elif filter_defintion == 2:
                if delta.days == -1:
                    rs_list.append(task_list[i])
            elif filter_defintion == 3:
                if delta.days < -1:
                    rs_list.append(task_list[i])
            else:
                print 'Error! filter_defintion is not found.'
    if len(rs_list) == 1:
        return ''
    else:
        return HTML.table(rs_list)


def main():
    t3d = filter_tasks('任务评分登记表.xlsx', 1)
    tt = filter_tasks('任务评分登记表.xlsx', 2)
    tod = filter_tasks('任务评分登记表.xlsx', 3)

    mail_msg = ''

    if t3d != '':
        mail_msg = '<H2>三天内到期的任务</H2>' + t3d + '</BR></BR>'

    if tt != '':
        mail_msg = mail_msg + '<H2>今天需要检验的任务</H2>' + tt + '</BR></BR>'

    if tod != '':
        mail_msg = mail_msg + '<H2>过了检验期还没有检验的任务</H2>' + tod

    if mail_msg != '':
        # 取当期时间
        now = datetime.now()
        currentime = now.strftime('%Y-%m-%d %H:%M:%S')
        # currentime = now.strftime('%Y-%m-%d')
        subject = u'【任务通知】任务评分登记表' + currentime
        # smtpMailInterface.send_html_mail(mail_msg, ['weidixian@126.com'],
        #                                  '任务通知',
        #                                  '业务运维组', subject)
        print mail_msg
    else:
        print 'mail msg is null. no email to send!'


if __name__ == '__main__':
    main()
