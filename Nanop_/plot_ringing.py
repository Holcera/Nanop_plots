# -*- encoding: utf-8 -*-
'''
@File    :   plot_ringing.py
@Time    :   2023/03/25 20:09:59
@Author  :   Wang Heng 
@Version :   1.0
'''
#%%
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
filepath = r"C:\Users\H\Documents\Lab_BUPT\Data\data5.14\tek0050.csv"
data_raw = pd.read_csv(filepath, 
                       header=19, 
                       na_values='--',
                       usecols=[0, 2]
                       )
re_col = ['time', 'ch1']
data_raw.columns = re_col
# data_raw.reset_index(inplace=True)
#%%
filepath = r"C:\Users\H\Documents\Lab_BUPT\Data\data4.25\tek0011.csv"
data_raw1 = pd.read_csv(filepath, 
                       header=19, 
                       na_values='--',
                       usecols=[0, 1]
                       )
re_col = ['time', 'ch1']
data_raw1.columns = re_col

#%%
fig, axs = plt.subplots(1, 2, figsize=(16, 6), sharex=False)
fig.subplots_adjust(hspace=0.05, wspace=0.2)

axs[0].plot(data_raw.time, data_raw.ch1, color='darkslateblue', alpha=1, lw=1, label='Cavity Exp.')
axs[0].plot()
# axs[0].set_ylim(-75, 5)
axs[0].set_xlim(0.00043, 0.000478)
axs[0].set_xlabel('Time(s)')
axs[0].set_ylabel('voltage (V)')
axs[0].legend(loc='lower right', fontsize=19, frameon=False)
# axs[0].get_xaxis().set_visible(False)
axs[0].locator_params(axis='y', nbins=2)
axs[0].locator_params(axis='x', nbins=3, tight=True)

axs[1].plot(data_raw1.time, data_raw1.ch1, color='darkslateblue', alpha=1, lw=1, label='Cavity Exp.')
# axs[1].set_ylim(-80, 5)
axs[1].set_xlim(0.002859, 0.002867)
axs[1].set_xlabel('Time(s)')
axs[1].set_ylabel('voltage (V)')
# plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
axs[1].legend(loc='lower right', fontsize=19, frameon=False)
axs[1].locator_params(axis='y', nbins=2)
axs[1].locator_params(axis='x', nbins=3, tight=True)

# fig.text(0.5, 0.05, 'Wavelength (nm)', ha='center')
# fig.text(0.04, 0.5, 'Intensity (dBm)', va='center', rotation='vertical')

plt.show()
# %%