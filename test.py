import requests
import pandas as pd
import json
import numpy as np
from datetime import datetime

Token = 'sFnzvgMvjWEXBVsssompToJFuwsVrEGt'

r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid=PRCP&stationid=GHCND:USC00452505&startdate=2020-05-01&enddate=2020-05-15', headers={'token':Token})
d = json.loads(r.text)

# #initialize lists to store data
# dates_temp = []
# dates_prcp = []
# temps = []
# prcp = []

# #for each year from 2015-2019 ...
# for year in range(2015, 2020):
#     year = str(year)
#     print('working on year '+year)
    
#     #make the api call
#     r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=LCD', headers={'token':Token})
#     #load the api response as a json
#     d = json.loads(r.text)
#     #get all items in the response which are average temperature readings
#     avg_temps = [item for item in d['results'] if item['datatype']=='TAVG']
#     #get the date field from all average temperature readings
#     dates_temp += [item['date'] for item in avg_temps]
#     #get the actual average temperature from all average temperature readings
#     temps += [item['value'] for item in avg_temps]