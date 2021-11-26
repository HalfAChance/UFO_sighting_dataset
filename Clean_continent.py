from geopy.geocoders import Nominatim
import pycountry_convert as pc
import pandas as pd
import numpy as np

def country_to_continent(country_name):
    #country_alpha2 = pc.country_name_to_country_alpha2(country_name)
    if country_name =="other":
      return "other"
    country_continent_code = pc.country_alpha2_to_continent_code(country_name)
    country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
    return country_continent_name

def get_continent(lat,lon):
  lat = float(lat)
  lon = float(lon)
  if (lat>1.17 and lat<77.43) and (lon>26.03 or lon<-169.4):
    return "Asia"
  elif (lat>36 and lat<71.08) and (lon>-9.31 and lon<66.1):
    return "Europe"
  elif (lat>-34.51 and lat<37.21) and (lon>17.33 and lon<51.24):
    return "Africa"
  elif (lat>7.12 and lat<71.59) and (lon>-168.05 and lon<-55.24):
    return "North America"
  elif (lat>-53.54 and lat<12.28) and (lon>-81.2 and lon<34.46):
    return "South America"
  elif (lat>-47 and lat<30) and (lon>110 or lon <-130):
    return "Oceania"
  elif lat<-62:
    return "Antarctica"
  else:
    return "Other"

geolocator = Nominatim(user_agent="geoapiExercises")

def get_country_name(lat,lon):
  lat = str(lat)
  lon = str(lon)
  location = geolocator.reverse(lat+","+lon)
  try:
    add = location.raw['address']
    res = add.get('country_code')
  except:
    print("other")
    return "other"
  else:
    print(res)
    return res

df = pd.read_csv("data/Cleaned.csv")

df["Continent"]=df.apply(lambda row: get_continent(row["latitude"],row["longitude "]),axis=1)

df.to_csv("data/Cleaned_with_continent.csv")