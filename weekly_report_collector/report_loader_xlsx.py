# -*- coding:utf-8 -*-

"""
function to load different weekly report
in .xlsx files
"""
import xlrd
from xls_week_report import XlsFormInfo


def ReadXlsx(file_path):
    '''
    give path return the data of xlsx
    :param file_path: absolute path of the xlsx
    :return: the workbook of slrd
    '''
    try:
        data = xlrd.open_workbook(file_path)
        return data
    except Exception as e:
        print(str(e))
    return

def AnalyzeXlsx(xls_data, key_list):
    '''
      give xls workbook data, generate a dict that key is
    the forms key, value is the row number.
    :param xls_data: input xls data
    :key_list: 3 forms' key to search in the xlsx 
    :return: dict
    '''
    # all the data must be in the first sheet
    table = xls_data.sheets()[0]
    nrows = table.nrows

    # generate a dict that key is the forms key, value is the row number
    row_num_keys = {}
    last_key = key_list[0]
    row_num_keys[last_key] = XlsFormInfo()

    for row_num in range(0, nrows):
        row = table.row_values(row_num)

        #skip empty line
        if len(row) == 0:
            continue

        #according to the key to search all the forms
        for key in key_list:
            if row[0].count(key) > 0:
                row_num_keys[last_key]._row_end = row_num
                last_key = key

                info = XlsFormInfo()
                info._key = key
                info._row_start = row_num + 2 # skip the title & key line
                info._row_end = nrows - 1
                row_num_keys[key] = info

    return row_num_keys

def ReadForm(xls_data, xls_info):
    '''
    given form key, row start idx and row end idx, export form row data
    :param xls_data: xlsx data
    :param row_start: form start row, not include the form key row
    :param row_end: form end row
    :return: form data like xlsx data, list of line, each line split into string list
    '''
    table = xls_data.sheets()[0]
    nrows = table.nrows

    # generate a dict that key is the forms key, value is the row number
    form = list()

    if xls_info._row_start > xls_info._row_end : 
        return form

    # 添加第一行, 用于表格只有1行时, 改行也有可能为空
    row_num = xls_info._row_start
    row = table.row_values(row_num)
    if _is_empty_line(row):
        return form

    form.append(table.row_values(row_num))
    row_num += 1

    while row_num < xls_info._row_end : 
        row = table.row_values(row_num)
        # skip empty line
        if (_is_empty_line(row)):
            row_num += 1 
            continue

        form.append(table.row_values(row_num))
        row_num +=1

    return form

def _is_empty_line(row):
    '''
    输入table的row数据, 判断是否为空
    '''
    if ('' == row[0] and '' == row[1] and
        '' == row[2] and '' == row[3] and
        '' == row[4]):
        return True
    return False
