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
from matplotlib import rcParams
# pd.options.plotting.backend = 'holoviews'
#%%
rcParams['font.family'] = 'Times New Roman'
rcParams['font.size'] = 20
#%%
filepath = r"C:\Users\H\Documents\Lab_BUPT\Data\data10.7\tek0102.csv"
data_raw = pd.read_csv(filepath, 
                       header=19, 
                       na_values='--',
                       usecols=[0, 2]
                       )
re_col = ['time', 'ch1']
data_raw.columns = re_col
# data_raw.reset_index(inplace=True)

# print('Memory usage:\n' + 
#       str(round(data_raw.shape[1]*
#                 data_raw.memory_usage(index=False).mean()/1e6, 1)) + 'MB')
# print(data_raw.head())
#%%
filepath = r"C:\Users\H\Documents\Lab_BUPT\Data\data9.23\tek0096.csv"
data_raw1 = pd.read_csv(filepath, 
                       header=19, 
                       na_values='--',
                       usecols=[0, 2]
                       )
re_col = ['time', 'ch3']
data_raw1.columns = re_col


#%%
#%%
fig, axs = plt.subplots(2, 1, figsize=(18, 7), sharex=False)
fig.subplots_adjust(hspace=0.05, wspace=0.2)

axs[0].plot(data_raw.time, data_raw.ch1, color='darkslateblue', alpha=1, lw=1, label='Cavity Exp.')
# axs[0, 0].set_ylim(-75, 5)
# axs[0].set_xlim(min(data_raw.time.values), max(data_raw.time.values))
axs[0].set_xlabel('Time(s)')
axs[0].set_ylabel('voltage (V)')
axs[0].legend(loc='upper left', fontsize=19, frameon=False)
axs[0].get_xaxis().set_visible(False)
# axs[0, 0].text(1587, -10, 'I', fontsize=13)
axs[0].locator_params(axis='y', nbins=2)
# axs[0].locator_params(axis='x', nbins=3, tight=True)

axs[1].plot(data_raw1.time, data_raw1.ch3, color='darkslateblue', alpha=1, lw=2, label='Cavity Exp.')
# axs[1].set_ylim(-80, 5)
# axs[1].set_xlim(min(data_raw1.time.values), 0.005)
axs[1].set_xlabel('Time(s)')
axs[1].set_ylabel('voltage (V)')
# plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
# axs[1, 0].text(1587, -10, 'II', fontsize=13)
axs[1].legend(loc='upper left', fontsize=19, frameon=False)
axs[1].locator_params(axis='y', nbins=2)
axs[1].locator_params(axis='x', nbins=4, tight=True)

# fig.text(0.5, 0.05, 'Wavelength (nm)', ha='center')
# fig.text(0.04, 0.5, 'Intensity (dBm)', va='center', rotation='vertical')

plt.show()
# %%
