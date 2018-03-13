from report_loader_xlsx import *
from xls_collector import *
from xls_week_report import *
from week_task_report import *
from last_week_finished_report import *
from last_week_unfinished_report import *


#filePath = 'D:\\Project\\Git\\python_learning_scripts\\weekly_report_collector\\unit_test\\周报_20180129_danny.xlsx'
filePath = 'D:\\Project\\Git\\python_learning_scripts\\weekly_report_collector\\unit_test\\周报_20180129_rust.xlsx'
keys = ['本周计划任务','上周完成任务','上周未完成任务']
xlsx_data = list()

def unit_test_read_form():
    xlsx_data = ReadXlsx(filePath)
    dict = AnalyzeXlsx(xlsx_data, keys)
    print(dict)
    for key in keys:
        print(ReadForm(xlsx_data, dict[key]))

def unit_test_all_report():
    dict = AnalyzeXlsx(xlsx_data, keys)
    objs = [WeekTaskRow(), LastWeekFinishedTaskRow(), LastWeekUnFinishedTaskRow()]
    for key, obj in zip(keys, objs):
        week_report_data = ReadForm(xlsx_data, dict[key])
        week_report = WeekReport()
        week_report.ReadData(week_report_data, obj.__class__)
        print(week_report)


#_folder = 'D:\\Project\\Git\\python_learning_scripts\\weekly_report_collector\\unit_test'
_folder = 'd:\\Project\\summer_plan\\week_report'
_exporter = [ExportWeekTaskRow(), ExportLastWeekFinishedTaskRow(), ExportLastWeekUnFinishedTaskRow()]
_rows = [WeekTaskRow(), LastWeekFinishedTaskRow(), LastWeekUnFinishedTaskRow()]

def unit_test_SearchFiles_and_GetInfo():
    allFiles = SearchFiles(_folder)
    print(allFiles)

    for filePath in allFiles:
        info = GetInfoFromFileName(filePath)
        print(info)

def unit_test_export_report():

    report = [list(), list(), list()]

    allFiles = SearchFiles(_folder)
    time = ''

    for file in allFiles:
        info = GetInfoFromFileName(file)
        time = info[0]

        print('Reading '+ info[1] + ' report' )
        xlsx_data = ReadXlsx(file)
        dict = AnalyzeXlsx(xlsx_data, keys)
        for i in range(0, len(_exporter)):
            week_report_data = ReadForm(xlsx_data, dict[keys[i]])
            week_report = WeekReport()
            week_report.ReadData(week_report_data, _rows[i].__class__)
            _exporter[i]._owner = info[1]
            report[i].append(week_report.Export(_exporter[i]))

    fw = open('D:\\report.txt', 'w')
    for i in range(0, len(_exporter)):
        fw.write(keys[i] + '\n')
        for strs in report[i]:
            for str in strs:
                fw.write(str)
        fw.write('\n\n\n')


unit_test_export_report()