# -*- encoding: utf-8 -*-
'''
@File    :   spanselect.py
@Time    :   2024/03/22 18:05:43
@Author  :   Wang Heng 
@Version :   1.0
'''
#%%
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector
from read_csv_all import read_csv
#%%
def creat_fig(time, trans, mzi):
    fig, (ax1, ax2) = plt.subplots(2, figsize=(10, 7))
    ax1.set(facecolor='#FFFFCC')
    ax2.set(facecolor='#FFFFCC')
    
    print(type(trans[0]))
    print(type(time[0]))
    x0 = range(len(trans))
    print(len(x0), len(trans))
    line1, _ = ax1.plot(time, trans, '.', label='trans')

    # line2, _ = ax1.plot(time, mzi, '.', label='mzi')
    ax1.set_xlim(time[0], time[1])
    ax1.legend(loc=3)
    ax1.set_title("Drag mouse to select")
    
    ax2.plot(time, trans, '.', label='trans')
    ax2.plot(time, mzi, '.', label='mzi')
    ax2.set_xlim(time[0], time[1])
    ax2.legend(loc=3)
    
def main():
    global data_raw
    filepath = r"C:\Users\WANG\OneDrive\KEIO\Wang\OSC\W07.CSV"
    data_raw = read_csv(filepath)
    for i in range(len(data_raw.columns)):
        data_raw.rename(columns={data_raw.columns[i]: f"ch{i}"}, inplace=True) #CH0:time

    time = data_raw.ch0.tolist()
    trans = data_raw.ch1.tolist()
    MZI = data_raw.ch2.tolist()
    
    creat_fig(time, trans, MZI)
    plt.show()

if __name__ == "__main__":
    main()

#%%