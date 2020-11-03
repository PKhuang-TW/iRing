import serial
import csv
import numpy as np
import pandas as pd

COM_PORT = '/dev/cu.usbmodem14401'    # 指定通訊埠名稱
BAUD_RATES = 9600    # 設定傳輸速率
ser = serial.Serial(COM_PORT, BAUD_RATES)   # 初始化序列通訊埠

s0_vals = []
s1_vals = []
s2_vals = []
s3_vals = []
avg_vals = []

try:
    while True:
        while ser.in_waiting:          # 若收到序列資料…
            data_raw = ser.readline()  # 讀取一行
            data = data_raw.decode()   # 用預設的UTF-8解碼
            data_list = list(map(int, data.split(',')))
            avg = int((np.asarray(data_list)).mean())

            s0_vals.append(data_list[0])
            s1_vals.append(data_list[1])
            s2_vals.append(data_list[2])
            s3_vals.append(data_list[3])
            avg_vals.append(avg)
            
             
 
except KeyboardInterrupt:
    ser.close()    # 清除序列通訊物件

    s0_vals.append(np.asarray(s0_vals).mean())
    s1_vals.append(np.asarray(s1_vals).mean())
    s2_vals.append(np.asarray(s2_vals).mean())
    s3_vals.append(np.asarray(s3_vals).mean())
    avg_vals.append(np.asarray(avg_vals).mean())

    dict = {
        "S0": s0_vals,  
        "S1": s1_vals, 
        "S2": s2_vals,
        "S3": s3_vals,
        "AVG": avg_vals
    }
    df = pd.DataFrame(dict)

    try:
        with open('data.csv', 'a') as f:
            f.write(df)
            print('try')
    except:
        # xport_csv = df.to_csv('NotWearingData.csv')
        # export_csv = df.to_csv('WearingData.csv')
        export_csv = df.to_csv('BendingData.csv')
        # export_csv = df.to_csv('90_degData.csv')
        # export_csv = df.to_csv('180_degData.csv')
        # export_csv = df.to_csv('270_degData.csv')
        # print('except')