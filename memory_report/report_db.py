# -*- coding:utf-8 -*-
from report_enum import *


class ReportDbRow:
    def __init__(self):
        self._res_type = ResType.none
        self._m_type = ModuleType.none
        self._size = 0
        self._name = ""

    def __str__(self):
        return "name:%s, rtype:%s, m_type:%s, size:%f" % (self._name, self._res_type, self._m_type, self._size)


class ReportDb:
    def __init__(self):
        self._db = list()

    def AddRow(self, row):
        self._add_to_db(row)

    def Add(self, res_type, m_type, size, name):
        row = ReportDbRow()
        row._res_type = res_type
        row._m_type = m_type
        row._size = size
        row._name = name
        self._add_to_db(row)

    def _add_to_db(self, row):
        self._db.append(row)

    def __str__(self):
        ret_str = ''
        for row in self._db:
            ret_str += row.__str__()
            ret_str += '\n'
        return ret_str
