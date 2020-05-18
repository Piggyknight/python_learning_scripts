# -*- coding:utf-8 -*-
from project_calendar import *
from report_24_category import *
from xls_week_report import *

_24_report_format = '**** [%s-%s]%s\n    :PROPERTIES:\n    :OWNER: %s\n    :WEEKTIME: %s-%s\n    :TIME: <%s>--<%s>\n    :END:\n'

class ExportWeekTaskRow24:
    def __init__(self):
        self._calendar = ProjectCalendar()
        self._category = Report24Category()
        self._report_data = {}

    def ExportReport(self, report_list, exportFilePath):
        # init data
        self.init_report_data()

        for report in report_list:
            #collect all the row string of report
            report.Export(self)

        #write into file
        fw = open(exportFilePath, 'w')
        for (key, val) in self._report_data.items():
            fw.write(key)
            fw.write('\n')
            for str in val:
                fw.write(str)
            fw.write('\n\n\n')

        print('Finished export ' + exportFilePath)

    def init_report_data(self):
        self._report_data = {}
        for (key, val) in self._category._map.items():
            self._report_data[key] = []


    def ExportRow(self, row):
        #transfer basic data
        start_week_time = self._calendar.GetIsoTime(row._start_day)
        end_week_time = self._calendar.GetIsoTime(row._end_day)

        #put row data into its category sting list
        category_key = self._category.GetCategory(row._module_str)
        if not category_key in self._report_data.keys():
            print('[Error]Dont have category key: '+
                  category_key +'for row ' + row.__str__() + '! Please update category cnf!')
            return 'error'

        row_str = _24_report_format % (category_key,
                                       row._module_str,
                                       row._task_str,
                                       row._owner,
                                       row._start_day,
                                       row._end_day,
                                       start_week_time,
                                       end_week_time)
        self._report_data[category_key].append(row_str)

        return 'success'