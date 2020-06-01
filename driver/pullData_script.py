
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