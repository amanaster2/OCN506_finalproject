import requests
import pandas as pd
import json
import numpy as np
from datetime import datetime, timedelta

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
				idn + '&startdate=' + date_start + '&enddate=' + date_end+ '&limit=60', headers={'token':Token})

			#Load API response as JSON
			try:
				d = json.loads(r.text)
			except:
				print('No climate data for this time period\n')
				continue

			#Save list of station IDs for dataframe
			station_id +=[idn]

			#Get dictionary containing all precipitation results
			try:
				prcp_dict = [item for item in d['results'] if item['datatype']=='PRCP']
			except (KeyError):
				print('There is no rainfall data for the time period specified! Moving to next variable.\n')
				continue
			#Get dictionary containing all max temperature results
			try:
				max_temp_dict = [item for item in d['results'] if item['datatype']=='TMAX']
			except (KeyError):
				print('There is no temperature data for the time period specified! Moving to next variable.\n')
				continue

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
# idnW, precip, p_date, temp, t_date,d = get_climate(['GHCND:USW00024220'], (datetime.now()-timedelta(25)).strftime("%Y-%m-%d"), (datetime.now()).strftime("%Y-%m-%d"))
# json = json.dumps(d, indent=4)
# f = open("dict.json","w")
# f.write(json)
# f.close()