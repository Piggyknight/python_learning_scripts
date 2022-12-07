import os
import csv
import subprocess
from datetime import datetime

csv_file_abs = "d:\\gpu_view\\FrameTime_2022_12_5_17_40_08.csv"
etl_file_abs = "d:\\gpu_view\\etl_test\\Merged.etl"
export_path_abs = "d:\\gpu_view\\etl_test\\test.etl"

jag_file_path = "./jag_time.txt"

# input: 2022_12_5_17_40_28 
# output: 12/05/2022 17:40:28
def FormatTimeStr(old_time_str):
    output_data_format = ""
    date = datetime.strptime(old_time_str, '%Y_%m_%d_%H_%M_%S')
    return date.strftime('%m/%d/%Y %H:%M:%S')

def ToFile(export_path, str_list):
    with open(export_path, "w+") as f:
        for str in str_list:
            f.write(str+"\n")

def main():
    # read csv , find jag time when renderwait > 20ms
    data_list = []
    with open(csv_file_abs, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            rw_time = float(row["RenderWait"])
            if rw_time > 20.0:
                jag_time = row["Date"]
                list.append(data_list, FormatTimeStr(jag_time))
                print("Found Jag Time: %s, RenderWait Time: %s" % (jag_time, rw_time))

    data_len = len(data_list)
    print("Analyze CSV finished, found %d jag data " % (data_len))
    
    if data_len == 0:
        return

    # export jag time to txt
    print("Export jag_time.txt.....")
    ToFile(jag_file_path, data_list)

    # call exe
    print("Filter data.....")
    ex = subprocess.Popen("\"./Filter.exe\" " + etl_file_abs +" "+ jag_file_path+" "+export_path_abs, stdout=subprocess.PIPE, shell=True)
    ex.wait()
    print("Done.....")

    return


main()