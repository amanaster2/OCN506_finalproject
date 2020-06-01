# Washington State River and Climate Data
This repository was created for the final project in OCN 506 at the University of Washington.

**Team Members:** Amanda Manaster (leader), Dylan Vecchione, Amy Larsen

## Purpose
The goal of this project was to create a program that allows a user to see flow discharge, river stage, temperature, and rainfall for a series of locations in Washington state. The data are pulled via API from the [USGS](https://www.usgs.gov/) (flow discharge, river stage) and [NOAA National Centers for Environmental Information (NCEI)](https://www.ncei.noaa.gov/) (temperature, rainfall). These data are then added to a Pandas data frame, plotted for visualization purposes, and saved for later use.

## File Structure
This repository has three main folders: **modules**, **driver**, and **output**.
### modules
This folder contains modules that are called by the script in the **driver** folder. We have four modules:
1. `inputs_func.py` - Functions that asks user for input values to feed to `getClimate_func.py` and `getRivers_func.py`.
2. `getClimate_func.py` - Function to pull climate data from NOAA NCEI. The data are pulled in JSON format and converted to numpy arrays.
3. `getRivers_func.py` - Function to pull river data from USGS. The data are pulled in JSON format and converted to numpy arrays.
4. `dir_func.py` - Function to ensure correct directories and file paths.

### driver
This folder contains one script: `pullData_script.py`. This script calls on the four modules in the **modules** folder, adds pulled data to a Pandas data frame, plots the data, and saves the data as a .pkl file for later use/analysis.

### output
This folder will be used to hold output from pullData_script.py including plots saved as .png files and the data saved as a .pkl file.

## How to Use
To use this program, run `pullData_script.py`. This script will prompt the user for input then will produce the desired data and plots.
