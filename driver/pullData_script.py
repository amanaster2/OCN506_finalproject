
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import sys, os
sys.path.append(os.path.abspath('modules'))
import input_func as ipt
import getClimate_func as climate
import getRiver_func as river

WCode, RCode, TDelta = ipt.input_func()
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
dfriver = dfriver.resample('D').mean()

dfweather =pd.DataFrame(index=pd.to_datetime(p_date[0])) 
#dfweather.index.tz_convert(None)
dfweather['precip'] = pd.to_numeric(precip[0]) #if len(precip[0]) == len(dfweather) else np.empty(len(dfweather))
dfweather['p_date'] = pd.to_datetime(p_date[0]) #if len(p_date[0]) == len(dfweather) else np.empty(len(dfweather))
dfweather['temp'] = pd.to_numeric(temp[0]) if len(temp[0]) == len(dfweather) else np.empty(len(dfweather))
dfweather['t_date'] = pd.to_datetime(t_date[0]) if len(t_date[0]) == len(dfweather) else np.empty(len(dfweather))
dfweather = dfweather.resample('D').mean()

plt.close('all')

#plot the river height 
dfriver.plot(y='height')
dfriver.plot(y='flow')

#Plot first variable
fig, ax = plt.subplots(figsize=(13,5))
dfriver.plot(y='height',ax=ax)
#ax.set_xlabel('Date', fontsize=14, fontweight='bold') #note: only need to set xlabel once
#ax.set_ylabel('Variable 1', fontsize=14, fontweight='bold')
#ax.set_ylim(0,5)
#ax.grid(False)

#Create another y-axis with the same x-axis
ax1 = ax.twinx()

#Plot second variable
<<<<<<< Updated upstream
dfweather.plot(y='precip',ax=ax1, kind='bar')
=======
dfweather.plot.bar(y='precip',ax=ax1)
>>>>>>> Stashed changes
#ax1.set_ylabel('Variable 2', fontsize=14, fontweight='bold')
#ax1.set_ylim(0, 15)
ax1.invert_yaxis() #makes the second y-axis inverted
#ax1.grid(False)
print('\nDone!')
#print('\nTodays flow:' %q[len(q)-1] '\nTodays height:' %depth[len(depth)-1]'\nTodays temperature:'%temp[len(temp)-1]'\nTodays precipitation:'%precip[len(precip)-1])
plt.show() 