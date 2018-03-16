# -*- coding:utf-8 -*-
_debug_format =  '[%s]%s (%s)\n'
_week_report_format = "[%s]%s (%s, %s)\n"

'''
store row data of last week finished task data
'''
class LastWeekFinishedTaskRow:
    def __init__(self):
        self._module_str = ''
        self._task_str = ''
        self._duration = ''
        self._owner=''

    def safe_check_time(selfs, time):
        time_lower = str(time).lower()
        if (time_lower.count('h') == 0 and
                    time_lower.count('d') == 0):
            return time_lower + 'd'
        return time

    def ReadData(self, row):
        self._module_str = row[0]
        if row[1] != '':
            self._task_str = row[1].replace('\n', ',')
        self._duration = self.safe_check_time(row[2])

    def __str__(self):
        return  _debug_format % (self._module_str, self._task_str, self._duration)

    def __repr__(self):
        return _debug_format % (self._module_str, self._task_str, self._duration)


'''
export last week finished task data row
'''
class ExportLastWeekFinishedTaskRow:
    def __init__(self):
        self._owner = ''

        def ExportRow(self, row):
            return _week_report_format % (row._module_str, row._task_str, self._owner, row._duration)
