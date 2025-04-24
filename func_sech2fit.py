# -*- encoding: utf-8 -*-
'''
@File    :   func_sech2.py
@Time    :   2025/01/25 22:50:13
@Author  :   Wang Heng 
@Version :   1.0
'''
#%%
import numpy as np
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from func_fileselect import select_file, read_file
from matplotlib import rcParams

#%%
rcParams['font.family'] = 'Times New Roman'
rcParams['font.size'] = 20
#%%
def find_data_peaks(x, y, threshold=-62, distance=20):
    """Find peaks above threshold
    
    Args:
        x (array): x data
        y (array): y data
        threshold (float): Minimum peak height (default: -60)
        distance (int): Minimum distance between peaks
    
    Returns:
        tuple: (peak_positions, peak_properties)
    """
    peaks, properties = find_peaks(y, 
                                 height=threshold,  # Set minimum height
                                 distance=distance,
                                 prominence=1)  # Reduced prominence requirement
    return peaks, properties

def sech2_func(x, A0, A, x0, width):
    """Hyperbolic secant squared function
    
    Args:
        x (array): x values
        A0 (float): Background level
        A (float): Amplitude
        x0 (float): Center position
        width (float): Width parameter
    
    Returns:
        array: sech² values
    """
    return A0 + A * (1 / np.cosh((x - x0) / width))**2

def fit_peaks_sech2(x, y, peaks):
    """Fit a sech² function to the detected peaks
    
    Args:
        x (array): x data
        y (array): y data
        peaks (array): Indices of detected peaks
    
    Returns:
        tuple: Fit parameters and covariance matrix
    """
    # Extract peak data
    x_peaks = x[peaks]
    y_peaks = y[peaks]
    
    # Initial parameter guesses
    A0_es = np.min(y_peaks)
    A_es = np.max(y_peaks) - A0_es
    x0_es = x_peaks[np.argmax(y_peaks)]
    width_es = (x_peaks[-1] - x_peaks[0]) / 10  # Rough estimate of width
    
    p0 = [A0_es, A_es, x0_es, width_es]
    
    try:
        popt, pcov = curve_fit(sech2_func, x_peaks, y_peaks, p0=p0)
        return popt, pcov
    except Exception as e:
        print(f"Fitting failed: {e}")
        return None, None

def main():
    # Select and read data file
    file_paths = select_file()
    if not file_paths:
        return
    
    df, file_name = read_file(file_paths[0])  # Use first selected file
    if df is None:
        return
        
    # Get x and y data
    x = df.iloc[:, 0].values
    cols = df.columns.tolist()
    print("\nAvailable columns:")
    for i, col in enumerate(cols):
        print(f"{i}: {col}")
    
    if len(cols) == 2:
        y_col = 1
        print(f"Automatically selected column: {cols[y_col]}")
    else:
        while True:
            try:
                y_col = int(input("\nSelect column to analyze: "))
                if 0 <= y_col < len(cols):
                    break
                print(f"Please enter a valid column number (0-{len(cols)-1})")
            except ValueError:
                print("Please enter a valid number")
    
    y = df.iloc[:, y_col].values
    
    # Find peaks above threshold
    peaks, properties = find_data_peaks(x, y, threshold=-62)
    
    if len(peaks) == 0:
        print("No peaks found above threshold")
        return
        
    # Filter peaks above x threshold
    valid_peaks = peaks[x[peaks] >= 1625]
    if len(valid_peaks) == 0:
        print("No valid peaks above x threshold")
        return
    
    print(f"\nFound {len(valid_peaks)} peaks above -60 and x ≥ 1625:")
    for i, peak_idx in enumerate(valid_peaks):
        print(f"Peak {i+1}: x={x[peak_idx]:.2f}, y={y[peak_idx]:.2f}")
    
    # Fit sech² function to the detected peaks
    popt, pcov = fit_peaks_sech2(x, y, valid_peaks)
    
    if popt is None:
        print("Fitting failed")
        return
    
    # Plot results
    plt.figure(figsize=(9, 5), dpi=150)
    plt.plot(x, y, 'b-', label='Exp.')
    plt.ylim(-65, 10)
    plt.xlim(1530, 1700)
    # plt.plot(x[valid_peaks], y[valid_peaks], 'ro', label='Detected Peaks')
    
    # Plot fit
    x_fit = np.linspace(x[valid_peaks].min()-5, x[valid_peaks].max()+5, 1000)
    y_fit = sech2_func(x_fit, *popt)
    plt.plot(x_fit, y_fit, 'r', lw=2, label='Sech² Fit')
    
    # plt.axhline(y=-65, color='r', linestyle=':', label='y threshold (-60)')
    # plt.axvline(x=1625, color='orange', linestyle=':', label='x threshold (1625)')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Intensity (dBm)')
    # plt.title(f'{file_name}')
    plt.legend()
    # plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
#%%