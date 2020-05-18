# -*- coding:utf-8 -*-
import time
from datetime import datetime, timedelta
import configparser

def StringToDate(format, string):
    return datetime.strptime(string, format)

# store data
class ReportDataInfo:
    def __init__(self):
        self._year = 0
        self._month = 1
        self._day = 0

    def __str__(self):
        return '<%s-%s-%s>' % (self._year, self._month, self._day)

class WeekDay:
    _min_week = 1
    _start = datetime(1,1,1)
    def __init__(self):
        self._week = 0
        self._weekday = 1

    def Set(self, week, weekday):
        self._week = week
        self._weekday = weekday

    def __str__(self):
        return "W%d.%d" % (self._week, self._weekday)

    def __repr__(self):
        return "W%d.%d" % (self._week, self._weekday)

'''
calculate week day and its iso time
'''
class ProjectCalendar:
    _format = '%Y-%m-%d'
    def __init__(self):
        self._w1_date = datetime(1,1,1)
        self._current_date = datetime(1,1,1)
        self._w1_weekday = WeekDay()

    def LoadIni(self, filePath):
        cf = configparser.ConfigParser()
        cf.read(filePath)

        sect_key = 'Days'
        item_key = 'startDay'
        self._w1_date = StringToDate('%Y%m%d',cf[sect_key][item_key])

    def get_weekday(self, day_string):
        wd = WeekDay()
        day_string = day_string.lower().replace('w', '')
        info = day_string.split('.')
        wd._weekday = int(info[1]) - 1
        wd._week = int(info[0])
        return wd

    '''
    given week day string, return iso Year-Month-Data string
    weekday string's format: W3.1, w1.1
    '''
    def GetIsoTime(self, weekday_str):
        wd = self.get_weekday(weekday_str)
        delta_week = wd._week - 1
        delta_day = wd._weekday
        result = self._w1_date + timedelta(days=delta_day, weeks=delta_week)
        return result.strftime(ProjectCalendar._format)


