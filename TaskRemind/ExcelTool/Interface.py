#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-11-27 下午1:17
# @Author  : weidixian@126.com
# @Site    : 
# @File    : Interface.py
# @Software: PyCharm

import xlrd
from xlrd import xldate_as_tuple
import sys
from datetime import datetime

# 设定默认的编码为 utf8
reload(sys)
sys.setdefaultencoding('utf8')


class Interface:
    """ Interface Object """

    def __init__(self):
        pass

    def read_excel_to_dict(self, filename, colname_index, sheet_index):
        rbook = object
        try:
            rbook = xlrd.open_workbook(filename)
        except Exception, e:
            print str(e)
        sheet = rbook.sheets()[sheet_index]
        nrows = sheet.nrows
        # ncols = sheet.ncols
        colnames = sheet.row_values(colname_index)
        json_data = []
        for rownum in range(0, nrows):
            row = sheet.row_values(rownum)
            if row:
                cells = {}
                for colnum in range(len(colnames)):
                    ctype = sheet.cell(rownum, colnum).ctype  # 表格的数据类型
                    # cell = sheet.cell_value(rownum, colnum)
                    cell = row[colnum]
                    if ctype == 2 and cell % 1 == 0:  # 如果是整形
                        cell = int(cell)
                    elif ctype == 3:
                        # 转成datetime对象
                        date = datetime(*xldate_as_tuple(cell, 0))
                        # cell = date.strftime('%Y/%m/%d %H:%M:%S')
                        cell = date.strftime('%Y/%m/%d')
                    elif ctype == 4:
                        cell = True if cell == 1 else False
                    # set key:value
                    cells[colnames[colnum]] = cell
                json_data.append(cells)
        return json_data

        # interface = Interface()
        # json_data = interface.read_excel_to_dict('任务评分登记表.xlsx', 0, 0)
        # print json_data[1][u'编号']
