import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import plotly.graph_objects as go



def num2color(values, cmap):
    norm = mpl.colors.Normalize(vmin=np.min(values), vmax=np.max(values))
    cmap = mpl.cm.get_cmap(cmap)
    return [cmap(norm(val)) for val in values]

def get_racebar(Shape_):
    values = np.arange(0, 30, 1)
    colors = num2color(values, "rainbow")

    name = Shape_.columns.values.tolist()
    name.pop(-1)
    years = Shape_["Year"].values.tolist()
    link_color = {}
    for i in range(30):
        link_color[name[i]] = colors[i]

    link_year_name = []
    link_year_value = []

    for frame in range(len(years)):
        xdata = Shape_.iloc[frame][0:30].values
        objects = np.max(xdata)
        dicc = {}
        for i in range(30):
            dicc[name[i]] = xdata[i]
        dicc = sorted(dicc.items(), key=lambda kv: (kv[1], kv[0]))

        name_ = []
        xdata = []
        for i, j in dicc:
            name_.append(i)
            xdata.append(j)
        link_year_name.append(name_)
        link_year_value.append(xdata)

        sort_color = []
        for i in name_:
            sort_color.append(link_color[i])

    link_name = link_year_name.copy()

    link_value = link_year_value.copy()

    temp = link_color.copy()
    temp2 = {}
    for i, j in temp.items():
        j = list(j)
        r = np.floor(j[0] * 255)
        g = np.floor(j[1] * 255)
        b = np.floor(j[2] * 255)
        a = j[3]
        temp2[i] = "rgb" + str((r, g, b))

    link_colors = temp2

    trace0 = []
    colors = []
    for i in link_name[0][-10:]:
        colors.append(link_colors[i])

    initial = np.zeros(10)

    trace = go.Bar(
        y=["other"],
        x=initial,
        orientation='h',
        marker=dict(
            color=colors
        )

    )

    trace0.append(trace)

    layout1 = go.Layout(width=700, height=500,
                        title="<b>Shapes of witeness</b>",
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
                                          y=-0.1,
                                          xanchor="right",
                                          yanchor="top")])

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
        "y": 0,
        "steps": []
    }

    traceN = []
    size = 1
    for i in range(len(years)):
        x_data = link_value[i][-10:].copy()
        y_data = link_name[i][-10:].copy()
        # A problem here:

        # The following commented code are use to eliminate the shape with 0 witness, so the graphe
        # will start with only one bar, then two, then three...

        # But using the following commented code can cause some problems with the animation. For example, if
        # you move the progress bar to the middle and then back to the start, there will be a misalignment in the image.

        # I think that's because for some reason, move the progress bar only update the bar plot, but it will not update
        # the the layout of the graph. I don't know to fix it.
        '''''
        need_to_del = 0
        for k in range(len(x_data)):
            if x_data[k] == 0:
                need_to_del += 1

        for k in range(need_to_del):
            x_data.pop(0)
            y_data.pop(0)
        '''''
        colors = []
        for j in y_data:
            colors.append(link_colors[j])

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
                                   font=dict(family="Arial", color="rgb(255,255,255)"), showarrow=False))

        if size <= np.max(x_data):
            size = np.max(x_data) * 5
        '''''
        if i < 5:
            size = size + 0.01

        if i==0:
            size=1
        '''''
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