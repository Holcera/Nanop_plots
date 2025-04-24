# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 14:33:20 2022

@author: Wang Heng
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
# import pyLPD.MLtools as mlt
from matplotlib import rcParams
from matplotlib.ticker import ScalarFormatter

# pd.options.plotting.backend = 'holoviews'
#%%
# %matplotlib ipympl
rcParams['font.family'] = 'Times New Roman'
rcParams['font.size'] = 20

#%%
def read_csv_all(folder_path, ext):
      global data_raw
      data_raw = pd.DataFrame()
      for i in range(len(files)):
            file = folder_path + '\\' + files[i]
            row, cols = get_skip_row(file, ext)
            if ext.lower() == '.dat':
                  data = pd.read_csv(file, 
                                    skiprows=row,
                                    sep='\t',  #dat file
                                    na_values='--',
                                    usecols=range(cols)
                                    )
                  data.columns = ['wave'+str(i), 'power'+str(i)]
                  data_raw = pd.concat([data_raw, data], axis=1)
            
            elif ext.lower() == '.csv':
                  data = pd.read_csv(file, 
                                    skiprows=row, 
                                    na_values='--',
                                    usecols=range(cols)
                                    )
                  data.columns = ['wave'+str(i), 'power'+str(i)]
                  data_raw = pd.concat([data_raw, data], axis=1)
      
      print('Memory usage:\n' + 
      str(round(data_raw.shape[1]*
                data_raw.memory_usage(index=False).mean()/1e6, 1)) + 'MB')
      # print(data_raw.head())
      return data_raw

def read_csv(file_path, ext):
      global data_raw
      row, cols = get_skip_row(file_path, ext)

      if ext.lower() == '.dat':
            data_raw = pd.read_csv(file_path, 
                                    skiprows=None,
                                    sep='\t', #dat file
                                    na_values='--',
                                    usecols=range(cols)
                                    )
            data_raw.columns = ['wave0', 'power0']
      
      elif ext.lower() == '.csv':
            data_raw = pd.read_csv(file_path, 
                                    skiprows=row, #get digit row_num
                                    na_values='--',
                                    usecols=range(cols)
                                    )
            data_raw.columns = ['wave0', 'power0']
            
      return data_raw

def get_skip_row(file_path, ext):
      with open(file_path, 'r') as f:
            for row, line in enumerate(f):
                  if ext.lower() == '.csv':
                        vals = line.strip().split(',')
                  elif ext.lower() == '.dat':
                        vals = line.strip().split('\t')
                  
                  cols = len(vals)      
                  if cols < 2:
                        continue
                  if all(value.replace('.', '').replace('-', '').isdigit() for value in vals): #if all cols is digit
                        return row, cols
      return None

def plot_csv():
      num_col = len(data_raw.columns)
      for i in range(0, num_col, 2):
            x = data_raw.iloc[:, i]
            y = data_raw.iloc[:, i+1]
            fname = files[int(i/2)]
            
            plt.figure(figsize=(10, 5))
            plt.plot(x, y, color='slateblue', lw=1)
            # plt.bar(x, y, color='royalblue', width=0.3, lw='0.1', label='power')
            # plt.scatter(x, y, color='royalblue', s=10)
            plt.ylim(-80, 5)
            plt.xlim(min(x), max(x))
            plt.xlabel('Wavelength (nm)')
            plt.ylabel('Intensity (dBm)')
            plt.title(fname)
            # plt.locator_params(axis='y', nbins=4)
            # plt.locator_params(axis='x', nbins=3)

            plt.gca().xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
            plt.show()
            
def main():
      global files
      files = []
      
      inputpath = input('Files address:')
      if inputpath.startswith('"') and inputpath.endswith('"'):
            inputpath = inputpath[1:-1]
      
      if os.path.isfile(inputpath):
            if inputpath.lower().endswith('.csv') or inputpath.lower().endswith('.dat'):
                  name, ext = os.path.splitext(inputpath)
                  files.append(os.path.basename(inputpath)) #extract file name
                  read_csv(inputpath, ext)
                  plot_csv()
      
      elif os.path.isdir(inputpath):
            for i in os.listdir(inputpath):
                  name, ext = os.path.splitext(i)
                  if ext.lower() == '.dat' or '.csv': 
                        files.append(i)
            
            read_csv_all(inputpath, ext)
            plot_csv()


            
if __name__ == "__main__":
      main()
      

#%%