import pandas as pd
import numpy as np


def clean_shape(value):
  return str(value)

def clean_lat(value):
  return float(value)

def clean_time2(value):
  if value[-5:-3]=="24":
    value = value[:-5]+"00"+value[-3:]
  return value

df = pd.read_csv("data/scrubbed.csv")

df.iloc[43782,9]=33.200088

df["latitude"]=df["latitude"].apply(clean_lat)
df["shape"] = df["shape"].apply(clean_shape)

df["shape"].fillna("other")

df["Time_clean"] = df["datetime"].apply(clean_time2)
df["Time_clean"]=pd.to_datetime(df["Time_clean"])

df["Year"] = df["Time_clean"].dt.year
df["Hour"] = df["Time_clean"].dt.hour
df["Month"] = df["Time_clean"].dt.month
df["Quarter"] = df["Time_clean"].dt.quarter

df_cleaned = df[["Time_clean","city","state","country","shape","duration (seconds)","latitude","longitude ","Year","Hour","Month","Quarter"]]
df_cleaned.sort_values("Time_clean",inplace=True)
df_cleaned = df_cleaned.reset_index(drop=True)
df_cleaned.to_csv("data/Cleaned.csv",index=None)



temp = df_cleaned.groupby(["Year","shape"]).count()["Time_clean"].reset_index()
temp_ = [temp["Year"].values,temp["shape"].values]
temp2 = pd.Series(temp["Time_clean"].values, index=temp_)

shapes = df_cleaned["shape"].unique()
shape_zero = np.zeros(shapes.size)
shape_dict_zero = dict(zip(shapes,shape_zero))
Years = df_cleaned["Year"].unique()

dic = {}
for i,j in zip(temp["Year"].values,temp["shape"].values):
  if i in dic.keys():
      dic[i][j]+=temp2[(i,j)]
  else:
    if i == 1906:
      dic[i] = shape_dict_zero.copy()
      dic[i][j]+=temp2[(i,j)]
      year = i
    else:
      dic[i] = dic[year].copy()
      dic[i][j]+=temp2[(i,j)]
      year = i

temp3 = []
for key,value in dic.items():
  temp3.append(list(value.values()))
temp3 = np.array(temp3)
temp3 = pd.DataFrame(temp3,columns=[list(dic[1906].keys())])
temp3["Year"] = list(dic.keys())
Shape_ = temp3




Shape_.to_csv("data/ShapesByYear.csv",index=None)
