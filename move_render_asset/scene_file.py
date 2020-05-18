'''
    class Scene will read the .txt under given folder with following format

    [scene_data]
    sub_scene=000100_10000
    night=000100_main

    class SceneDb will read all the txt under root folder. Need to check 
'''

import configparser,os

_section_key = 'scene_data'
_sub_key = 'sub_scene'
_day_key = 'day'
_night_key = 'night'
_ext = '.txt'

_scene_debug_format = 'level: %s, sub: %s, day: %s, night: %s'

class Scene:
    def __init__(self):
        self._day = ''
        self._night = ''
        self._sub = ''
        self._level =''

    def Load(self, file_path):
        cf = configparser.RawConfigParser()
        cf.read(file_path)

        if not cf.has_section(_section_key):
            return
        
        if cf.has_option(_section_key, _day_key):
            self._day = cf[_section_key][_day_key]
        
        if cf.has_option(_section_key, _night_key):
            self._night=cf[_section_key][_night_key]

        if cf.has_option(_section_key, _sub_key):
            self._sub = cf[_section_key][_sub_key]
            self._level = self._sub.split('_')[0]

    def __str__(self):
        return  _scene_debug_format % (self._level, 
                                self._sub,
                                self._day,
                                self._night)

    def __repr__(self):
        return _scene_debug_format % (self._level,
                                self._sub,
                                self._day,
                                self._night)

class SceneDb:
    def __init__(self):
        self._all_scenes = list()

    def _search_files(self, rootFolder):
        '''
            search all  files under given folder     
        '''
        result = list()
        for rt, dirs, files in os.walk(rootFolder):
            for f in files:
                if self._end_with(f, _ext):
                    result.append(os.path.join(rt,f))
        return result

    def _end_with(self, s, *endstring):
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

    def Load(self, root_folder):
        files = self._search_files(root_folder)
        for f in files:
            s = Scene()
            s.Load(f)
            self._all_scenes.append(s)

    def __str__(self):
        lines= list()
        for s in self._all_scenes:
            lines.append(s.__str__())
        return lines

    def __repr__(self):
        lines = list()
        for s in self._all_scenes:
            lines.append(s.__str__())
        return lines




