
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
import requests
import json
from bs4 import BeautifulSoup
!pip install geopy
from geopy.geocoders import Nominatim
import folium
%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
from sklearn.preprocessing import StandardScaler, normalize, scale
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error, r2_score

print('Import Complete')



import os
cwd = os.getcwd()
cwd



print(Geospacial_Coordinates.shape)
col_list = ["NAME", "NAME2"]
df = pd.read_csv("Algeria_centroid_map.csv", usecols=col_list)


col_list = ["NAME", "CENTROID_LATITUDE", "CENTROID_LONGITUDE"]

df = pd.read_csv("Algeria_csv", usecols=col_list)
df. head()



address = 'Missouri, USA'
geolocator = Nominatim(user_agent="ny_explorer")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geograpical coordinate of Missouri, USA are {}, {}.'.format(latitude, longitude))


map_MO = folium.Map(location=[latitude, longitude], zoom_start=7)

# add markers to map
for lat, lng, county in zip(Geo['CENTROID_LATITUDE'], Geo['CENTROID_LONGITUDE'], Geo['NAME']):
    label = '{}'.format(county)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='ORANGE',
        fill=True,
        fill_color='#3186cc',
        fill_opacity=0.7).add_to(map_MO)

map_MO



CLIENT_ID = '20YU4MCI13AFWJYD2DH10DOHAT0MCWFLWKPS4FA52VALZJ5G' # my Foursquare ID
CLIENT_SECRET = 'TWGAMJPEI3ARRMSMGQP3QP1RGGEWV0PYHF2NHSZBK4AK5MZN' # your Foursquare Secret
VERSION = '20180605' # Foursquare API version
radius = 10000
LIMIT = 250

print('Your credentails:')
print('CLIENT_ID: ' + CLIENT_ID)
print('CLIENT_SECRET:' + CLIENT_SECRET)


county_longitude = Geo.loc[11, 'CENTROID_LONGITUDE']
county_name = Geo.loc[11, 'NAME']
print('Latitude and longitude values of {} are {}, {}.'.format(county_name,
                                                               county_latitude,
                                                               county_longitude))




url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}'.format(
    CLIENT_ID,
    CLIENT_SECRET,
    VERSION,
    county_latitude,
    county_longitude,
    radius,
    LIMIT)
url





def get_category_type(row):
    try:
        categories_list = row['categories']
    except:
        categories_list = row['venue.categories']

    if len(categories_list) == 0:
        return None
    else:
        return categories_list[0]['name']




venues = results['response']['groups'][0]['items']
stc = json_normalize(venues) # flatten JSON
filtered_columns = ['venue.name', 'venue.categories', 'venue.location.lat', 'venue.location.lng']
stc = stc.loc[:, filtered_columns]
stc['venue.categories'] = stc.apply(get_category_type, axis=1)
stc.columns = [col.split(".")[-1] for col in stc.columns]
stc.insert(0, 'County', 'St. Charles')
print('{} venues were returned by Foursquare.'.format(df.shape[0]))
stc
