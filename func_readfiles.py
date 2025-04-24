# -*- encoding: utf-8 -*-
'''
@File    :   func_readfiles.py
@Time    :   2024/10/16 16:16:25
@Author  :   Heeeg 
@Version :   1.0
'''
#%%
import os
import pandas as pd
from func_fileselect import select_file
#%%
def read_csv_dats(file_paths):
    """load csv or dat files to dataframe

    Args:
        file_paths (str): file path

    Returns:
        dataframe
    """
    dfs = pd.DataFrame()
    
    for file_path in file_paths:
        file_ext = os.path.splitext(file_path)[1].lower()
    
        try:
            if file_ext == ".csv":
                df = pd.read_csv(file_path)
            elif file_ext == ".dat": 
                df = pd.read_csv(file_path, sep='\s+')
            else:
                print(f"Unsupported file format: {file_ext}") #skip other file format
                continue
        
            print(f"The file was read successfully: {file_path}")
            print(df.head())
            dfs = pd.concat([dfs, df], ignore_index=True, axis=1) #merge dataframe along the axis=1
            
        except Exception as e:
            print(f"Error loading file {file_path}: {e}")
    print(dfs)        
    return dfs

# def read_csv_dat(file_paths):
#     for file_path in file_paths:
#         file_ext = os.path.splitext(file_path)[1].lower()
    
#         try:
#             if file_ext == ".csv":
#                 df = pd.read_csv(file_path)
#             elif file_ext == ".dat":
#                 df = pd.read_csv(file_path, sep='\s+')
#             else:
#                 print(f"Unsupported file format: {file_ext}")
#                 return None
        
#             print(f"The file was read successfully: {file_path}")
#             print(df.head())
#             return df
            
#         except Exception as e:
#             print(f"Error loading file {file_path}: {e}")
#             return None
            

if __name__ == "__main__":
    file_paths = select_file()
    
    if file_paths:
        read_csv_dats(file_paths)

#%%    