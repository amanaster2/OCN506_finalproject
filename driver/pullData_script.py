"""
Purose: This script calls on the four modules in the modules folder, 
adds pulled data to two Pandas data frames, plots the data, 
and saves the data as two .pkl files for later use/analysis.
"""
#===========================================
#Importing the packages
#===========================================

#Import necessary packages
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import sys, os

#Import modules made for this project
sys.path.append(os.path.abspath('modules'))
import input_func as ipt
import getClimate_func as climate
import getRiver_func as river
import dir_func

#===========================================
#Calling the modules
#===========================================

#Create output folders
this_parent, out_dir = dir_func.get_outdir()
dir_func.make_dir(out_dir)

#Call the input function
WCode, RCode, TDelta, rivname = ipt.input_func()

#Define date range
date_start = (datetime.now()-timedelta(TDelta)).strftime("%Y-%m-%d")
date_end = (datetime.now()).strftime("%Y-%m-%d")

#Call getClimate_func and getRiver_func
idnW, precip, p_date, temp, t_date = climate.get_climate([WCode], date_start, date_end)
idnR, depth, d_date, q, q_date, d_q, d_s = river.get_river([RCode],  date_start, date_end)

#Let user know that the data has been gathered
print('\nData Loaded\n')

#===========================================
#Plotting the data 
#===========================================

#Create dataframe for river data
dfriver = pd.DataFrame(index=pd.to_datetime(d_date[0]))
dfriver.index = dfriver.index.tz_convert('US/Pacific')
dfriver.index = dfriver.index.tz_convert(None)
dfriver['height'] = pd.to_numeric(depth[0])
dfriver['h_date'] = pd.to_datetime(d_date[0])
dfriver['flow'] = pd.to_numeric(q[0])
dfriver['f_date'] = pd.to_datetime(q_date[0])

#Set some flags for error handling
t_flag=False
p_flag=False

#Create dataframe for climate data
dfweather =pd.DataFrame(index=pd.to_datetime(p_date[0])) 
if len(precip) != 0:
	dfweather['precip'] = pd.to_numeric(precip[0]) if len(precip[0]) == len(dfweather) else np.empty(len(dfweather))
	p_flag=True
if len(p_date) != 0:
	dfweather['p_date'] = pd.to_datetime(p_date[0]) if len(p_date[0]) == len(dfweather) else np.empty(len(dfweather))
if len(temp) != 0:
	dfweather['temp'] = pd.to_numeric(temp[0]) if len(temp[0]) == len(dfweather) else np.empty(len(dfweather))
	dfweather.temp = dfweather.temp -273.15 #convert to celsius from kelvin
	t_flag=True
if len(t_date) != 0:
	dfweather['t_date'] = pd.to_datetime(t_date[0]) if len(t_date[0]) == len(dfweather) else np.empty(len(dfweather))

plt.close('all')

#Plot the river height 
if len(dfriver.height) > 0 :
	#make plot
	dfriver.plot(y='height') 
	plt.title('River Height at %s' %rivname)
	plt.xlabel('Date', fontsize=14, fontweight='bold') 
	plt.ylabel('River Height (ft)', fontsize=14, fontweight='bold')
	plt.tight_layout()
	plt.savefig(fname = out_dir + 'Height_%s.png' %rivname)
	print('\nToday\'s height:',dfriver.height[len(dfriver.height)-1],'ft')
else:
	print('\nNo river height available')

#Plot river flow 
if len(dfriver.flow) > 0 :
	#make plot 
	dfriver.plot(y='flow')
	plt.title('River Flow at %s' %rivname)
	plt.xlabel('Date', fontsize=14, fontweight='bold') 
	plt.ylabel('River Flow (cfs)', fontsize=14, fontweight='bold')
	plt.tight_layout()
	plt.savefig(fname= out_dir + 'Flow_%s.png' %rivname)
	print('\nToday\'s flow:',dfriver.flow[len(dfriver.flow)-1],'cfs')
else: 
	print('\nNo river flow available')

#Plot precipitation 
if p_flag==True:
	#make plot 
	dfweather.plot.bar(y='precip')
	plt.title('Precipitation at %s' %rivname)
	plt.xticks(rotation=0)
	plt.xlabel('Date', fontsize=14, fontweight='bold') 
	plt.ylabel('Preciitation (mm)', fontsize=14, fontweight='bold')
	plt.tight_layout()
	plt.savefig(fname= out_dir+'Precip_%s.png' %rivname)
	print('\nMost recent precipitation:',dfweather.precip[len(dfweather.precip)-1],'mm')
else:
	print('\nNo precipitation available')

#Plot temperature 
if t_flag==True:
	#make plot 
	dfweather.plot(y='temp') 
	plt.title('Temperature at %s' %rivname)
	plt.xlabel('Date', fontsize=14, fontweight='bold') 
	plt.ylabel('Temperature (C)', fontsize=14, fontweight='bold')
	plt.tight_layout()
	plt.savefig(fname= out_dir+'Temp_%s.png' %rivname)
	print('\nToday\'s maximum temperature:',dfweather.temp[len(dfweather.temp)-1],'C')
else: 
	print('\nNo temperature available')

print('\nDone!')
plt.show() 


#===========================================
#Saving the data as pkl files
#===========================================
out_fn_riv = out_dir + 'dfriver.pkl'
pickle.dump(dfriver, open(out_fn_riv, 'wb'))

out_fn_clim = out_dir +'dfweather.pkl'
pickle.dump(dfweather, open(out_fn_clim, 'wb'))
