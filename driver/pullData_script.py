
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
idnR, depth, d_date, q, q_date, d_s, d_q = river.get_river([RCode],  date_start, date_end)

#plotting the data 
#load arrays into dataframes 
dfriver = pd.DataFrame
dfriver['height'] = 
dfriver['h_date'] = 
dfriver['flow'] = 
dfriver['f_date'] = 

dfweather =pd.DataFrame
dfweather['precip'] = precip 
dfweather['p_date'] = p_date 
dfweather['temp'] = temp 
dfweather['t_date'] = t_date


plt.close('all')

#plot the river height and flow 
dfriver.plot(x='h_date', y='height',y='flow')
