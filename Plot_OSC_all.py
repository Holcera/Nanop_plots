# -*- encoding: utf-8 -*-
'''
@File    :   Plot_OSC_all.py
@Time    :   2024/03/28 23:01:57
@Author  :   Heeeg 
@Version :   1.0
'''
#%%
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.widgets import SpanSelector
from func_read import read_csv
from tkinter import filedialog
#%%
def select_file():
    root = tk.Tk()
    root.withdraw()
    
    file_path = filedialog.askopenfilename()
    
    if file_path:
        print(f"file path: {file_path}")
        return file_path
    else:
        print("No file selected!")
        return None

if __name__ == "__main__":
    select_file()


#%%
filepath = r"/Users/heng_air/Library/CloudStorage/OneDrive-Personal/Lab/Wang/er-sp/yos09241851(41)-up.dat"
data_raw = read_csv(filepath)
for i in range(len(data_raw.columns)):
    data_raw.rename(columns={data_raw.columns[i]: f"ch{i}"}, inplace=True)
    
#%%
plt.figure(figsize=(10, 5))
plt.plot(data_raw.ch0, data_raw.ch1, color='slateblue', lw=1)
# plt.bar(x, y, color='royalblue', width=0.3, lw='0.1', label='power')
# plt.scatter(x, y, color='royalblue', s=10)
plt.xlim(min(data_raw.ch0), max(data_raw.ch0))
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (dBm)')

plt.show()
#%%