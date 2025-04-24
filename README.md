# Nanop_plots

This repository contains Python scripts and utilities for data analysis and visualization related to Nanop_ paper. The scripts are organized to handle tasks such as file selection, data processing, peak detection, fitting, and plotting.

Includes a lot of unrelated drawing scripts.

### Main Scripts

- **`func_fileselect.py`**: Provides functions for selecting and reading files using a graphical file dialog.
- **`func_fpeaks.py`**: Implements peak detection functionality for experimental data.
- **`func_plot.py`**: Contains utilities for plotting multiple datasets in a single figure.
- **`func_readfiles.py`**: Handles reading and merging of `.csv` and `.dat` files into pandas DataFrames.
- **`func_sech2fit.py`**: Includes functions for detecting peaks and fitting them with a hyperbolic secant squared (`sech²`) function.
- **`func_spanselect.py`**: Provides interactive span selection for data visualization.
- **`plot_OSA_all.py`**: Script for plotting optical spectrum analyzer (OSA) data.
- **`Plot_OSC_all.py`**: Script for plotting oscilloscope data.

### Subdirectory: `Nanop_/`

This folder contains specialized scripts for various nanoparticle-related experiments:

- **`disper_cut.py`**: Processes and trims dispersion data.
- **`disper_plot1.py`**: Visualizes dispersion data with fitting.
- **`fig3_group_8th.py`**: Generates grouped plots for specific experimental datasets.
- **`plot_2trans.py`**: Plots transmission data from two channels.
- **`plot_3kerrcomb.py`**: Visualizes Kerr comb data across multiple datasets.
- **`plot_coupling_position.py`**: Analyzes and plots coupling position data.
- **`plot_PSC.py`**: Plots power spectral density data.
- **`plot_ringing.py`**: Visualizes ringing effects in experimental data.
- **`soliton_sech2fit.py`**: Fits soliton data using a `sech²` function.
- **`trans.py`**: Processes and visualizes transmission data.

## Requirements

The scripts rely on the following Python libraries:
- `numpy`
- `pandas`
- `matplotlib`
- `scipy`
- `tkinter`
- `holoviews`
- `bokeh`

## Usage

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Nanop_plots