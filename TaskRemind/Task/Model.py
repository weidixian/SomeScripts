#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-11-27 下午12:06
# @Author  : weidixian@126.com
# @Site    :
# @File    : Model.py
# @Software: PyCharm


class Task:
    """ Task model object """

    def __init__(self, code, group_type, task_type, title, content, key_score, start_time, end_time, charger, manager,
                 check_time, check_result, score):
        self.code = code
        self.group_type = group_type
        self.task_type = task_type
        self.title = title
        self.content = content
        self.key_score = key_score
        self.start_time = start_time
        self.endTime = end_time
        self.charger = charger
        self.manager = manager
        self.check_time = check_time
        self.check_result = check_result
        self.score = score

    def get_item_list(self):
        items = [self.code, self.group_type, self.task_type, self.title, self.content, self.key_score, self.start_time,
                 self.endTime, self.charger, self.manager, self.check_time, self.check_result, self.score]
        return items
