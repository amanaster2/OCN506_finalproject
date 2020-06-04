# Washington State River and Climate Data
This repository was created for the final project in OCN 506 at the University of Washington.

**Team Members:** Amanda Manaster (leader), Dylan Vecchione, Amy Larsen

## Purpose
The goal of this project was to create a program that allows a user to see flow discharge, river stage, temperature, and rainfall for a series of locations in Washington state. We aim to proivde easy access for people who fish in rivers so they can know the curret state of common rivers and see how past weather has impacted the rivers. The data are pulled via API from the [USGS](https://www.usgs.gov/) (flow discharge, river stage) and [NOAA National Centers for Environmental Information (NCEI)](https://www.ncei.noaa.gov/) (temperature, rainfall). These data are then added to a Pandas data frame, plotted for visualization purposes, and saved for later use.

## File Structure
This repository has three main folders: **modules**, **driver**, and **output**.
### modules
This folder contains modules that are called by the script in the **driver** folder. We have four modules:
1. `inputs_func.py` - Functions that asks user for input values to feed to `getClimate_func.py` and `getRivers_func.py`. Input also deals with error handling, and prevents the user from erroring too
	times consecutively.
2. `getClimate_func.py` - Function to pull climate data from NOAA NCEI. The data are pulled in JSON format and converted to numpy arrays.
3. `getRivers_func.py` - Function to pull river data from USGS. The data are pulled in JSON format and converted to numpy arrays.
4. `dir_func.py` - Function to ensure correct directories and file paths.

### driver
This folder contains one script: `pullData_script.py`. This script calls on the four modules in the **modules** folder, adds pulled data to a Pandas data frame, plots the data, and saves the data as a .pkl file for later use/analysis.

### output
This folder will be used to hold output from pullData_script.py including plots saved as .png files and the data saved as a .pkl file.

## How to Use
To use this program, run `pullData_script.py` by navigating to `OCN506_finalproject` and using the command `run driver/pullData_script.py` This script will prompt the user for input then will produce the desired data and plots.

1) Users are prompted (with an in-terminal printout) with the rivers they can pull data from. Each river has a corresponding integer number, which the user inputs into the terminal prompt to make a selection.
	If users input a different data-type (non-integer), or if users input an interger value outside of the given range, they will be prompted to answer within the stated ranges. Users will have 10 attempts
	to complete this step successfully before the program auto-terminates, and the users can re-run the program if desired.
2) If users successfully complete the first step users will see a printed confirmation of the selected river, and they will be prompted to enter another integer number from 1-60, corresponding to the number of days (since "now") of data they would like to download. Again,
	if users input an integer within the printed range, the program will progress to data retrieval. Users have 5 attempts to successfully enter their selection before the process auto-terminates and 
	prompts the user to re-run the program when ready.
3) Once users have successfully entered both specifications, they will see a confirmation that data is being retrieved. They will then see printed confirmation as each day of river and weather data is 
	collected. Once finished, a "data retrieval confirmation" will be displayed in-terminal.
4) Plots will automatically be generated with river and weather data, named and labeled accordingly, for the selected location and time-period, where data is available, and saved to the output folder within the project's output folder 
	(described above). Additionally, the raw dataframes will be saved as a Pickle file (.pkl) to the output folder. River data is saved as "dfriver.pkl" and Weather data is saved as "dfweather.pkl". 
