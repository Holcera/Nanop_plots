# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 14:33:20 2022

@author: Wang Heng
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pyLPD.MLtools as mlt
from scipy import constants as C
from scipy import optimize
from matplotlib import rcParams

# pd.options.plotting.backend = 'holoviews'
#%%
rcParams['font.family'] = 'Times New Roman'
rcParams['font.size'] = 12

#%%
filepath = r"C:\Users\H\Documents\Lab_BUPT\Data\data12.29\W0030.CSV"
data_raw = pd.read_csv(filepath, 
                       header=32, 
                       na_values='--',
                       usecols=[0, 1]
                       )
data_raw.columns = ['wave', 'power']
# data_raw.reset_index(inplace=True)

print('Memory usage:\n' + 
      str(round(data_raw.shape[1]*
                data_raw.memory_usage(index=False).mean()/1e6, 1)) + 'MB')
# print(data_raw.head())
#%%
plt.figure(figsize=(12, 6))
plt.plot(data_raw.wave, data_raw.power, color='royalblue')
# plt.bar(data_raw.wave, data_raw.dbm, color='royalblue', width=0.3, lw='0.1', label='power')
# plt.scatter(data_raw.wave, data_raw.dbm, color='royalblue', s=10)
plt.ylim(-80, 5)
plt.xlim(min(data_raw.wave), max(data_raw.wave))
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (dBm)')
plt.locator_params(axis='y', nbins=4)
plt.locator_params(axis='x', nbins=3)

plt.show()
#%%
ind_max, maxtab, ind_min, mintab = mlt.peakdet(data_raw.power.values, 10)

plt.figure(figsize=(12, 6))
plt.plot(data_raw.wave, data_raw.power, color='royalblue', lw=0.6)
plt.scatter(data_raw.wave[ind_max], maxtab, color='darkred', s=20)
# plt.scatter(data_raw.wave[ind_min], mintab, color='seagreen', s=20)
plt.ylim(-80, 5)
plt.xlim(min(data_raw.wave), max(data_raw.wave))
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (dBm)')
plt.locator_params(axis='y', nbins=4)
plt.locator_params(axis='x', nbins=3)

plt.show()
#%%
def sech2func(x):
    return (1.0/np.cosh(x))**2

def sech2fit(x, A0, A, x0, width):
    """sech^2 fitting of soliton
        A0 - bg
        A - amp
        x0 - center
        width - width
        oms - center_shift #fit para
    """
    return A0+A*sech2func((x-x0)/width)

#%%
idx_fit = []
tab_fit = []
for i in range(0, len(ind_max)):
      if maxtab[i] >= -67:
            idx_fit.append(ind_max[i])
            tab_fit.append(maxtab[i])

# idx_fit1 = range(0, len(tab_fit))
# idx_fit1 = data_raw.wave.values[idx_fit]          
# plt.figure(figsize=(12, 6))
# plt.scatter(idx_fit, tab_fit, color='royalblue', s=20)
# plt.ylim(-80, 5)
# plt.xlabel('Wavelength (nm)')
# plt.ylabel('Intensity (dBm)')

# plt.show()
#%%
data_fit = pd.DataFrame()
data_fit['wave_fit'] = data_raw.wave.values[idx_fit]
data_fit['power_fit'] = tab_fit
data_fit['omega'] = 2*np.pi*C.c/(data_fit.wave_fit*1e-9)

data_fit.drop(data_fit[data_fit['wave_fit']>=1580].index, inplace=True)
data_fit.drop(data_fit[data_fit['wave_fit']<=1520].index, inplace=True)
# data_fit.drop(data_fit[data_fit['power_fit']==max(tab_fit)].index, inplace=True)
data_fit.reset_index(drop=True, inplace=True)

print(data_fit.head())
#%%
A0_es = min(tab_fit[0], tab_fit[-1])
x0_es = data_fit.wave_fit[np.argmax(tab_fit)]
A_es = max(tab_fit)
width_es = 20.0
# oms = 0
guess0 = [A0_es, A_es, x0_es, width_es]

x1 = data_fit.wave_fit.values
y1 = data_fit.power_fit.values

pfit,pcov = optimize.curve_fit(sech2fit, x1, y1, p0=guess0, maxfev=4500)
p_err = np.sqrt(pcov.diagonal())

print(x0_es)
print(*pfit)
print('cov_error:\n', *p_err)

plt.figure(figsize=(12, 6))
plt.plot(data_raw.wave, data_raw.power, color='royalblue', lw=1, alpha=1)
plt.scatter(x1, y1, color='seagreen', s=20, alpha=0.8)
plt.plot(x1, sech2fit(x1, *pfit), c='darkred', lw=5)
plt.plot(data_raw.wave, sech2fit(data_raw.wave, *pfit), c='orange', lw=2)
plt.ylim(-80, 5)
plt.xlim(min(data_raw.wave), max(data_raw.wave))
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (dBm)')

plt.show()
#%%
plt.figure(figsize=(10, 6))
plt.plot(data_raw.wave, data_raw.power, color='royalblue', lw=1, alpha=1)
# plt.scatter(x1, y1, color='seagreen', s=20, alpha=0.8)
# plt.plot(x1, sech2fit(x1, *pfit), c='black', lw=3, ls='-.')
plt.plot(data_raw.wave, sech2fit(data_raw.wave, *pfit), c='black', lw=3, ls='-.')
plt.ylim(-75, 5)
plt.xlim(min(data_raw.wave), max(data_raw.wave)-1)
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (dBm)')
plt.locator_params(axis='y', nbins=4)
plt.locator_params(axis='x', nbins=4)

plt.show()
#%%
fr0_p = C.c/(x0_es*1e-9)
fr0_s = C.c/(pfit[2]*1e-9)
fr_shift = abs(fr0_p-fr0_s)*1e-9 #GHz

wid_fwhm = (np.pi*pfit[3])/2
#%%
def save_para():
      data_fit.to_csv(r'C:\Users\H\Documents\Lab_BUPT\Data\sech2fit_data.csv', encoding='utf-8')
#%%