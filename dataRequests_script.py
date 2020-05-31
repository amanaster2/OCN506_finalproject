import requests
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET
import pandas as pd
import bs4
import matplotlib.pyplot as plt

# set query parameters
name = 'yakima'
usgs_code = 12484500 
t0 = datetime.now() - timedelta(days=7)
t1 = datetime.now() + timedelta(days=1)
# This gets USGS data for a past time period specfied by t0 to t1
time_str = ('&startDT=' + t0.strftime('%Y-%m-%d')
    +'&endDT=' + t1.strftime('%Y-%m-%d'))
# Form the url.
url_str = ('http://waterservices.usgs.gov/nwis/iv/'
    + '?format=waterml,1.1&sites=' + str(usgs_code)
    + time_str + '&parameterCd=00060')

# here is the resulting url_str
"""
http://waterservices.usgs.gov/nwis/dv/?format=waterml,1.1&sites=12200500&startDT=2020-05-01&endDT=2020-05-10&parameterCd=00060
"""
# Get the XML to parse:
if True:
    # use this to get it from the web
    response = requests.get(url_str)
    root = ET.fromstring(response.content)
else:
    # use this to read it from the saved file
    e0 = ET.parse('./waterservices.usgs.gov.xml')
    root = e0.getroot()

"""    
Extract the data from the XML.

...not a pleasant operation...

The "root" is the starting branch of the tree of "elements", kind of like
a hierarchy of folders and subfolders.

We will take the approach of going through each element and seeing if it
is one that holds data.  Those elements look like:
    
<ns1:value qualifiers="P" dateTime="2020-05-01T00:00:00.000">20100</ns1:value>
    
If this element was called "e" then:
    e.tag = ns1:value
    e.attrib is a python dict with keys "qualifiers" and "dateTime"
    e.text = 20100 is the data value at this time
    
One issue is that the "ns1:" is an example of an XML "prefix" which is commonly used
to make sure that each element is unique, even if it came from a different context.
This is good coding practice, but it makes our job harder, because the value of "ns1"
is actually set in the first element of the XML:
    
<ns1:timeSeriesResponse xmlns:ns1="http://www.cuahsi.org/waterML/1.1/"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.cuahsi.org/waterML/1.1/
    http://waterservices.usgs.gov/WaterML-1.1.xsd">

where "xmlns" is a special XML property that stands for XML Namespace, and you can see here
that they define ns1="http://www.cuahsi.org/waterML/1.1/".
    
The results is that when I get the tag of the first element using "root.tag", even
though I am expecting "ns1:timeSeriesResponse" (the first item in the element above)
what actually happens is that root.tag returns the string:
    
{http://www.cuahsi.org/waterML/1.1/}timeSeriesResponse
    
from this you can tell that what happend is that the "ns1:" in each element tag
gets replaced by "{http://www.cuahsi.org/waterML/1.1/}"
and you HAVE to refer to tags using this string when searching for specific ones.
    
In the code below:
"aa" is '{http://www.cuahsi.org/waterML/1.1/}'

"""
    
# get the root tag
rt = root.tag
# find the part of the tag in {}
aa = rt[rt.find('{'): rt.find('}') + 1]

# initialize lists to hold data
Q = [] # flow
T = [] # time

# loop over ALL elements in the tree
for e in root.findall(".//"):
    # NOTE: "." stands for the current element, and "//" stands for all subelements under "."
    # see: https://docs.python.org/3/library/xml.etree.elementtree.html#supported-xpath-syntax
    
    if True:
        # if you make this section True it prints out the parts of each element
        # to the screen, a helpful tool sometimes
        print('\ntag = ' + e.tag)
        atr = e.attrib
        if len(atr) > 0:
            for a in atr.keys():
                print(' - attrib = ' + a + ' : ' + atr[a])
        print(' -- text = ' + str(e.text))
    
    # get a data value and associated time
    if e.tag == aa+'value':
        Q.append(float(e.text))
        T.append(pd.to_datetime(e.get('dateTime'))) # pandas handles times well
        
    # get the units
    if e.tag == aa+'unitCode':
        flow_units = e.text
    
# put the results in a DataFrame
qt_df = pd.DataFrame(Q, index=T, columns=['Flow (' + flow_units + ')'])
qt_df.index.name = 'Date'
print(qt_df)

"""
A final comment: since all XML files are different you have to look at them in a
browser or by parsing to the screen first in order to find the right ways to get
what you are looking for.
"""

# EXAMPLE 1: NDBC buoy data - historical for one year

# Resources
# https://www.ndbc.noaa.gov/
# https://www.ndbc.noaa.gov/download_data.php?filename=46029h2018.txt.gz&dir=data/historical/stdmet/

# station and year
ncei_sn = 24220 # Ellensburg
ncei_year = 2018

# get the data as a text file 
try:
    # form the url string for the request
    idn = str(ncei_sn) + 'h' + str(ncei_year)
    wunderground_url = ('https://www.wunderground.com/history/daily/KYKM/date/2020-5-29')
           
    # get the request and do some parsing
    page = requests.get(wunderground_url)
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    table = soup.find(id='inner-wrap')
    obs = table.find_all(class_="small-12 columns has-sidebar")

    # some munging required
    sns = str(sn_text)[2:-2] # get rid of [' at start and '] at end
    sns = sns.replace('\\n','\n') # replace odd line feeds with real ones

    # write data to a text file
    ndbc_fn = out_dir + 'ndbc_' + idn + '.txt'
    f = open(ndbc_fn,'w')
    f.write(sns)
    f.close()

    print(' Retrieved ' + idn)
except:
    print(' -- Failed ' + idn)
    pass

# parse the text file into a pandas DataFrame
ndbc_df = pd.read_csv(ndbc_fn, delim_whitespace=True, index_col='date',
         skiprows=[1],
         parse_dates={'date':[0, 1, 2, 3, 4]}, # the columns containing time info
         date_parser=lambda x: datetime.strptime(x, '%Y %m %d %H %M'))

# plot one column
ndbc_df[['WSPD']].plot()
