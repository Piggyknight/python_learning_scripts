# -*- coding:utf-8 -*-

from report_loader_xlsx import *
from xls_collector import *
from xls_week_report import *
from week_task_report import WeekTaskRow, ExportWeekTaskRow
from last_week_finished_report import LastWeekFinishedTaskRow, ExportLastWeekFinishedTaskRow
from last_week_unfinished_report import LastWeekUnFinishedTaskRow, ExportLastWeekUnFinishedTaskRow
from report_24_category import *
from report_24_exporter import *
from project_calendar import *

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
    objs = [
            WeekTaskRow(),
            LastWeekFinishedTaskRow(),
            LastWeekUnFinishedTaskRow()
            ]
    for key, obj in zip(keys, objs):
        week_report_data = ReadForm(xlsx_data, dict[key])
        week_report = WeekReport()
        week_report.ReadData("", week_report_data, obj.__class__)
        print(week_report)


#_folder = 'D:\\Project\\Git\\python_learning_scripts\\weekly_report_collector\\unit_test'
_folder = 'd:\\summer_plan\\week_report\\20180925\\'

_exporter = [
            ExportWeekTaskRow(),
            ExportLastWeekFinishedTaskRow(),
            ExportLastWeekUnFinishedTaskRow()
            ]
            
_rows = [
        WeekTaskRow(), 
        LastWeekFinishedTaskRow(),
        LastWeekUnFinishedTaskRow()
        ]

def unit_test_SearchFiles_and_GetInfo():
    allFiles = SearchFiles(_folder)
    print(allFiles)

    for filePath in allFiles:
        info = GetInfoFromFileName(filePath)
        print(info)

def unit_test_export_report():
    report = [list(), list(), list()]

    # 在目录中找到所有文件
    allFiles = SearchFiles(_folder)
    time = ''

    
    for file in allFiles:
        # 从文件名解析相应信息, 范例: 周报_20180705_henry
        #   - info[0] : 时间
        #   - info[1] : name
        info = GetInfoFromFileName(file)
        time = info[0]

        # 获取xlsx的数据, 转换成单独的表存于dict中
        print('Reading '+ info[1] + ' report' )
        xlsx_data = ReadXlsx(file)
        dict = AnalyzeXlsx(xlsx_data, keys)

        # 讲数据全部存于相对应的exporter中
        for i in range(0, len(_exporter)):
            week_report_data = ReadForm(xlsx_data, dict[keys[i]])
            week_report = WeekReport()
            week_report.ReadData(info[1],week_report_data, _rows[i].__class__)
            report[i].append(week_report.Export(_exporter[i]))

    # 遍历所有exporter并导出
    fw = open('D:\\report.txt', 'w',encoding='utf-8')
    for i in range(0, len(_exporter)):
        title_str = '##%s\n' % keys[i]
        fw.write( title_str )
        for strs in report[i]:
            for str in strs:
                fw.write(str)
        fw.write('\n\n\n')

    return


_calendar_ini_file = 'D:\\Project\\Git\\python_learning_scripts\\weekly_report_collector\\calendar_cnf.ini'
_category_ini_file = 'D:\\Project\\Git\\python_learning_scripts\\weekly_report_collector\\category_mapping_cnf.ini'
def unit_test_export_24_report():
    report = [list(), list(), list()]
    allFiles = SearchFiles(_folder)
    time = ''

    #prepare exporter
    calendar = ProjectCalendar()
    calendar.LoadIni(_calendar_ini_file)

    category = Report24Category()
    category.LoadIni(_category_ini_file)
    exporter = ExportWeekTaskRow24()
    exporter._calendar = calendar
    exporter._category = category

    report_list=[]
    filters = ['story', 'weber']
    for file in allFiles:
        info = GetInfoFromFileName(file)
        time = info[0]
        date = StringToDate('%Y%m%d', time)


        shouldSkip = False
        for filter in filters:
            if info[1] == filter:
                shouldSkip = True
                break

        if shouldSkip == True:
            continue

        print('Reading '+ info[1] + ' report' )

        #load weekreport
        xlsx_data = ReadXlsx(file)
        dict = AnalyzeXlsx(xlsx_data, keys)
        week_report_data = ReadForm(xlsx_data, dict[keys[0]])
        week_report = WeekReport()
        week_report.ReadData(info[1], week_report_data, _rows[0].__class__)
        report_list.append(week_report)

    #export file
    exporter.ExportReport(report_list, 'D:\\24_report.txt')
    return

def unity_test_ProjectCalendar():
    file= 'D:\\Project\\Git\\python_learning_scripts\\weekly_report_collector\\calendar_cnf.ini'
    pc = ProjectCalendar()
    pc.LoadIni(file)
    print(pc._w1_date)
    print(pc.GetIsoTime('W3.1'))
    print(pc.GetIsoTime('w1.1'))
    print(pc.GetIsoTime('w4.6'))
    return

def unit_test_load_report_ini():
    cf = Report24Category()
    cf.LoadIni(_category_ini_file)
    print(cf)
    print(cf.GetCategory('公会'))
    print(cf.GetCategory('目标选择'))
    print(cf.GetCategory('好友'))
    print(cf.GetCategory('百环'))
    print(cf.GetCategory('NPC|Entity|Monster'))
    return


#unit_test_export_24_report()
unit_test_export_report()
#unity_test_ProjectCalendar()

#unit_test_load_report_ini()
#unit_test_data_time()


