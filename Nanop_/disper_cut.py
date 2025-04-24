# -*- coding: utf-8 -*-
"""
Created on Sun May 22 14:33:20 2022

@author: Wang Heng
"""
from cProfile import label
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import hvplot.pandas
import holoviews as hv
import pyLPD.MLtools as pmlt
from pyparsing import alphas
import scipy
from bokeh.plotting import show
from scipy import signal, optimize, signal, interpolate
from scipy import constants as C
# pd.options.plotting.backend = 'holoviews'

#%%
filepath = r"C:\Users\H\Documents\Lab_BUPT\Data\DAQ_data\DAQ-4-3mm-mgf2.csv"
data_raw = pd.read_csv(filepath, 
                       header=3, 
                       na_values='--',
                       usecols=[0, 1, 3]
                       )

re_col = ['time', 'MZI', 'trans']
data_raw.columns = re_col
# data_raw.reset_index(inplace=True)

print('Memory usage:\n' + 
      str(round(data_raw.shape[1]*
                data_raw.memory_usage(index=False).mean()/1e6, 1)) + 'MB')
print(data_raw.head())
#%%
t_start = 2.944
t_end = 26.1300

t_start = data_raw[data_raw['time'] >= t_start].index.tolist()[0]
t_end = data_raw[data_raw['time'] <= t_end].index.tolist()[-1]
data_cut = data_raw.iloc[t_start:t_end, :].copy()

data_cut.reset_index(drop=True, inplace=True)
# data_cut.drop(['index'], axis=1, inplace=True)

print('Memory usage:\n' + 
      str(round(data_cut.shape[1]*
                data_cut.memory_usage(index=False).mean()/1e6, 1)) + 'MB')
print(data_cut)
#%%
plt.figure(figsize=(15, 3))
# plt.plot(data_cut.index, data_cut.gas, c='r', lw=1, alpha=0.7, label='gas')
plt.plot(data_cut.time, data_cut.trans, c='b', lw=1, alpha=0.7, label='trans')
plt.plot(data_cut.time, data_cut.MZI, c='green', label='mzi')
plt.legend(loc=7, bbox_to_anchor=(1, 0.5))

plt.show()
#%%
data_save = pd.DataFrame()
data_save['mzi'] = data_cut.MZI
data_save['trans'] = data_cut.trans

data_save.to_csv(r"C:\Users\H\Documents\Lab_BUPT\Data\0DIspersion_data\2nm.csv", encoding='utf-8')
#%%