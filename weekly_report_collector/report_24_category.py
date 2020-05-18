# -*- coding:utf-8 -*-
import sys,os
import configparser

_item_key = 'item'

class Report24Category:
    def __init__(self):
        self._cf = configparser.ConfigParser()
        self._map = {}

    def LoadIni(self, filePath):
        self._cf.read(filePath)

        #store all the data into map
        for sect in self._cf.sections():
            key = self._cf[sect][_item_key]
            str_list = key.split(',')
            self._map[sect] = str_list

    def GetCategory(self, mod):
        for (key, val) in self._map.items():
            for str in val:
                if(str.lower() == mod.lower()):
                    return key
        return ''

    def __str__(self):
        return self._map.__str__()

    def __repr__(self):
        return self._map.__str__()









