
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import sys, os
sys.path.append(os.path.abspath('modules'))
import input_func as ipt
import getClimate_func as climate
import getRiver_func as river

WCode, RCode, TDelta, rivname = ipt.input_func()
date_start = (datetime.now()-timedelta(TDelta)).strftime("%Y-%m-%d")
date_end = (datetime.now()).strftime("%Y-%m-%d")

idnW, precip, p_date, temp, t_date = climate.get_climate([WCode], date_start, date_end)
idnR, depth, d_date, q, q_date, d_q, d_s = river.get_river([RCode],  date_start, date_end)
print('\nData Loaded\n')
#plotting the data 
#load arrays into dataframes 
dfriver = pd.DataFrame(index=pd.to_datetime(d_date[0]))
dfriver.index = dfriver.index.tz_convert('US/Pacific')
dfriver.index = dfriver.index.tz_convert(None)
dfriver['height'] = pd.to_numeric(depth[0])
dfriver['h_date'] = pd.to_datetime(d_date[0])
dfriver['flow'] = pd.to_numeric(q[0])
dfriver['f_date'] = pd.to_datetime(q_date[0])
#dfriver = dfriver.resample('D').mean()

dfweather =pd.DataFrame(index=pd.to_datetime(p_date[0])) 
#dfweather.index.tz_convert(None)
dfweather['precip'] = pd.to_numeric(precip[0]) if len(precip[0]) == len(dfweather) else np.empty(len(dfweather))
dfweather['p_date'] = pd.to_datetime(p_date[0]) if len(p_date[0]) == len(dfweather) else np.empty(len(dfweather))
dfweather['temp'] = pd.to_numeric(temp[0]) if len(temp[0]) == len(dfweather) else np.empty(len(dfweather))
dfweather.temp = dfweather.temp -273.15 #convert to celsius from kelvin
dfweather['t_date'] = pd.to_datetime(t_date[0]) if len(t_date[0]) == len(dfweather) else np.empty(len(dfweather))
#dfweather = dfweather.resample('D').mean()

plt.close('all')

#plot the river height 
if len(dfriver.height) > 0 :
	#make plot
	dfriver.plot(y='height') 
	plt.title('River Height at', rivname)
	plt.xlabel('Date', fontsize=14, fontweight='bold') 
	plt.ylabel('River Height (ft)', fontsize=14, fontweight='bold')
	#plt.savefig('Height')
	print('\nTodays height:',dfriver.height[len(dfriver.height)-1],'ft')
else:
	print('No river height available')
	

#plot river flow 
if len(dfriver.flow) > 0 :
	#make plot 
	dfriver.plot(y='flow')
	plt.xlabel('Date', fontsize=14, fontweight='bold') 
	plt.ylabel('River Flow (cfs)', fontsize=14, fontweight='bold')
	print('\nTodays flow:',dfriver.flow[len(dfriver.flow)-1],'cfs')
else: 
	print('No river flow available')
	

#plot precipitation 
if len(dfweather.precip) > 0 :
	#make plot 
	dfweather.plot(y='precip')
	plt.xlabel('Date', fontsize=14, fontweight='bold') 
	plt.ylabel('Preciitation (mm)', fontsize=14, fontweight='bold')
	print('\nTodays precipitation:',dfweather.precip[len(dfweather.precip)-1],'mm')
else:
	print('No precipitation available')
	  

#plot temperature 
if len(dfweather.temp) > 0 :
	#make plot 
	dfweather.plot(y='temp') 
	plt.xlabel('Date', fontsize=14, fontweight='bold') 
	plt.ylabel('Temperature (C)', fontsize=14, fontweight='bold')
	print('\nTodays maximum temperature:',dfweather.temp[len(dfweather.temp)-1],'C')
else: 
	print('No temperature available')
	  




#Plot first variable
#fig, ax = plt.subplots(figsize=(13,5))
#dfriver.plot(y='height',ax=ax)
#ax.set_xlabel('Date', fontsize=14, fontweight='bold') #note: only need to set xlabel once
#ax.set_ylabel('Variable 1', fontsize=14, fontweight='bold')
#ax.set_ylim(0,5)
#ax.grid(False)

#Create another y-axis with the same x-axis
#ax1 = ax.twinx()

#Plot second variable
#dfweather.plot(y='precip',ax=ax1, kind='bar')
#dfweather.plot.bar(y='precip',ax=ax1)
#ax1.set_ylabel('Variable 2', fontsize=14, fontweight='bold')
#ax1.set_ylim(0, 15)
#ax1.invert_yaxis() #makes the second y-axis inverted
#ax1.grid(False)
print('\nDone!')
plt.show() 
