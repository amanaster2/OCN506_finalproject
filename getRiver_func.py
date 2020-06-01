import requests
import pandas as pd
import json
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

def get_river(station, date_start, date_end):
	#Initialize lists to store data
	station_id=[]
	stage = []
	q=[]
	dates_stage=[]
	dates_q=[]

	#Loop through list of station IDs
	for idn in station:
		#Loop through date range
		for date in pd.date_range(date_start, date_end):
			sta = str(idn)
			date = str(date)
			print('Working on '+sta+' for '+date) #Print some information for user

			#Call API
			stage_req = requests.get('https://waterservices.usgs.gov/nwis/iv/?format=json&indent=on&sites='
				+idn+'&startDT='+date_start+'&endDT='+date_end+'&parameterCd=00065')
			q_req = requests.get('https://waterservices.usgs.gov/nwis/iv/?format=json&indent=on&sites='
				+idn+'&startDT='+date_start+'&endDT='+date_end+'&parameterCd=00060')

			#Load API response as JSON
			d_stage = json.loads(stage_req.text)
			d_q = json.loads(q_req.text)

			#Save list of station IDs for dataframe
			station_id +=[idn]

			#Get dictionary containing all stage data
			stage_dict = d_stage['value']['timeSeries'][0]['values'][0]['value']
			#Get dictionary containing all flow data
			q_dict = d_q['value']['timeSeries'][0]['values'][0]['value']

		#Get stage values
		stage.append([item['value'] for item in stage_dict])
		#Get date corresponding to stage values
		dates_stage.append([item['dateTime'] for item in stage_dict])
		#Get flow values
		q.append([item['value'] for item in q_dict])
		#Get date corresponding to flow values
		dates_q.append([item['dateTime'] for item in q_dict])

	return(station_id, stage, dates_stage, q, dates_q, d_stage, d_q)

#Example function call for one site
idn, depth, d_date, q, q_date, d_s, d_q = get_river(['12484500'], '2020-05-27', '2020-05-31')

plt.figure(1)
plt.plot(q_date[0], q[0])
plt.show()

plt.figure(2)
plt.plot(d_date[0], depth[0])
plt.show()