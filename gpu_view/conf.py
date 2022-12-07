# coding:utf8
# 多少时间启停exe一次
duration_s = 30.0

# gpuview的log.cmd的目录
log_cmd_path_abs = "c:/Program Files (x86)/Windows Kits/10/Windows Performance Toolkit/gpuview/log.cmd"

# 由于python的subprocess与system每次运行都是独立, 无法共享环境变量, 因此我们专门自己修改了一个stop cmd
log_cmd_stop_path = "log_stop.cmd"

# 检查存在该文件则进行保存
lag_file_location_abs = "d:/test.txt"

# 触发卡顿保存的文件目录
export_path_abs = "d:/gpu_view"

# 需要保存的etl数据文件
copy_file = "Merged.etl"

# python脚本刷新频率
update_freq_s = 1.0 / 60.0
