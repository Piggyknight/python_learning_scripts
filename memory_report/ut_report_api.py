# -*- coding:utf-8 -*-

import report_api,math
from my_linq import *
from report_enum import *
from report_sum_report import SumReporter


ut_tex_path = "d:/Project/python_learning_scripts/memory_report/ut_data/ut_texture2d.txt"
ut_particle_system_path = "d:/Project/python_learning_scripts/memory_report/ut_data/ut_particle_system.txt"
ut_animator_path = "d:/Project/python_learning_scripts/memory_report/ut_data/ut_animator.txt"
ut_animator_op_path = "d:/Project/python_learning_scripts/memory_report/ut_data/ut_animator_export.txt"

def UnitTestAll():
    UT_ParseTextuer2D()
    UT_ParseParticleSystem()
    UI_ParseAnimator()
    UI_ExportReport()
     
def UT_ParseTextuer2D():
    db = report_api._load_db(ut_tex_path)
    assert linq(db._db).where(lambda x: x._res_type == ResType.Texture2D).count() == 24,"texture type not correct"
    assert linq(db._db).where(lambda x: x._m_type == ModuleType.char).count() == 7, "char type not correct"
    assert linq(db._db).where(lambda x: x._m_type == ModuleType.scene).count() == 7,"scene type not correct"
    assert linq(db._db).where(lambda x: x._m_type == ModuleType.effect).count() == 5,"effect type not correct"
    assert linq(db._db).where(lambda x: x._m_type == ModuleType.ui).count() == 3, "ui type not correct"
    
    
    misc = linq(db._db).where(lambda x: x._m_type == ModuleType.misc).tolist()
    sum = 0.0
    for row in misc:
        sum += row._size 
    assert len(misc) == 2, "misc type not correct"
    assert math.isclose(sum, 10.4), "size not correct"

    print("[test success]UT_ParseTextuer2D")

def UT_ParseParticleSystem():
    db = report_api._load_db(ut_particle_system_path)

    ps = linq(db._db).where(lambda x: x._res_type == ResType.ParticleSystem).tolist()
    sum = 0.0
    for row in ps:
        sum += row._size

    assert len(ps) == 2 , "particle sytem count error"
    assert math.isclose(sum, (15 + 14.9)/1024), "particle kb size is not correct"
    print("[test success]UT_ParseParticleSystem")

def UI_ParseAnimator():
    db=report_api._load_db(ut_animator_path)

    assert linq(db._db).where(lambda x: x._res_type == ResType.Animator).count() == 7, "animator type error"
    assert linq(db._db).where(lambda x: x._m_type == ModuleType.char).count() == 3, "animator char note correct"
    assert linq(db._db).where(lambda x: x._m_type == ModuleType.ui).count() == 1, "animator ui not correct"
    assert linq(db._db).where(lambda x: x._m_type == ModuleType.scene).count() == 2, "animator scene not correct"
    assert linq(db._db).where(lambda x: x._m_type == ModuleType.effect).count() == 1, "animator scene not correct"
    print("[test success]UI_ParseAnimator")

def UI_ExportReport():
    report_api.ExportSumReport(ut_animator_path, ut_animator_op_path)
    

print("Start Unit Test...")
UnitTestAll();
print("Unit Test Finished")