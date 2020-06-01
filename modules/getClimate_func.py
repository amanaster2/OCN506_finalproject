import requests
import pandas as pd
import json
import numpy as np
from datetime import datetime

Token = 'sFnzvgMvjWEXBVsssompToJFuwsVrEGt'

def get_climate(station, date_start, date_end):
	#Initialize lists to store data
	station_id=[]
	prcp_dict = []
	max_temp_dict = []
	prcp = []
	dates_prcp = []
	max_temp=[]
	dates_temp = []

	#Loop through list of station IDs
	for idn in station:
		#Loop through date range
		for date in pd.date_range(date_start, date_end):
			sta = str(idn)
			date = str(date)
			print('Working on '+sta+' for '+date) #Print some information for user

			#Call API
			r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid=PRCP,TMAX&stationid=' +
				idn + '&startdate=' + date_start + '&enddate=' + date_end, headers={'token':Token})

			#Load API response as JSON
			d = json.loads(r.text)

			#Save list of station IDs for dataframe
			station_id +=[idn]

			#Get dictionary containing all precipitation results
			prcp_dict = [item for item in d['results'] if item['datatype']=='PRCP']
			#Get dictionary containing all max temperature results
			max_temp_dict = [item for item in d['results'] if item['datatype']=='TMAX']

		#Get precipitation values
		prcp.append([item['value'] for item in prcp_dict])
		#Get date corresponding to precipiation values
		dates_prcp.append([item['date'] for item in prcp_dict])
		#Get max temperature values
		max_temp.append([item['value'] for item in max_temp_dict])
		#Get date corresponding to max temperature values
		dates_temp.append([item['date'] for item in max_temp_dict])

	return(station_id, prcp, dates_prcp, max_temp, dates_temp)


#Example function call for two sites
idn, precip, p_date, temp, t_date = get_climate(['GHCND:USW00024220','GHCND:USC00458034'], '2020-05-01', '2020-05-10')