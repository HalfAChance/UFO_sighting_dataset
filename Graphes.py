import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

def define_period(value):
  if value<=1938:
    return "Before Golden Age"
  elif value>1938 and value<=1970:
    return "Golden Age"
  elif value>1970 and value<=1996:
    return "New Wave"
  else:
    return "Modern Age"

def find_percentage(df,notfirst=False):
    df = df.groupby("shape").count()["city"]
    df = df.reset_index(drop=False)
    df["%"]= 100 * (df['city'] / df['city'].sum())
    if notfirst:
        df["shape_filtered"] = df["shape"].mask(df["%"] < 1, "other")
    df.sort_values("%", inplace=True, ascending=False)
    return df

def get_map(df):
    df["Observed time"] = df["Hour"].where(df["Hour"].between(8, 19), "Observed in night")
    df["Observed time"] = df["Observed time"].mask(df["Observed time"] != "Observed in night", "Observed in day")
    fig = px.scatter_mapbox(df, lat="latitude", lon="longitude ",hover_name="city",hover_data=["Time_clean","latitude","longitude ","shape"]
                            ,color="Observed time",color_discrete_sequence=["#F3C623","#10375C"],zoom=1,center={"lat" : 35.74,"lon" : -39.46})
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0}
                      ,title={"text":"<b>UFO sightings from 1906 to 2014</b>","xanchor":"center","yanchor":"top","x":0.5,"y":0.9}
                      ,height=500,width=800,legend = dict(x=0,y=0.2,traceorder="normal"))
    return fig

def get_pies(df):
    df["Period"] = df["Year"].apply(define_period)

    df_P1 = df[df["Period"] == "Before Golden Age"]
    df_P2 = df[df["Period"] == "Golden Age"]
    df_P3 = df[df["Period"] == "New Wave"]
    df_P4 = df[df["Period"] == "Modern Age"]

    df_P1 = df_P1[df_P1["shape"] != "other"]
    df_P2 = df_P2[df_P2["shape"] != "other"]
    df_P3 = df_P3[df_P3["shape"] != "other"]
    df_P4 = df_P4[df_P4["shape"] != "other"]

    df_P1_study = find_percentage(df_P1.copy())
    df_P2_study = find_percentage(df_P2.copy(),True)
    df_P3_study = find_percentage(df_P3.copy(),True)
    df_P4_study = find_percentage(df_P4.copy(),True)

    color_set = np.union1d(df_P1_study["shape"].values, df_P2_study["shape_filtered"].values)
    color_set = np.union1d(color_set, df_P3_study["shape_filtered"].values)
    color_set = np.union1d(color_set, df_P4_study["shape_filtered"].values)

    color_indexes = {}
    for i in range(color_set.shape[0]):
        color_indexes[color_set[i]] = px.colors.qualitative.Alphabet[i + 1]

    color_P1 = []
    for i in df_P1_study["shape"].values:
        color_P1.append(color_indexes[i])

    color_P2 = []
    for i in df_P2_study["shape_filtered"].values:
        color_P2.append(color_indexes[i])

    color_P3 = []
    for i in df_P3_study["shape_filtered"].values:
        color_P3.append(color_indexes[i])

    color_P4 = []
    for i in df_P4_study["shape_filtered"].values:
        color_P4.append(color_indexes[i])

    fig1 = go.Figure(data=[go.Pie(labels=df_P1_study["shape"], values=df_P1_study["city"], textinfo="label+percent",
                                  marker=dict(colors=color_P1), pull=[0.1])])
    fig1.update_layout(margin=dict(t=60, b=0, l=0, r=0), height=500, width=610,
                       title={"text": "<b>Distribution of UFO's shape in sighting during 1906-1938</b>",
                              "xanchor": "center", "yanchor": "top", "x": 0.5, "y": 0.9}, showlegend=False)

    fig2 = go.Figure(data=[
        go.Pie(labels=df_P2_study["shape_filtered"], values=df_P2_study["city"], textinfo="label+percent",
               marker=dict(colors=color_P2), pull=[0.1])])
    fig2.update_layout(margin=dict(t=60, b=0, l=0, r=0), height=500, width=610,
                       title={"text": "<b>Distribution of UFO's shape in sighting during 1938-1970</b>",
                              "xanchor": "center", "yanchor": "top", "x": 0.5, "y": 0.9}, showlegend=False)

    fig3 = go.Figure(data=[
        go.Pie(labels=df_P3_study["shape_filtered"], values=df_P3_study["city"], textinfo="label+percent",
               marker=dict(colors=color_P3), pull=[0.1])])
    fig3.update_layout(margin=dict(t=60, b=0, l=0, r=0), height=500, width=610,
                       title={"text": "<b>Distribution of UFO's shape in sighting during 1970-1996</b>",
                              "xanchor": "center", "yanchor": "top", "x": 0.5, "y": 0.9}, showlegend=False)

    fig4 = go.Figure(data=[
        go.Pie(labels=df_P4_study["shape_filtered"], values=df_P4_study["city"], textinfo="label+percent",
               marker=dict(colors=color_P4), pull=[0.1])])
    fig4.update_layout(margin=dict(t=70, b=0, l=0, r=0), height=600, width=610,
                       title={"text": "<b>Distribution of UFO's shape in sighting during 1996-now</b>",
                              "xanchor": "center", "yanchor": "top", "x": 0.5, "y": 0.9}, showlegend=False)

    return [fig1,fig2,fig3,fig4]