# coding:utf8
import conf
import os,time
import subprocess
import shutil

def main_func():
    print("Start Merging.....")
    
    xperf_path = os.path.dirname(conf.log_cmd_path_abs)
    xperf_path = "\""+xperf_path + "/../Xperf.exe"+"\""

    file_list = {
        "SchedulingLog.etl",
        "NoCaptureState.etl",
        "Kernel.etl",
        "CaptureState.etl",
    }

    merge_str = " -merge %s/Kernel.etl %s/NoCaptureState.etl %s/CaptureState.etl %s/SchedulingLog.etl %s/Merged.etl"
    for rt, dirs, files in os.walk(conf.export_path_abs):
        for dir_name in dirs:
            if "etl_" not in dir_name :
                continue
            print("Hanlde dir:%s..." % dir_name)
            cmd_str = merge_str % (dir_name,dir_name,dir_name,dir_name,dir_name)
            ex = subprocess.Popen(xperf_path + cmd_str, stdout=subprocess.PIPE, shell=True)
            status = ex.wait()

    print("Finsihed.........")

main_func()
