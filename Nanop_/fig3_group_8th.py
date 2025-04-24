# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 14:33:20 2022

@author: Wang Heng
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import pyLPD.MLtools as mlt
from scipy import constants as C
from scipy import optimize
from sympy import Symbol
from sympy import solve
from matplotlib import rcParams
#%%
rcParams['font.family'] = 'Times New Roman'
rcParams['font.size'] = 20
#%% fig2
filespathfig2 = r"C:\Users\H\Documents\Lab_BUPT\Paper\soliton_AOM_23.1.11\fig2"
filesfig2 = []
for i in os.listdir(filespathfig2):
    name, ext = os.path.splitext(i)
    if ext == '.CSV':
        filesfig2.append(i)

data_rawfig2 = pd.DataFrame()
for i in range(len(filesfig2)):
      file = filespathfig2 + '\\' + filesfig2[i]
      data = pd.read_csv(file, 
                        header=32, 
                        na_values='--',
                        usecols=[0, 1]
                        )
      data_rawfig2 = pd.concat([data_rawfig2, data], axis=1)
data_rawfig2.columns = ['wave1', 'power1', 'wave2', 'power2', 'wave3', 'power3',
                    'wave4', 'power4', 'wave5', 'power5']
# data_rawfig2.reset_index(inplace=True)

print('Memory usage:\n' + 
      str(round(data_rawfig2.shape[1]*
                data_rawfig2.memory_usage(index=False).mean()/1e6, 1)) + 'MB')
# print(data_rawfig2.head())
crop1fig2 = []
crop1fig2 = data_rawfig2.loc[(data_rawfig2.power1 >= -80)].index

crop2fig2 = []
crop2fig2 = data_rawfig2.loc[(data_rawfig2.power2 >= -80)].index

crop3fig2 = []
crop3fig2 = data_rawfig2.loc[(data_rawfig2.power3 >= -80)].index

crop4fig2 = []
crop4fig2 = data_rawfig2.loc[(data_rawfig2.power4 >= -80)].index

crop5fig2 = []
crop5fig2 = data_rawfig2.loc[(data_rawfig2.power5 >= -80)].index
#%%
filespath = r"C:\Users\H\Documents\Lab_BUPT\Paper\soliton_AOM_23.1.11\fig4"
files = []
for i in os.listdir(filespath):
    name, ext = os.path.splitext(i)
    if ext == '.CSV':
        files.append(i)
        
data_rawfig4 = pd.DataFrame()
for i in range(len(files)):
      file = filespath + '\\' + files[i]
      data = pd.read_csv(file, 
                        header=32, 
                        na_values='--',
                        usecols=[0, 1]
                        )
      data_rawfig4 = pd.concat([data_rawfig4, data], axis=1)
data_rawfig4.columns = ['wave1', 'power1', 'wave2', 'power2', 'wave3', 'power3',
                    'wave4', 'power4', 'wave5', 'power5']
crop1 = []
crop1 = data_rawfig4.loc[(data_rawfig4.power1 >= -80)].index

crop2 = []
crop2 = data_rawfig4.loc[(data_rawfig4.power2 >= -80)].index

crop3 = []
crop3 = data_rawfig4.loc[(data_rawfig4.power3 >= -80)].index

crop4 = []
crop4 = data_rawfig4.loc[(data_rawfig4.power4 >= -80)].index

crop5 = []
crop5 = data_rawfig4.loc[(data_rawfig4.power5 >= -80)].index
#%%
parapath2 = r"C:\Users\H\Documents\Lab_BUPT\Paper\soliton_AOM_23.1.11\fig2\allfig2.csv"
data_para2 = pd.read_csv(parapath2, header=0, na_values="--")
parapath4 = r"C:\Users\H\Documents\Lab_BUPT\Paper\soliton_AOM_23.1.11\fig4\allfig4.csv"
data_para4 = pd.read_csv(parapath4, header=0, na_values="--")

detufig2 = data_para2.detunings.values
detufig4 = data_para4.detunings.values
width2 = data_para2.width.values
width4 = data_para4.width.values
pumpfig2 = data_para2.pump_power.values
pumpfig4 = data_para4.pump_power.values
volfig2 = [10, 9.5, 9, 8.5, 8] #v
volfig4 = [8, 8.5, 9, 9.5, 10]
solpower2 = data_para2.sol_power.values
solpower4 = data_para4.sol_power.values
recoil2 = data_para2.recoil.values
recoil4 = data_para4.recoil.values
#%%
def fitting2(x, A, b):
      return ((A/x)**(1/2))+b
#%%
detunings = np.concatenate((detufig2, detufig4), axis=0)
width = np.concatenate((width2, width4), axis=0)
solpower = np.concatenate((solpower2, solpower4), axis=0)

detunings.sort()
width.sort()
width = width[::-1] #reverse
x11 = np.arange(5, 30, 0.1)
#%%
pfit1,_ = optimize.curve_fit(fitting2, detunings, width, p0=[100, 100])
# pfit2,_ = optimize.curve_fit(fitting2, detunings, solpower, p0=[100, 100])
#%%
power22 = [6.552516271316735, 6.838364414753711, 7.113806361443319, 7.430700758131225, 7.7189177063032375]
power44 = [7.429254326854572, 6.925395483159303, 6.696173912947193, 6.454270720928542, 6.325531109734687]
#%%
fig2rep = [26.94429351993138, 26.59987176214942, 26.912697731210105, 26.78805700722674, 26.49339314554072]
fig4rep = [26.591085999820656, 26.920108439764686, 26.82465911437037, 27.212562723166574, 26.85991482720075]
#%%
ratio = dict(width_ratios=[1, 1, 1])
fig, axs = plt.subplots(1, 3, figsize=(18, 5), sharex=False, gridspec_kw=ratio)
fig.subplots_adjust(hspace=0.25, wspace=0.25)

axs[0].plot(data_rawfig2.wave1[crop1fig2], data_rawfig2.power1[crop1fig2], color='royalblue', alpha=1, label='10V')
axs[0].plot(data_rawfig2.wave2[crop2fig2], (data_rawfig2.power2[crop2fig2] - 20), color='darkred', alpha=1, label='9.5V')
axs[0].plot(data_rawfig2.wave3[crop3fig2], (data_rawfig2.power3[crop3fig2] - 40), color='orange', alpha=1, label='9V')
axs[0].plot(data_rawfig2.wave4[crop4fig2], (data_rawfig2.power4[crop4fig2] - 60), color='slateblue', alpha=1, label='8.5V')
axs[0].plot(data_rawfig2.wave5[crop5fig2], (data_rawfig2.power5[crop5fig2] - 80.5), color='seagreen', alpha=1, label='8V')
axs[0].set_xlim(min(data_rawfig2.wave1)+9, max(data_rawfig2.wave1)-4)
axs[0].set_ylim(min(data_rawfig2.power5[crop5fig2])-80, max(data_rawfig2.power1[crop1fig2])+5)
axs[0].set_xlabel('Wavelength (nm)')
axs[0].set_ylabel('Optical power \n(40dBm/div)', labelpad=10)
axs[0].legend(loc=1, frameon=False, fontsize=15)
axs[0].locator_params(axis='y', nbins=4)
axs[0].locator_params(axis='x', nbins=3)
axs[0].get_yaxis().set_ticklabels([])

axs[1].plot(data_rawfig4.wave1[crop1], data_rawfig4.power1[crop1], color='royalblue', alpha=1, label='8V')
axs[1].plot(data_rawfig4.wave2[crop2], (data_rawfig4.power2[crop2] - 20), color='darkred', alpha=1, label='8.5V')
axs[1].plot(data_rawfig4.wave3[crop3], (data_rawfig4.power3[crop3] - 40), color='orange', alpha=1, label='9V')
axs[1].plot(data_rawfig4.wave4[crop4], (data_rawfig4.power4[crop4] - 60), color='slateblue', alpha=1, label='9.5V')
axs[1].plot(data_rawfig4.wave5[crop5], (data_rawfig4.power5[crop5] - 80.5), color='seagreen', alpha=1, label='10V')
axs[1].set_xlim(min(data_rawfig4.wave5)+3, max(data_rawfig4.wave5))
axs[1].set_ylim(min(data_rawfig4.power5[crop5])-79, max(data_rawfig4.power1[crop1])+5)
axs[1].set_xlabel('Wavelength (nm)')
axs[1].set_ylabel('Optical power \n(40dBm/div)', labelpad=10)
axs[1].legend(loc=1, frameon=False, fontsize=15)
axs[1].locator_params(axis='y', nbins=4)
axs[1].locator_params(axis='x', nbins=3)
axs[1].get_yaxis().set_ticklabels([])

axs[2].scatter(volfig2, width2, color='royalblue', s=50, marker='^', label='Vol/down')
axs[2].plot(volfig2, width2, color='royalblue')
axs[2].scatter(volfig4, width4, color='darkred', s=50, label='Vol/up')
axs[2].plot(volfig4, width4, color='darkred')
axs[2].legend(loc='upper left', frameon=False, fontsize=15)
axs[2].set_ylim(min(width2)-20, max(width4)+20)
axs[2].locator_params(axis='y', nbins=6)
axs[2].set_xlabel('Modulation voltage (V)')
axs[2].set_ylabel('FWHM (fs)')

plt.show()
# %%
# power22 = [6.552516271316735, 6.838364414753711, 7.113806361443319, 7.430700758131225, 7.7189177063032375]
# power44 = [7.429254326854572, 6.925395483159303, 6.696173912947193, 6.454270720928542, 6.325531109734687]
# powerfit = power22 + power44
# powerfit.sort()

# # pfit2,_ = optimize.curve_fit(fitting2, detunings, powerfit, p0=[1, 1])

# plt.figure(figsize=(5, 3))
# plt.scatter(detufig2, power22, color='royalblue', s=50, marker='^')
# plt.scatter(detufig4, power44, color='darkred', s=50)
# # plt.plot(range(5, 25, 1), fitting2(range(5, 25, 1), *pfit2), color='seagreen', lw=1)
# plt.xlabel('Effective detuning (MHz)')
# plt.ylabel('Total comb power ($u$W)')

# plt.show()
# %%
detu_width2 = width2[0] - width2[-1] #down
detu_width4 = width4[-1] - width4[0] #up
detu2 = detufig2[-1] - detufig2[0] # detuning changes
detu4 = detufig4[0] - detufig4[-1]

print('detu_witdth2:', detu_width2)
print('detu_witdth4:', detu_width4)
print('detu2:', detu2)
print('detu4:', detu4)
# %%
