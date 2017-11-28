#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-11-27 下午12:06
# @Author  : weidixian@126.com
# @Site    :
# @File    : Interface.py
# @Software: PyCharm
import HTML

import ExcelTool.Interface
import Task.Model


class Interface:
    """ Task interface """

    def __init__(self):
        pass

    def get_all_task_in_json(self, filename):
        excel_tool = ExcelTool.Interface.Interface()
        json_data = excel_tool.read_excel_to_dict(filename, 0, 0)
        # print list_data[1][u'编号']
        return json_data

    def get_all_task_in_list(self, filename):
        excel_tool = ExcelTool.Interface.Interface()
        json_data = excel_tool.read_excel_to_dict(filename, 0, 0)
        # print list_data[1][u'编号']
        task_list = []
        for i in range(len(json_data)):
            task_model = Task.Model.Task(json_data[i][u'编号'], json_data[i][u'分类'], json_data[i][u'任务类型'],
                                         json_data[i][u'标题'],
                                         json_data[i][u'任务内容'], json_data[i][u'关键度'], json_data[i][u'开始时间'],
                                         json_data[i][u'结束时间'],
                                         json_data[i][u'负责人'], json_data[i][u'验收人'], json_data[i][u'验收时间'],
                                         json_data[i][u'验收结果'],
                                         json_data[i][u'得分'])
            task_list.append(task_model.get_item_list())
        return task_list

    def get_all_task_in_html(self, filename):
        html_data = self.get_all_task_in_list(filename)
        # print HTML.table(html_data)
        return HTML.table(html_data)
