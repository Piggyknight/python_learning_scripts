# -*- coding:utf-8 -*-
import os


_ext = '.xlsx'

def _end_with(s, *endstring):
    '''
    :param s: string to search 
    :param endstring: a list of search pattern
    :return: return true if contains any pattern in *endstring, else return false 
    '''
    array = map(s.endswith, endstring)
    if True in array:
        return True
    else:
        return False

def SearchFiles(rootFolder):
    '''
    search all  files under given folder     
    '''
    result = list()
    for rt, dirs, files in os.walk(rootFolder):
        for f in files:
            if _end_with(f, _ext):
                result.append(os.path.join(rt,f))
    return result



'''
give file name return the data & user info 
'''
def GetInfoFromFileName(filePath):
    fileName = os.path.basename(filePath)
    fileName = os.path.splitext(fileName)[0]
    data = fileName.split('_')
    return (data[1], data[2])


