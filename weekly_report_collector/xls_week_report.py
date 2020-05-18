# -*- coding:utf-8 -*-
'''
store info about the start and end row index of each form
'''
class XlsFormInfo:
    _format_str = 'key:{self._key}, row_start:{self._row_start}, row_end:{self._row_end}'
    def __init__(self):
        self._key = ''
        self._row_start = 0
        self._row_end = 0
    def __str__(self):
        return XlsFormInfo._format_str.format(self=self)
    def __repr__(self):
        return XlsFormInfo._format_str.format(self=self)

'''
store info of report rows
'''
class WeekReport:
    def __init__(self):
        self._rows = list()

    def ReadData(self, owner, row_data, row_type):
        for row in row_data:
            report_row = row_type()
            report_row._owner = owner
            report_row.ReadData(row)
            self._rows.append(report_row)

    def Export(self, exporter):
        result = list()
        for row in self._rows:
            result.append(exporter.ExportRow(row))
        return result

    def __str__(self):
        strs = ''
        for row in self._rows:
            strs += row.__str__()
        return strs

    def __repr__(self):
        strs = list()
        for row in self._rows:
            strs += row.__str__()
        return strs

