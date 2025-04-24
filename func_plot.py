# -*- encoding: utf-8 -*-
'''
@File    :   func_plot.py
@Time    :   2024/10/16 17:38:54
@Author  :   Wang Heng 
@Version :   1.0
'''
#%%
import matplotlib.pyplot as plt
from func_fileselect import select_file
from func_readfiles import read_csv_dats
#%%
def plot_multi(file_paths):
    num_files = len(file_paths)
    
    # 创建一个具有num_files个子图的图形，每个文件一个子图
    fig, axes = plt.subplots(num_files, 1, figsize=(8, 4 * num_files))
    
    if num_files == 1:
        axes = [axes]  # 确保 axes 是列表形式，即使只有一个文件
    
    for i, file_path in enumerate(file_paths):
        print (file_path)
        df = read_csv_dat(file_path)
        
        if df is not None:
            try:
                # 假设每个文件都有两列 'x' 和 'y' 用于绘图
                df.plot(x='x', y='y', kind='line', ax=axes[i], title=f"Data from {os.path.basename(file_path)}")
                axes[i].set_xlabel("X-axis")
                axes[i].set_ylabel("Y-axis")
            except Exception as e:
                print(f"Error plotting data from {file_path}: {e}")
        else:
            print(f"df has not been assigned correctly")

    plt.tight_layout()  # 自动调整子图间距
    plt.show()
    
if __name__ == "__main__":
    file_paths = select_file()
    
    if file_paths:
        plot_multi(file_paths)
#%%