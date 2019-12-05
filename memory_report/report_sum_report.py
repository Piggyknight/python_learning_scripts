# -*- coding:utf-8 -*-

from my_linq import *
from report_enum import *

class SumReporter:
    def __init__(self):
        pass

    def Export(self, op_path, db):
        op_str=''
        # 1. loop all the module type to find correcsponding res
        for name,m_type in ModuleType.__members__.items():
            res = linq(db._db).where(lambda x : x._m_type == m_type).tolist()
            print("[report]Cal res %s, size %d" %(name, len(res))) 

            if 0 == len(res):
                continue;
            
            # 1.1 calculate all res size
            sum = 0.0
            for row in res:
                sum += row._size

            op_str += 'Module:%s, size:%.3f MB\n' %(name, sum)
            
            # 1.2 loop all the res type, cal its size
            for r_name, r_type in ResType.__members__.items():
                t_res = linq(res).where(lambda x: x._res_type == r_type).tolist()
                if 0 == len(t_res):
                    continue

                sum = 0.0
                for row in t_res:
                    sum += row._size

                op_str += '\t\tres:%s, size:%.3f MB\n' % (r_name, sum)

        # write string into file
        with open(op_path, 'w',encoding='utf-8') as file:
            file.write(op_str)

