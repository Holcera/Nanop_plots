# -*- coding: utf-8 -*-
"""
Created on Sun Oct 8 14:33:20 2022

@author: Wang Heng
"""
import pandas as pd
import matplotlib.pyplot as plt
import hvplot.pandas
import holoviews as hv
from bokeh.plotting import show
from scipy import constants as C
# pd.options.plotting.backend = 'holoviews'

#%%
filepath = r"C:\Users\H\OneDrive\KEIO\Wang\OSC\W02.CSV"
data_raw = pd.read_csv(filepath, 
                       header=19, 
                       na_values='--',
                       usecols=[0, 1, 2]
                       )
re_col = ['time', 'ch1', 'ch2']
data_raw.columns = re_col
# data_raw.reset_index(inplace=True)

# print('Memory usage:\n' + 
#       str(round(data_raw.shape[1]*
#                 data_raw.memory_usage(index=False).mean()/1e6, 1)) + 'MB')
# print(data_raw.head())
#%%
plt.figure(figsize=(14, 4))

# plt.plot(data_raw.time, data_raw.ch1, color='darkslateblue', label='Cavity Exp.', lw=1)
plt.plot(data_raw.time, data_raw.ch2, color='r', label='comb')
# plt.plot(data_raw.time, data_raw.ch3, color='orange', label='comb')
# plt.plot(data_raw.time, data_raw.ch4, color='seagreen', label='comb')
# plt.bar(data_raw.wavelength, data_raw.dbm, color='royalblue', width=0.3, lw='0.1', label='power')
# plt.scatter(data_raw.wavelength, data_raw.dbm, color='royalblue', s=10)
# plt.ylim(0.3, 0.55)
# plt.xlim(-0.0002370, -0.0001054)
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
plt.legend(loc='lower right', fontsize=15, frameon=False)
plt.locator_params(axis='x', nbins=2, tight=True)
plt.locator_params(axis='y', nbins=2, tight=True)

plt.show()
#%%
