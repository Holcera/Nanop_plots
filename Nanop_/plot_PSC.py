# -*- encoding: utf-8 -*-
'''
@File    :   plot_PSC.py
@Time    :   2023/03/30 20:04:11
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
filepath = r"C:\Users\H\Documents\Lab_BUPT\Data\data10.31-11.4\W20221103_202159.CSV"
data_raw = pd.read_csv(filepath, 
                header=32, 
                na_values='--',
                usecols=[0, 1]
                )
re_col = ['wave1', 'power1']
data_raw.columns = re_col
# data_raw.reset_index(inplace=True)

print('Memory usage:\n' + 
      str(round(data_raw.shape[1]*
                data_raw.memory_usage(index=False).mean()/1e6, 1)) + 'MB')
# print(data_raw.head())
#%%
i = 1
plt.figure(figsize=(12, 6))
plt.plot(data_raw['wave'+str(i)], data_raw['power'+str(i)], color='darkslateblue', lw=2)
plt.ylim(-85, 5)
plt.xlim(min(data_raw['wave'+str(i)]), max(data_raw['wave'+str(i)]))
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (dBm)')
plt.locator_params(axis='y', nbins=3)
plt.locator_params(axis='x', nbins=3)

plt.show()
#%%