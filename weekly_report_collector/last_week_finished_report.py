# -*- coding:utf-8 -*-
import re
_debug_format =  '[%s]%s (%s/%s) \n'
_week_report_format = "[%s]%s (%s, %s)\n"

'''
store row data of last week finished task data
- 暂不支持单位的转换, 统一使用天数(d)为单位
'''
class LastWeekFinishedTaskRow:
    def __init__(self):
        self._module_str = ''
        self._task_str = ''
        self._duration = 0
        self._duration_str = ''
        self._owner=''


    def safe_check_time(self, time):
        '''
        保障时间字符串包含单位符号天数(d)
        '''
        time_lower = str(time).lower()
        if (time_lower.count('h') == 0 and
                    time_lower.count('d') == 0):
            return time_lower + 'd'
        return time

    def _convert_time(self, time):
        '''
        将时间转换成int
        '''
        time_str=str(time).lower()
        replace_str='[dh]'
        time_str = re.sub(replace_str, '', time_str)
        return int(time_str)
        
    def ReadData(self, row):
        self._module_str = row[0]
        if row[1] != '':
            self._task_str = row[1].replace('\n', ',')
        self._duration_str = self.safe_check_time(row[2])
        self._duration = self._convert_time(row[2])

    def __str__(self):
        return  _debug_format % (self._module_str, 
                                self._task_str,
                                self._duration_str,
                                self._duration)

    def __repr__(self):
        return _debug_format % (self._module_str,
                                self._task_str,
                                self._duration_str,
                                self._duration)


'''
export last week finished task data row
'''
class ExportLastWeekFinishedTaskRow:
    def __init__(self):
        self._owner = ''

    def ExportRow(self, row):
        return _week_report_format % (row._module_str, row._task_str, row._owner, row._duration)
