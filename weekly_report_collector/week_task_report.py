# -*- coding:utf-8 -*-

from project_calendar import *
from datetime import datetime

_debug_format = '%s-%s [%s]%s %s\n'
_week_report_format =  '%s-%s [%s]%s (%s, %s)\n'


'''
store row data of week task report
'''
class WeekTaskRow:
    def __init__(self):
        self._module_str = ''
        self._task_str = ''
        self._estimate_day = ''
        self._start_day = ''
        self._end_day = ''
        self._owner =''

    def safe_check_week(self, week):
        if 0 == week.lower().count('w'):
            return 'W' + week
        return week

    def safe_check_time(self, time):
        time_lower = str(time).lower()
        if (time_lower.count('h') == 0 and
            time_lower.count('d') == 0):
            return time_lower + 'd'
        return time

    def ReadData(self, row):
        self._module_str = row[0]
        if row[1] != '':
            self._task_str = row[1].replace('\n', ',')
        self._estimate_day = self.safe_check_time(row[2])
        self._start_day = self.safe_check_week(str(row[3]))
        self._end_day = self.safe_check_week(str(row[4]))

    def __str__(self):
        return  _debug_format % (
        self._start_day, self._end_day, self._module_str, self._task_str, self._estimate_day)

    def __repr__(self):
        return _debug_format % (
        self._start_day, self._end_day, self._module_str, self._task_str, self._estimate_day)

'''
export current week plan row data
'''
class ExportWeekTaskRow:
    def __init__(self):
        self._owner = ''

    def ExportRow(self, row):
        return _week_report_format % (
        row._start_day, row._end_day, row._module_str, row._task_str, row._owner, row._estimate_day)


