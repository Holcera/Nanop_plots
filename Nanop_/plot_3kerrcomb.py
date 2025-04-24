# -*- encoding: utf-8 -*-
'''
@File    :   plot_3kerrcomb.py
@Time    :   2023/03/26 15:11:40
@Author  :   Wang Heng 
@Version :   1.0
'''
#%%
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pyLPD.MLtools as mlt
from bokeh.plotting import show
from scipy import constants as C
from scipy import optimize
from matplotlib import rcParams

# pd.options.plotting.backend = 'holoviews'

#%%
rcParams['font.family'] = 'Times New Roman'
rcParams['font.size'] = 24
#%%
filespath = r"C:\Users\H\Documents\Lab_BUPT\Paper\毕业论文\4chapter\kerr_comb"
files = []
for i in os.listdir(filespath):
    name, ext = os.path.splitext(i)
    if ext == '.CSV':
        files.append(i)

files[0], files[3] = files[3], files[0]
files[2], files[3] = files[3], files[2]
files[2], files[1] = files[1], files[2]


data_raw = pd.DataFrame()
for i in range(len(files)):
      file = filespath + '\\' + files[i]
      data = pd.read_csv(file, 
                        header=32, 
                        na_values='--',
                        usecols=[0, 1]
                        )
      data_raw = pd.concat([data_raw, data], axis=1)
data_raw.columns = ['wave1', 'power1', 'wave2', 'power2', 'wave3', 'power3',
                    'wave4', 'power4']
# data_raw.reset_index(inplace=True)

print('Memory usage:\n' + 
      str(round(data_raw.shape[1]*
                data_raw.memory_usage(index=False).mean()/1e6, 1)) + 'MB')
#%%
fig, axs = plt.subplots(4, 1, figsize=(9, 12), sharex=False)
fig.subplots_adjust(hspace=0, wspace=0.2)

axs[0].plot(data_raw.wave1, data_raw.power1, color='darkslateblue', alpha=1, lw=1)
axs[0].set_ylim(-80, -15)
axs[0].set_xlim(min(data_raw.wave1), max(data_raw.wave1))
axs[0].set_xlabel('Wavelength (nm)')
# axs[0].set_ylabel('Intensity (dBm)')
axs[0].legend(loc='upper right', fontsize=19, frameon=False)
axs[0].get_xaxis().set_visible(False)
axs[0].get_yaxis().set_ticklabels([])
axs[0].locator_params(axis='y', nbins=2)
axs[0].locator_params(axis='x', nbins=3, tight=True)

axs[1].plot(data_raw.wave2, data_raw.power2, color='darkslateblue', alpha=1, lw=1)
axs[1].set_ylim(-80, -25)
axs[1].set_xlim(min(data_raw.wave2), max(data_raw.wave2))
axs[1].set_xlabel('Wavelength (nm)')
# axs[1].set_ylabel('Intensity (dBm)')
# plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
axs[1].get_xaxis().set_visible(False)
axs[1].get_yaxis().set_ticklabels([])
axs[1].legend(loc='lower right', fontsize=19, frameon=False)
axs[1].locator_params(axis='y', nbins=2)
axs[1].locator_params(axis='x', nbins=3, tight=True)

axs[2].plot(data_raw.wave3, data_raw.power3, color='darkslateblue', alpha=1, lw=1)
axs[2].set_ylim(-80, -20)
axs[2].set_xlim(min(data_raw.wave3), max(data_raw.wave3))
axs[2].set_xlabel('Wavelength (nm)')
# axs[2].set_ylabel('Intensity (dBm)')
axs[2].legend(loc='upper right', fontsize=19, frameon=False)
axs[2].get_xaxis().set_visible(False)
axs[2].get_yaxis().set_ticklabels([])
axs[2].locator_params(axis='y', nbins=2)
axs[2].locator_params(axis='x', nbins=3, tight=True)

axs[3].plot(data_raw.wave4, data_raw.power4, color='darkslateblue', alpha=1, lw=1)
axs[3].set_ylim(-80, -20)
axs[3].set_xlim(min(data_raw.wave3), max(data_raw.wave3))
axs[3].set_xlabel('Wavelength (nm)')
# axs[3].set_ylabel('Intensity (dBm)')
axs[3].legend(loc='upper right', fontsize=19, frameon=False)
# axs[0].get_xaxis().set_visible(False)
axs[3].get_yaxis().set_ticklabels([])
axs[3].locator_params(axis='y', nbins=2)
axs[3].locator_params(axis='x', nbins=3, tight=True)

# fig.text(0.5, 0.05, 'Wavelength (nm)', ha='center')
fig.text(0.04, 0.5, 'Intensity (25dBm/div)', va='center', rotation='vertical')

plt.show()
#%%