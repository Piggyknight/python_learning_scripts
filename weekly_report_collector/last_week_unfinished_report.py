# -*- coding:utf-8 -*-
_debug_format =  '[%s]%s: (%s)\n'
_week_report_format = "[%s]%s: %s;    (%s)\n"

'''
store row data of last week unfinished task data
'''
class LastWeekUnFinishedTaskRow:
    def __init__(self):
        self._module_str = ''
        self._task_str = ''
        self._reason = ''
        self._owner=''
    def ReadData(self, row):
        self._module_str = row[0]

        if row[1] != '':
            self._task_str = row[1].replace('\n',',')
        self._reason = row[2]

    def __str__(self):
        return _debug_format % (self._module_str, self._task_str, self._reason)

    def __repr__(self):
        return _debug_format % (self._module_str, self._task_str, self._reason)

'''
export last week finished task data row
'''
class ExportLastWeekUnFinishedTaskRow:
    def __init__(self):
        self._owner = ''

    def ExportRow(self, row):
        return _week_report_format % (row._module_str, row._task_str, row._reason, self._owner)
