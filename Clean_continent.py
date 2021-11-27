import pandas as pd
import numpy as np


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

df = pd.read_csv("data/Cleaned.csv")

df["Continent"]=df.apply(lambda row: get_continent(row["latitude"],row["longitude "]),axis=1)

df.to_csv("data/Cleaned_with_continent.csv")