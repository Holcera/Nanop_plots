# -*- coding: utf-8 -*-
"""
Created on Sun Oct 8 14:33:20 2022

@author: Wang Heng
"""
from cProfile import label
import pandas as pd
import numpy as np
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
filepath = r"C:\Users\H\Documents\Lab_BUPT\Data\Convert\disper_AOM1.csv"
data_raw = pd.read_csv(filepath, 
                       header=None, 
                       na_values='--',
                       usecols=[0, 1, 2]
                       )
data_raw.columns = ['mu', 'freq', 'fitting']
# data_raw.reset_index(inplace=True)
# data_raw[['mu']] = data_raw[['mu']].astype(int)

print('Memory usage:\n' + 
      str(round(data_raw.shape[1]*
                data_raw.memory_usage(index=False).mean()/1e6, 1)) + 'MB')
print(data_raw.head())
#%%
def fit_func2(x, *p):
      return p[0] + p[1]*x + p[2]*x**2/2
#%%
# x = []
# for i in range(int(min(data_raw.mu)), int(max(data_raw.mu))+1):
#       x.append(i)
x = np.arange(min(data_raw.mu), max(data_raw.mu))
pfit = data_raw.fitting.values
#%%
plt.figure(figsize=(8, 6),)
# plt.plot(data_raw.wavelength, data_raw.dbm, color='royalblue', label='power')
# plt.bar(data_raw.wavelength, data_raw.dbm, color='royalblue', width=0.3, lw='0.1', label='power')
plt.scatter(data_raw.mu, data_raw.freq, color='royalblue', s=20, label='data_raw',  alpha=0.7)
plt.plot(x, fit_func2(x, *pfit), 'r', lw=2, label='dispersion_fit')

# plt.xlim(min(data_raw.wavelength), max(data_raw.wavelength))
plt.axvline(x=0, ls='-.', color='g', lw=1.5, alpha=0.5)
plt.axhline(y=0, ls='-.', color='g', lw=1.5, alpha=0.5)
# plt.title(label='λ0=1550.11, D1=25.97(GHz), D2=200.7(kHz), D3=983(Hz)')
plt.xlabel('Mode number (u)')
plt.ylabel('Relative Mode Frequency (MHz)')
plt.legend(loc='upper right',fontsize=17, frameon=False)

plt.show()
#%%
plt.figure(figsize=(8, 6))
# plt.plot(data_raw.wavelength, data_raw.dbm, color='royalblue', label='power')
# plt.bar(data_raw.wavelength, data_raw.dbm, color='royalblue', width=0.3, lw='0.1', label='power')
plt.scatter(data_raw.mu, data_raw.freq, color='royalblue', s=50, label='Cavity Exp.',  alpha=0.8)
plt.plot(x, fit_func2(x, *pfit), 'darkred', lw=5, label='Fitting')

plt.ylim(-0.15e3, 0.7e3)
# plt.axvline(x=0, ls='-.', color='g', lw=1.5, alpha=0.5)
# plt.axhline(y=0, ls='-.', color='g', lw=1.5, alpha=0.5)
# plt.title(label='λ0=1550.11, D1=25.97(GHz), D2=455.7(kHz)')
plt.xlabel('Mode number (u)')
plt.ylabel('Relative Mode Frequency (MHz)')
plt.locator_params(axis='y', nbins=2)
plt.locator_params(axis='x', nbins=3)
plt.legend(loc='center right',fontsize=17, frameon=False)

plt.show()
# %%
