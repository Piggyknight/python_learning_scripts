'''
function to load different weekly report
in .xlsx files
'''
import xlrd


def read_xlsx(file_path):
    '''
    give path return the data of xlsx
    :param file_path: absolute path of the xlsx
    :return: the workbook of slrd
    '''
    try:
        data = xlrd.open_workbook(file_path)
        return data
    except Exception as e:
        print(str(e))

def analyze_xls(xls_data):
    '''
    give xls workbook data, read each line and split form
    according to the key word
    :param xls_data: input xls data
    :return: different forms
    '''
    # all the data must be in the first sheet
    table = xls_data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols



    for row_num in range(1, nrows):
        row = table.row_values(row_num)
        if row









