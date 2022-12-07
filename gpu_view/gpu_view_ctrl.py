# coding:utf8
import conf
import os,time
import subprocess
import shutil

# ---------------动态数据-------------------------
is_profiling = True

def get_time_str_in_data(time_float):
    return time.strftime("%Y%m%d%H%M%S", time.localtime(time_float))

def trigger_profile():
    global is_profiling
    if is_profiling :         
       xperf_path = os.path.dirname(conf.log_cmd_path_abs)
       xperf_path = "\""+xperf_path + "/../Xperf.exe"+"\""
       ex = subprocess.Popen(xperf_path + " -capturestate SchedulingLog 802ec45a-1e99-4b83-9920-87c98277ba9d:0x04000000:5", stdout=subprocess.PIPE, shell=True)
       status = ex.wait()
       ex = subprocess.Popen(xperf_path + " -stop SchedulingLog", stdout=subprocess.PIPE, shell=True)
       status = ex.wait()
       ex = subprocess.Popen(xperf_path + " -stop CaptureState", stdout=subprocess.PIPE, shell=True)
       status = ex.wait()
       ex = subprocess.Popen(xperf_path + " -stop NoCaptureState", stdout=subprocess.PIPE, shell=True)
       status = ex.wait()
       ex = subprocess.Popen(xperf_path + " -stop", stdout=subprocess.PIPE, shell=True)
       status = ex.wait()
       print("Stop xperf...")
    else:
       ex = subprocess.Popen(conf.log_cmd_path_abs, stdout=subprocess.PIPE, shell=True)
       out, err = ex.communicate()
       status = ex.wait()
       print("start log.cmd...")
    
    is_profiling = not is_profiling
    print("Trigger Profiling:", str(is_profiling))

def update_lag_detection_process(cur_time):
    # 检查是核心文件是否存在, 存在则触发数据保存
    is_lag_file_exist = os.path.exists(conf.lag_file_location_abs)
    if is_lag_file_exist :
        print("Found lag file, start move data....")
        # 如果在profiling, 则先停止
        if is_profiling :
            trigger_profile()

        # 准备需要copy的文件名与目标文件名, 通过当前时间命名, 
        move_file_list = {
            "SchedulingLog.etl",
            "NoCaptureState.etl",
            "Kernel.etl",
            "CaptureState.etl",
        }

        target_folder = conf.export_path_abs + "/etl_" + get_time_str_in_data(cur_time)
        os.makedirs(target_folder)

        for file_name in move_file_list :
            target_file = target_folder + "/" + file_name
            shutil.move(file_name, target_file)
            print("move to %s" % (target_file))
        
        # 删除lag file, 不用清空数据, log.cmd会自动清空
        os.remove(conf.lag_file_location_abs)

        return True
    
    return False


def main_func():
    print("Start.....")

    # 检查exe是否存在
    if not os.path.exists(conf.log_cmd_path_abs) :
        print("ERROR: File not exist:", conf.log_cmd_path_abs)
        return
    print("Log.cmd is exist.....")

    # export_loaction是否存在,不存在则创建目录
    if not os.path.exists(conf.export_path_abs) : 
        os.makedirs(conf.export_path_abs)
    print("file will copy to ", conf.export_path_abs)

    # 开始主循环
    cur_time = last_time = time.time()
    cur_countdown = 0.0
    # 先clean然后再启动
    is_profiling = True
    trigger_profile()
    trigger_profile()
    print("Start Monitoring...")
    while True:
        # 开始倒计时
        cur_time = time.time()
        delta = cur_time - last_time
        last_time = cur_time
        cur_countdown += delta

        # 检查一下lag文件是否存在, 存在在处理完文件后则再次进行profile
        has_lag_file = update_lag_detection_process(cur_time)
        if has_lag_file:
            cur_countdown = 0.0
            trigger_profile()

        # 启停log.cmd
        if cur_countdown >= conf.duration_s:
            print("Start Profile again, Duration=", conf.duration_s, "Please don't quit untill it is finished")
            trigger_profile()
            trigger_profile()
            cur_countdown = 0.0
            print("Finished. You may exit now(press ctrl+c) or continue the monitoring")

        # 休息一下
        time.sleep(conf.update_freq_s)

is_profiling = True
trigger_profile()
# main_func()
