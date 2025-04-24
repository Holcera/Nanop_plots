# -*- encoding: utf-8 -*-
'''
@File    :   findpeaks.py
@Time    :   2024/03/28 22:10:27
@Author  :   Wang Heng 
@Version :   1.0
'''
#%%
import pandas as pd
import matplotlib.pyplot as plt
import pyLPD.MLtools as pmlt
from matplotlib.widgets import SpanSelector
from read_csv_all import read_csv
from matplotlib.ticker import ScalarFormatter
#%%
filepath = r"C:\Users\H\OneDrive\KEIO\Wang\brillouin\yos03171842(35).dat"
data_raw = read_csv(filepath)
for i in range(len(data_raw.columns)):
    data_raw.rename(columns={data_raw.columns[i]: f"ch{i}"}, inplace=True)

#%%
idx_max, maxtab, idx_min, mintab = pmlt.peakdet(data_raw.ch1.values, delta=20)

idx_max1 = []
maxtab1 = []
for i in range(0, len(maxtab)):
      if maxtab[i] >= -40:
            idx_max1.append(idx_max[i])
            maxtab1.append(maxtab[i])

x = data_raw.ch0
y = data_raw.ch1
plt.figure(figsize=(10, 5))
plt.plot(x, y, color='slateblue', lw=1)
plt.scatter(x[idx_max1], maxtab1, color='red', s=10)
plt.ylim(-80, 5)
plt.xlim(-0.6+1550, max(x))
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (dBm)')
plt.gca().xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
plt.show()
#%%
print(x.iloc[idx_max1])
# %%
