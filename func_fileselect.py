# -*- encoding: utf-8 -*-
'''
@File    :   func_fileselect.py
@Time    :   2024/10/16 14:55:49
@Author  :   Wang Heng 
@Version :   1.0
'''
#%% packages
import os
import pickle
import numpy as np
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt

#%% select file func
def select_file():
    """Open a file dialog to select one or more files.

    Returns:
        tuple: Selected file paths or None if no files were selected
    """
    def bring_to_front():
        root.lift()  # Lift the window
        root.attributes('-topmost', True)  # Keep on top
        root.attributes('-topmost', False)  # Allow other windows to go on top again
        root.focus_force()  # Force focus

    # Create and configure root window
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Bring dialog to front after a short delay
    root.after(100, bring_to_front)
    
    # Configure file dialog to allow multiple file selection
    file_paths = filedialog.askopenfilenames(
        title='Select file(s)',
        filetypes=[('CSV files', '*.csv'), ('DAT files', '*.dat')]
    )
    file_paths = file_paths if file_paths else None
    
    # Print results
    if file_paths:
        print("\nSelected files:")
        for path in file_paths:
            print(f"- {path}")
        return file_paths
    else:
        print("No files selected")
        return None

#%% read file func
def read_file(file_path):
    """read csv or dat files with improved CSV handling

    Args:
        file_path (str): file path

    Returns:
        DataFrame: dataframe of the files
        str: file name
    """
    try:
        file_name = os.path.basename(file_path)
        
        if file_path.lower().endswith('.csv'):
            # Try different header configurations for CSV
            try_params = [
                {'header': None},  # No header
                {'header': 0},     # First row as header
                {'header': 32, 'na_values': '--'},  # Header at row 32 (common for some instruments)
                {'skiprows': 32, 'header': 0},  # Skip rows and use first available as header
                {'header': None, 'skiprows': 1}  # No header, skip first row
            ]
            
            for params in try_params:
                try:
                    df = pd.read_csv(file_path, **params)
                    # Verify we have numeric data
                    if df.select_dtypes(include=[np.number]).shape[1] >= 2:
                        # If no column names, assign default names
                        if df.columns.dtype == 'int64':
                            df.columns = [f'Column_{i}' for i in range(len(df.columns))]
                        print(f"Successfully read CSV with parameters: {params}")
                        return df, file_name
                except Exception as e:
                    print(f"Failed to read CSV with parameters {params}: {e}")
                    continue
                    
            # If all standard attempts fail, try with different encodings and separators
            encodings = ['utf-8', 'gbk', 'latin1', 'ISO-8859-1']
            separators = [',', ';', '\t', '|']
            
            for encoding in encodings:
                for separator in separators:
                    try:
                        df = pd.read_csv(file_path, encoding=encoding, sep=separator)
                        if df.select_dtypes(include=[np.number]).shape[1] >= 2:
                            print(f"Read CSV with encoding={encoding}, separator={separator}")
                            return df, file_name
                    except Exception as e:
                        print(f"Failed to read CSV with encoding={encoding}, separator={separator}: {e}")
                        continue
            
            raise ValueError(f"Could not read CSV file: {file_path}")
            
        elif file_path.lower().endswith('.dat'):
            df = pd.read_csv(file_path, delimiter='\s+')
            return df, file_name
        else:
            raise ValueError(f"Unsupported file: {file_path}")
                
    except Exception as e:
        print(f"Error loading file {file_path}: {e}")
        return None, None

#%% plot func
def plot_file(df, file_name):
    """plot the file with improved error handling

    Args:
        df (dataframe): dataframe of the file
        file_name (str): file name
    """
    try:
        # Validate DataFrame
        if df is None or df.empty:
            print("Error: Empty or invalid DataFrame")
            return
            
        plt.figure(figsize=(12, 6))
        
        cols = df.columns.tolist()
        print("\nAvailable columns:")
        for i, col in enumerate(cols):
            print(f"{i}: {col}")
        
        # Automatic column selection for two-column files
        if len(cols) == 2:
            y_cols = [1]  # Select second column automatically
            print(f"\nAutomatically selected column: {cols[1]}")
        else:
            # User selection for files with more than 2 columns
            while True:
                try:
                    y_input = input("\nPlease select the column(s) to plot (separated by commas): ")
                    y_cols = [int(col.strip()) for col in y_input.split(",")]
                    
                    if all(0 <= col < len(cols) for col in y_cols):
                        break
                    else:
                        print(f"Please enter valid column numbers between 0 and {len(cols)-1}")
                except ValueError:
                    print("Please enter valid numbers separated by commas")
        
        x_col = df.iloc[:, 0]  # First column as x-axis
        
        # Plot with error handling for each column
        for y_col in y_cols:
            try:
                y_data = df.iloc[:, y_col]
                if y_data.dtype.kind in 'biufc':  # Check if numeric
                    plt.plot(x_col, y_data, label=f"{cols[y_col]}", lw=1)
                else:
                    print(f"Warning: Column {cols[y_col]} is not numeric, skipping...")
            except Exception as e:
                print(f"Error plotting column {y_col}: {e}")
                continue
        
        plt.xlabel('Wavelength (nm)')
        plt.ylabel('Intensity (dBm)')
        plt.title(file_name)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        
    except Exception as e:
        print(f"Error in plotting: {e}")
        plt.close()  # Clean up any partial plots

#%% main function
def main():
    """Main function to handle file selection and plotting"""
    # Select files using the file dialog
    file_paths = select_file()
    if not file_paths:
        print("No files selected")
        return

    # Process each selected file
    for file_path in file_paths:
        try:
            print(f"\nProcessing file: {file_path}")
            df, file_name = read_file(file_path)
            if df is not None:
                plot_file(df, file_name)
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")
            continue

if __name__ == "__main__": 
    main()
    
#%%