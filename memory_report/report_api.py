# -*- coding:utf-8 -*-
from report_enum import *
from report_sum_report import *
from report_module_analyze import *
from report_db import *


def ExportSumReport(file_path, op_path):
    # 1.���ļ�
    db = _load_db(file_path)

    # 2.������db����exporter, ���б��浼��
    print("2. Export sumarized report...")
    exporter = SumReporter()
    exporter.Export(op_path, db)
    print("3. Finished export sumarized report...")
    pass


def _load_db(file_path):
    # 1. ��ʼ���ֲ�����
    res_type = ResType.none
    m_type = ModuleType.none
    db = ReportDb()
    line_count = 0

    # 2.���ļ�
    with open(file_path, 'r') as file:
        print("1. Start reading file ...")
        while True:
            line = file.readline()
            line_count += 1

            if not line:
                break;

            # 3.�����е�����
            line_type = _try_parse_line_type(line)

            # 4.���������ͽ��н���
            if LineType.data == line_type:
                row_data = _analyze_data(line, res_type, m_type)
                db.AddRow(row_data)
            elif LineType.split_group == line_type:
                m_type = _analyze_split_group(line)
                print("has sub_type:", m_type)
            elif LineType.group == line_type:
                res_type = _analyze_group(line)
                m_type = ModuleType.none
                print("Start analyze res:", res_type)
            elif LineType.total_size == line_type:
                pass
            else:
                print("[error]unknown line type : ", line)

    return db


def _try_parse_line_type(line):
    '''
       According to the key word in each line to return line type
    '''
    line_map = {"Group": LineType.group
        , "split_group": LineType.split_group
        , "Total": LineType.total_size
        , "name:": LineType.data}

    for (key, pair) in line_map.items():
        if key in line:
            return pair

    print("[error]unknown line type: ", line)
    return LineType.none


def _analyze_group(line):
    '''
        - According to the key word in the group line to return group type(res type)
        - should change according to the unity engine
    '''
    for name, member in ResType.__members__.items():
        if name in line:
            return member

    print("[error]Unknonw group type: ", line)

    return ResType.none


def _analyze_split_group(line):
    line_map = {"Character": ModuleType.char
        , "Scene": ModuleType.scene
        , "UI": ModuleType.ui
        , "building": ModuleType.scene
        , "Effect": ModuleType.effect
        , "NotFound": ModuleType.misc
        , "ImageEffect": ModuleType.effect
        , "Other": ModuleType.char
        , "water": ModuleType.scene}

    for (key, pair) in line_map.items():
        if key in line:
            return pair

    print("[error]Unknown split_group in line: ", line)
    return ModuleType.none


def _analyze_data(line, res_type, module_type):
    '''
        analyze data line, to return ReportDbRow
    '''
    # 1. find the name, size, path 
    datas = line.split(',')
    datas_len = len(datas)
    path_str = ""
    if 2 == datas_len:
        name_str = _analyze_json_str(datas[0])
        size_str = _analyze_json_str(datas[1])
    elif 3 == datas_len:
        name_str = _analyze_json_str(datas[0])
        size_str = _analyze_json_str(datas[1])
        path_str = _analyze_json_str(datas[2])
    else:
        print("[error]data line format not correct: ", line)
        return

    # 2. according to the name, try to analyze which moduel it belongs to
    name_analyzer = NameAnalyzers()
    new_module_type = name_analyzer.GetModuleType(name_str, res_type, module_type)

    # 3. according to the size, find KB try transfer to MB 
    size = _analyze_size(size_str)

    # 4. create ReportDbRow
    row = ReportDbRow()
    row._res_type = res_type
    row._m_type = new_module_type
    row._size = size
    row._name = name_str
    row._path = path_str

    return row


def _analyze_json_str(str):
    '''
        Given string  "xxx : yyy", return yyy
    '''
    if None == str:
        return ""

    datas = str.split(':')
    return datas[1]


def _analyze_size(str):
    '''
        - input str forma: size:0.05 KB(MB), 
        - len is fixed, so we just need to use length to get substring for the size
        -
    '''
    is_kb = 'KB' in str
    size = float(str.strip()[0:-2])

    if is_kb:
        size = size / 1024
    return size


# ExportSumReport("D:/memory_profile/2019-11-30-linxizheng_end/memory_report.txt", "D:/memory_profile/2019-11-30-linxizheng_end/report.txt")
# ExportSumReport("d:/memory_profile/2019-11-30-linxizheng_start/memory_report.txt", "D:/memory_profile/2019-11-30-linxizheng_start/report.txt")
# ExportSumReport("d:/memory_profile/2019-11-30-character_createor/memory_report.txt", "D:/memory_profile/2019-11-30-character_createor/report.txt")
# ExportSumReport("d:/memory_profile/2019-11-30-jingqiao_start/memory_report.txt", "D:/memory_profile/2019-11-30-jingqiao_start/report.txt")
ExportSumReport("d:/memory_profile/2019-11-30-jingqiao_end/memory_report.txt",
                "D:/memory_profile/2019-11-30-jingqiao_end/report.txt")
