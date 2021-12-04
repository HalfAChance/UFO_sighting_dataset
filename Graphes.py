import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import re

def define_period(value):
    if value <= 1938:
        return "Before Golden Age"
    elif value > 1938 and value <= 1970:
        return "Golden Age"
    elif value > 1970 and value <= 1996:
        return "New Wave"
    else:
        return "Modern Age"


def get_parents(value):
    if value <= 2:
        return "Rare shapes"
    elif value > 2 and value <= 9:
        return "Common shapes"
    else:
        return "High frequent shapes"


def find_percentage(df, notfirst=False):
    df = df.groupby("shape").count()["city"]
    df = df.reset_index(drop=False)
    df["%"] = 100 * (df['city'] / df['city'].sum())
    if notfirst:
        df["shape_filtered"] = df["shape"].mask(df["%"] < 1, "other")
    df.sort_values("%", inplace=True, ascending=False)
    return df

def change_duration(value):
  value = str(value)
  value = float(re.findall(r"\d+",value)[0])
  if value > 3600:
    return 3600
  else:
    return value


class Graphess():
    def __init__(self,df_clean,df_bar,df_movies):
        self.df_clean = df_clean
        self.color_indexes={}
        self.df_bar = df_bar
        self.df_movies = df_movies

    def get_map(self):
        self.df_clean["duration (seconds)"] = self.df_clean["duration (seconds)"].apply(change_duration)
        fig = go.Figure(go.Densitymapbox(lat=self.df_clean["latitude"], lon=self.df_clean["longitude "], z=self.df_clean["duration (seconds)"], radius=6,
                                         colorscale="Cividis",opacity=0.8,
                                         hovertemplate="lon: %{lon}<br>lat: %{lat}<br>Sighting duration: %{z}s<extra></extra>",colorbar={"title":"Sighting duration<br>(seconds)"}))
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0},width=900, height=500,
                          title={"text": "<b>Duration of UFO sighting since 1906</b>",
                                 "xanchor": "center", "yanchor": "top", "x": 0.5, "y": 0.9,"font":{"color":"#212121","size":20,"family":"Trebuchet MS"}}, legend=dict(x=0,y=.5,traceorder="normal"))

        df_info_c = self.df_movies.groupby(["iso3", "continent", "country_first"]).count()["title"]
        df_info_c = df_info_c.reset_index(drop=False)
        df_info_c.columns = ["iso3", "continent", "country_first", "Sci-Fi films"]

        fig_ = px.scatter_geo(df_info_c, locations="iso3", color="continent", size="Sci-Fi films", size_max=100,
                             hover_name="country_first", hover_data={"iso3": False, "continent": False},
                             projection="natural earth")
        fig_.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0}, width=900, height=500,
                          title={"text": "<b>Sci-Fi movies since 1906</b>",
                                 "xanchor": "center", "yanchor": "top", "x": 0.5, "y": 0.9,"font":{"color":"#212121","size":20,"family":"Trebuchet MS"}},
                          legend=dict(x=0, y=.5, traceorder="normal"))

        return [fig,fig_]

    def get_pies(self):
        # Preprocessing:
        self.df_clean["Period"] = self.df_clean["Year"].apply(define_period)
        df_P1 = self.df_clean[self.df_clean["Period"] == "Before Golden Age"]
        df_P2 = self.df_clean[self.df_clean["Period"] == "Golden Age"]
        df_P3 = self.df_clean[self.df_clean["Period"] == "New Wave"]
        df_P4 = self.df_clean[self.df_clean["Period"] == "Modern Age"]

        df_P1 = df_P1[df_P1["shape"] != "other"]
        df_P2 = df_P2[df_P2["shape"] != "other"]
        df_P3 = df_P3[df_P3["shape"] != "other"]
        df_P4 = df_P4[df_P4["shape"] != "other"]

        df_P1_study = df_P1.groupby("shape").count()["city"]
        df_P1_study = df_P1_study.reset_index(drop=False)
        df_P1_study["%"] = 100 * (df_P1_study['city'] / df_P1_study['city'].sum())
        df_P1_study.sort_values("%", inplace=True, ascending=False)

        df_P2_study = df_P2.groupby("shape").count()["city"]
        df_P2_study = df_P2_study.reset_index(drop=False)
        df_P2_study["%"] = 100 * (df_P2_study['city'] / df_P2_study['city'].sum())
        df_P2_study["shape_filtered"] = df_P2_study["shape"].mask(df_P2_study["%"] < 1, "other")
        df_P2_study.sort_values("%", inplace=True, ascending=False)

        df_P3_study = df_P3.groupby("shape").count()["city"]
        df_P3_study = df_P3_study.reset_index(drop=False)
        df_P3_study["%"] = 100 * (df_P3_study['city'] / df_P3_study['city'].sum())
        df_P3_study["shape_filtered"] = df_P3_study["shape"].mask(df_P3_study["%"] < 1, "other")
        df_P3_study.sort_values("%", inplace=True, ascending=False)

        df_P4_study = df_P4.groupby("shape").count()["city"]
        df_P4_study = df_P4_study.reset_index(drop=False)
        df_P4_study["%"] = 100 * (df_P4_study['city'] / df_P4_study['city'].sum())
        df_P4_study["shape_filtered"] = df_P4_study["shape"].mask(df_P4_study["%"] < 1, "other")
        df_P4_study.sort_values("%", inplace=True, ascending=False)

        color_set = np.union1d(df_P1_study["shape"].values, df_P2_study["shape_filtered"].values)
        color_set = np.union1d(color_set, df_P3_study["shape_filtered"].values)
        color_set = np.union1d(color_set, df_P4_study["shape_filtered"].values)
        color_set = color_set.tolist()
        labels_all = ["Total", "Rare shapes", "Common shapes", "High frequent shapes"]
        parents_all = ["", "Total", "Total", "Total"]
        color_set = labels_all + color_set

        for i in range(len(color_set)):
            self.color_indexes[color_set[i]] = px.colors.qualitative.Alphabet[i + 1]

        # Pie1
        color_P1 = []
        for i in df_P1_study["shape"].values:
            color_P1.append(self.color_indexes[i])

        fig1 = go.Figure(data=[go.Pie(labels=df_P1_study["shape"], values=df_P1_study["city"], textinfo="label+percent",hovertemplate="<b>%{label}</b><br>Total counts: %{value}<br><extra></extra>",
                                      marker=dict(colors=color_P1), pull=[0.1])])
        fig1.update_layout(margin=dict(t=60, b=0, l=0, r=0), height=500, width=610,
                           title={"text": "<b>Distribution of UFO's shape in sighting during 1906-1938</b>",
                                  "xanchor": "center", "yanchor": "top", "x": 0.5, "y": 0.9,"font":{"color":"#212121","size":20,"family":"Trebuchet MS"}}, showlegend=False)

        # sunburst2
        total2 = df_P2_study["city"].sum()
        df_P2_study["parent"] = df_P2_study["%"].apply(get_parents)
        total_low2 = df_P2_study[df_P2_study["parent"] == "Rare shapes"]["city"].sum()
        total_med2 = df_P2_study[df_P2_study["parent"] == "Common shapes"]["city"].sum()
        total_high2 = df_P2_study[df_P2_study["parent"] == "High frequent shapes"]["city"].sum()

        values_all = [total2, total_low2, total_med2, total_high2]
        color2 = df_P2_study["shape_filtered"].unique().tolist()

        labels_2 = labels_all + df_P2_study["shape_filtered"].unique().tolist()
        temp = len(labels_2) - 4
        parents_2 = parents_all + df_P2_study["parent"].values[:temp].tolist()
        values_2 = values_all + df_P2_study["city"].values[:temp].tolist()
        values_2[-1] = df_P2_study[df_P2_study["shape_filtered"] == "other"].sum()["city"]

        color_P2 = []
        for i in labels_2:
            color_P2.append(self.color_indexes[i])
        color_P2[0] = ""

        fig2 = go.Figure(go.Sunburst(
            labels=labels_2,
            parents=parents_2,
            values=values_2,
            branchvalues="total",
            textinfo="label+percent entry",
            marker=dict(
                colors=color_P2,
            ),
            hovertemplate="<b>%{label}</b><br>Total counts: %{value}<br><extra></extra>",
        ))
        fig2.update_layout(margin=dict(t=60, b=0, l=0, r=0), height=500, width=610,
                           title={"text": "<b>Distribution of UFO's shape in sighting during 1938-1970</b>",
                                  "xanchor": "center", "yanchor": "top", "x": 0.5, "y": 0.95,"font":{"color":"#212121","size":20,"family":"Trebuchet MS"}}, showlegend=False)

        # Sunburst3
        total3 = df_P3_study["city"].sum()
        df_P3_study["parent"] = df_P3_study["%"].apply(get_parents)
        total_low3 = df_P3_study[df_P3_study["parent"] == "Rare shapes"]["city"].sum()
        total_med3 = df_P3_study[df_P3_study["parent"] == "Common shapes"]["city"].sum()
        total_high3 = df_P3_study[df_P3_study["parent"] == "High frequent shapes"]["city"].sum()
        values_all = [total3, total_low3, total_med3, total_high3]

        color3 = df_P3_study["shape_filtered"].unique().tolist()

        labels_3 = labels_all + df_P3_study["shape_filtered"].unique().tolist()
        temp = len(labels_3) - 4
        parents_3 = parents_all + df_P3_study["parent"].values[:temp].tolist()
        values_3 = values_all + df_P3_study["city"].values[:temp].tolist()
        values_3[-1] = df_P3_study[df_P3_study["shape_filtered"] == "other"].sum()["city"]

        color_P3 = []
        for i in labels_3:
            color_P3.append(self.color_indexes[i])
        color_P3[0] = ""

        fig3 = go.Figure(go.Sunburst(
            labels=labels_3,
            parents=parents_3,
            values=values_3,
            branchvalues="total",
            textinfo="label+percent entry",
            marker=dict(
                colors=color_P3,
            ),
            hovertemplate="<b>%{label}</b><br>Total counts: %{value}<br><extra></extra>",
        ))
        fig3.update_layout(margin=dict(t=60, b=0, l=0, r=0), height=500, width=610,
                           title={"text": "<b>Distribution of UFO's shape in sighting during 1970-1996</b>",
                                  "xanchor": "center", "yanchor": "top", "x": 0.5, "y": 0.95,"font":{"color":"#212121","size":20,"family":"Trebuchet MS"}}, showlegend=False)

        # sunburst4
        total4 = df_P4_study["city"].sum()
        df_P4_study["parent"] = df_P4_study["%"].apply(get_parents)
        total_low4 = df_P4_study[df_P4_study["parent"] == "Rare shapes"]["city"].sum()
        total_med4 = df_P4_study[df_P4_study["parent"] == "Common shapes"]["city"].sum()
        total_high4 = df_P4_study[df_P4_study["parent"] == "High frequent shapes"]["city"].sum()

        values_all = [total4, total_low4, total_med4, total_high4]
        color4 = df_P4_study["shape_filtered"].unique().tolist()

        labels_4 = labels_all + df_P4_study["shape_filtered"].unique().tolist()
        temp = len(labels_4) - 4
        parents_4 = parents_all + df_P4_study["parent"].values[:temp].tolist()
        values_4 = values_all + df_P4_study["city"].values[:temp].tolist()
        values_4[-1] = df_P4_study[df_P4_study["shape_filtered"] == "other"].sum()["city"]

        color_P4 = []
        for i in labels_4:
            color_P4.append(self.color_indexes[i])
        color_P4[0] = ""

        fig4 = go.Figure(go.Sunburst(
            labels=labels_4,
            parents=parents_4,
            values=values_4,
            branchvalues="total",
            textinfo="label+percent entry",
            marker=dict(
                colors=color_P4,
            ),
            hovertemplate="<b>%{label}</b><br>Total counts: %{value}<br><extra></extra>",
        ))
        fig4.update_layout(margin=dict(t=60, b=0, l=0, r=0), height=500, width=610,
                           title={"text": "<b>Distribution of UFO's shape in sighting during 1996-now</b>",
                                  "xanchor": "center", "yanchor": "top", "x": 0.5, "y": 0.95,"font":{"color":"#212121","size":20,"family":"Trebuchet MS"}}, showlegend=False)

        return [fig1, fig2, fig3, fig4]

    def get_racebar(self):
        # Preprocessing:
        name = self.df_bar.columns.values.tolist()
        name.pop(-1)
        name = np.intersect1d(name, list(self.color_indexes.keys())).tolist()
        years = self.df_bar["Year"].values.tolist()

        link_year_name = []
        link_year_value = []

        for frame in range(len(years)):
            xdata = self.df_bar.iloc[frame][name].values
            dicc = {}
            for i in range(len(name)):
                dicc[name[i]] = xdata[i]
            dicc = sorted(dicc.items(), key=lambda kv: (kv[1], kv[0]))

            name_ = []
            xdata = []
            for i, j in dicc:
                name_.append(i)
                xdata.append(j)
            link_year_name.append(name_)
            link_year_value.append(xdata)

        link_name = link_year_name.copy()
        link_value = link_year_value.copy()
        trace0 = []
        colors = []
        for i in link_name[0][-10:]:
            colors.append(self.color_indexes[i])

        # Inital chart:
        initial = np.zeros(10)
        trace = go.Bar(
            y=link_name[0][-10:].copy(),
            x=initial,
            orientation='h',
            marker=dict(
                color=colors
            )

        )

        trace0.append(trace)

        # Layout part:
        layout1 = go.Layout(width=800, height=500,plot_bgcolor="#A7BBC7",
                            title={"text":"<b>The evolution of UFO's shape</b>","xanchor": "center", "yanchor": "top", "x": 0.5, "y": 0.9,"font":{"color":"#212121","size":20,"family":"Trebuchet MS"}},
                            hovermode="closest",
                            xaxis=dict(range=[0, 1]),
                            updatemenus=[dict(type="buttons",
                                              buttons=[dict(label="<b>Play</b>",
                                                            method="animate",
                                                            args=[None, dict(fromcurrent=True, frame=dict(duration=250),
                                                                             transition=dict(duration=0))]),
                                                       dict(label="<b>Pause</b>",
                                                            method="animate",
                                                            args=[[None], dict(mode="immediate")])],
                                              direction="left",
                                              showactive=False,
                                              x=0,
                                              y=-0.2,
                                              xanchor="right",
                                              yanchor="top")])

        # Slider part:
        sliders_dict = {
            "active": 0,
            "yanchor": "top",
            "xanchor": "left",
            "bgcolor": "#F3F1F5",
            "bordercolor": "#E1E5EA",
            "currentvalue": {
                "font": {"size": 20},
                "prefix": "<b>Year:</b>",
                "visible": True,
                "xanchor": "right",
            },
            "transition": {"duration": 300, "easing": "cubic-in-out"},
            "pad": {"b": 10, "t": 50},
            "len": 0.9,
            "x": 0.1,
            "y": 0.1,
            "steps": []
        }

        # Animation part
        traceN = []
        size = 1
        for i in range(len(years)):
            x_data = link_value[i][-10:].copy()
            y_data = link_name[i][-10:].copy()

            colors = []
            for j in y_data:
                colors.append(self.color_indexes[j])

            trace_ = go.Bar(
                y=y_data,
                x=x_data,
                orientation='h',
                marker={
                    "color": colors
                })

            annotation = []
            for x_, y_ in zip(x_data, y_data):
                annotation.append(dict(xref="x", yref="y", y=y_, x=x_ / 2, text=str(int(x_)),
                                       font=dict(family="Arial", color="#F3F1F5"), showarrow=False))

            size = np.max(x_data)

            traceN.append(
                go.Frame(data=[trace_], name=str(years[i]),
                         layout=dict(xaxis=dict(range=[0, size]), annotations=annotation)))

            slider_step = {"args": [
                [str(years[i])],
                {"frame": {"duration": 100},
                 "mode": "immediate",
                 "transition": {"duration": 100}}
            ],
                "label": "<b>" + str(int(years[i])) + "</b>",
                "method": "animate"}

            sliders_dict["steps"].append(slider_step)

        layout1.sliders = [sliders_dict]

        fig_ = go.Figure(data=trace0, layout=layout1, frames=traceN)
        return fig_






