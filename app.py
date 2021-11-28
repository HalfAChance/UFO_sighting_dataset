import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from get_RaceBar import get_racebar
from Graphes import get_map
from Graphes import get_pies
import json
import psutil
import os

with open("data/Texts.json","r") as f:
    content = f.read()
    texts = json.loads(content)
    f.close()

Shape_ = pd.read_csv("data/ShapesByYear.csv")
fig_racebar = get_racebar(Shape_)

data = pd.read_csv("data/Cleaned_with_continent.csv")
fig_map = get_map(data)
fig_pie_list=get_pies(data)


intro_example = "An uniderovided pologists' favour unconventional, pseudoscientific hypotheses, some of which go beyond the typical extraterrestrial visitation claims and sometimes form part of new religions."
df = px.data.tips()
fig = px.pie(df, values='tip', names='day',height=500,width=500,title="Example graphe")

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(children = [
    html.Div(
        children=[
            html.H1(children="Peek the impact of Science Fiction through the sight of UFO",className="Title"),
            html.H2(children="Present by Tianyuan ZHANG and Adrien VILLEMIN",className = "Names")
        ],
        className="Title_board"
    ),
    html.Div(
        className="Intro_board",
        children = [
            html.Div(
                className="Intro_text_board",
                children=[
                    html.H3(children="Introduction", className="Intro_title1"),
                    html.P(children=texts["Intro"]["1_"], className="Intro_content")
                ]
            ),
            html.Div(
                className="Intro_graphe_board1",
                children=[
                    dcc.Graph(
                        id="graphe_intro1",
                        figure=fig_map
                    )
                ]
            ),
            html.Div(
                className="Intro_text_board",
                children = [
                    #html.H3(children="This is Introduction",className="Intro_title2"),
                    html.P(children=texts["Intro"]["2_"],className="Intro_content"),
                    html.P(children=texts["Intro"]["3_"], className="Intro_content"),
                    html.P(children=texts["Intro"]["4_"], className="Intro_content")
                ]
            ),
            html.Div(
                className="Intro_graphe_board2",
                children=[
                    dcc.Graph(
                        id="graphe_intro2",
                        figure=fig_racebar
                    )
                ]
            ),
            html.Div(
                className="Intro_text_board",
                children=[
                    # html.H3(children="This is Introduction",className="Intro_title2"),
                    html.P(children=texts["Intro"]["5_"], className="Intro_content"),
                    html.P(children=texts["Intro"]["6_"], className="Intro_content"),
                    html.P(children=texts["Intro"]["7_"], className="Intro_content")
                ]
            ),
            html.Div(
                className="End_intro",
                children=[
                    html.P(
                        children="-----------------------------------------------------------------"
                    ),
                    html.P(
                        children="---------------------------------------------------"
                    ),
                    html.P(
                        children="------------------------------------------"
                    ),
                    html.P(
                        children="-",className="End_invisible"
                    )

                ]
            )
        ]
    ),
    html.Div(
        className="Timeline_board1",
        children=[
            html.Div(
                className="Timeline1_title",
                children=[
                    html.H2(children="Before Golden Age (Before 1938)", className="Timeline1_title")
                ]
            ),
            html.Div(
                className="Timeline1",
                children=[
                    html.Div(
                        className="Graph_Timeline1",
                        children=[
                            html.Div(
                                className="Sticky_graph_Timeline1",
                                children=[
                                    dcc.Graph(
                                        id="example_timeline1",
                                        figure=fig_pie_list[0]
                                    ),
                                    html.P(
                                        className="explaination_examlpe_timeline1",
                                        children=" Lorem ipsum dolor sit amet elit. Aliquam odio dolor, id luctus erat sagittis non. Ut blandit semper pretium."
                                    )
                                ]
                            )
                        ]
                    ),
                    html.Div(
                        className="TimeLine_pannel_right",
                        children=[
                            html.Div(
                                className="Indice_Timeline1",
                                children="Start Year"
                            ),
                            html.Div(
                                className="Container_timeline_right",
                                children=[
                                    html.Div(
                                        className="Container_timeline_right_content",
                                        children=[
                                            html.H2(children="This is the title of event1",
                                                    className="Timeline1_event1_title"),
                                            html.P(
                                                children=" Lorem ipsum dolor sit amet elit. Aliquam odio dolor, id luctus erat sagittis non. Ut blandit semper pretium.",
                                                className="Timeline1_event1_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_right_time",
                                        children="Year 1"
                                    )

                                ]
                            ),
                            html.Div(
                                className="Container_timeline_right",
                                children=[
                                    html.Div(
                                        className="Container_timeline_right_content",
                                        children=[
                                            html.H2(children="This is the title of event2",
                                                    className="Timeline1_event2_title"),
                                            html.P(
                                                children=" Lorem ipsum dolor sit amet elit. Aliquam odio dolor, id luctus erat sagittis non. Ut blandit semper pretium.",
                                                className="Timeline1_event2_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_right_time",
                                        children="Year 2"
                                    )

                                ]
                            ),
                            html.Div(
                                className="Container_timeline_right",
                                children=[
                                    html.Div(
                                        className="Container_timeline_right_content",
                                        children=[
                                            html.H2(children="This is the title of event3",
                                                    className="Timeline1_event3_title"),
                                            html.P(
                                                children=" Lorem ipsum dolor sit amet elit. Aliquam odio dolor, id luctus erat sagittis non. Ut blandit semper pretium.",
                                                className="Timeline1_event3_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_right_time",
                                        children="Year 3"
                                    )

                                ]
                            ),
                            html.Div(
                                className="Container_timeline_right",
                                children=[
                                    html.Div(
                                        className="Container_timeline_right_content",
                                        children=[
                                            html.H2(children="This is the title of event4",
                                                    className="Timeline1_event4_title"),
                                            html.P(
                                                children=" Lorem ipsum dolor sit amet elit. Aliquam odio dolor, id luctus erat sagittis non. Ut blandit semper pretium.",
                                                className="Timeline1_event4_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_right_time",
                                        children="Year 4"
                                    )
                                ]
                            ),
                            html.Div(
                                className="Indice_Timeline1",
                                children="End Year"
                            ),
                        ]
                    )
                ]
            )
        ]
    ),

    html.Div(
        className="Timeline_board2",
        children=[
            html.Div(
                className="Timeline2_title",
                children=[
                    html.H2(children="Golden Age (1938 - 1960)", className="Timeline2_title")
                ]
            ),
            html.Div(
                className="Timeline2",
                children=[
                    html.Div(
                        className="TimeLine_pannel_left",
                        children=[
                            html.Div(
                                className="Indice_Timeline2",
                                children="Start Year"
                            ),
                            html.Div(
                                className="Container_timeline_left",
                                children=[
                                    html.Div(
                                        className="Container_timeline_left_content",
                                        children=[
                                            html.H2(children="This is the title of event1",
                                                    className="Timeline2_event1_title"),
                                            html.P(
                                                children=" Lorem ipsum dolor sit amet elit. Aliquam odio dolor, id luctus erat sagittis non. Ut blandit semper pretium.",
                                                className="Timeline2_event1_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_left_time",
                                        children="Year 1"
                                    )

                                ]
                            ),
                            html.Div(
                                className="Container_timeline_left",
                                children=[
                                    html.Div(
                                        className="Container_timeline_left_content",
                                        children=[
                                            html.H2(children="This is the title of event2",
                                                    className="Timeline2_event2_title"),
                                            html.P(
                                                children=" Lorem ipsum dolor sit amet elit. Aliquam odio dolor, id luctus erat sagittis non. Ut blandit semper pretium.",
                                                className="Timeline2_event2_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_left_time",
                                        children="Year 2"
                                    )

                                ]
                            ),
                            html.Div(
                                className="Container_timeline_left",
                                children=[
                                    html.Div(
                                        className="Container_timeline_left_content",
                                        children=[
                                            html.H2(children="This is the title of event3",
                                                    className="Timeline2_event3_title"),
                                            html.P(
                                                children=" Lorem ipsum dolor sit amet elit. Aliquam odio dolor, id luctus erat sagittis non. Ut blandit semper pretium.",
                                                className="Timeline2_event3_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_left_time",
                                        children="Year 3"
                                    )

                                ]
                            ),
                            html.Div(
                                className="Container_timeline_left",
                                children=[
                                    html.Div(
                                        className="Container_timeline_left_content",
                                        children=[
                                            html.H2(children="This is the title of event4",
                                                    className="Timeline2_event4_title"),
                                            html.P(
                                                children=" Lorem ipsum dolor sit amet elit. Aliquam odio dolor, id luctus erat sagittis non. Ut blandit semper pretium.",
                                                className="Timeline2_event4_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_left_time",
                                        children="Year 4"
                                    )
                                ]
                            ),
                            html.Div(
                                className="Indice_Timeline2",
                                children="End Year"
                            ),
                        ]
                    ),
                    html.Div(
                        className="Graph_Timeline2",
                        children=[
                            html.Div(
                                className="Sticky_graph_Timeline2",
                                children=[
                                    dcc.Graph(
                                        id="example_timeline2",
                                        figure=fig_pie_list[1]
                                    ),
                                    html.P(
                                        className="explaination_examlpe_timeline2",
                                        children=" Lorem ipsum dolor sit amet elit. Aliquam odio dolor, id luctus erat sagittis non. Ut blandit semper pretium."
                                    )
                                ]
                            )
                        ]
                    ),
                ]
            )
        ]
    ),

    html.Div(
        className="Timeline_board3",
        children=[
            html.Div(
                className="Timeline3_title",
                children=[
                    html.H2(children="New Wave (1960 - 1996)", className="Timeline3_title")
                ]
            ),
            html.Div(
                className="Timeline3",
                children=[
                    html.Div(
                        className="Graph_Timeline3",
                        children=[
                            html.Div(
                                className="Sticky_graph_Timeline3",
                                children=[
                                    dcc.Graph(
                                        id="example_timeline3",
                                        figure=fig_pie_list[2]
                                    ),
                                    html.P(
                                        className="explaination_examlpe_timeline3",
                                        children=" Lorem ipsum dolor sit amet elit. Aliquam odio dolor, id luctus erat sagittis non. Ut blandit semper pretium."
                                    )
                                ]
                            )
                        ]
                    ),
                    html.Div(
                        className="TimeLine_pannel_right",
                        children=[
                            html.Div(
                                className="Indice_Timeline3",
                                children="Start Year"
                            ),
                            html.Div(
                                className="Container_timeline_right",
                                children=[
                                    html.Div(
                                        className="Container_timeline_right_content",
                                        children=[
                                            html.H2(children="This is the title of event1",
                                                    className="Timeline3_event1_title"),
                                            html.P(
                                                children=" Lorem ipsum dolor sit amet elit. Aliquam odio dolor, id luctus erat sagittis non. Ut blandit semper pretium.",
                                                className="Timeline3_event1_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_right_time",
                                        children="Year 1"
                                    )

                                ]
                            ),
                            html.Div(
                                className="Container_timeline_right",
                                children=[
                                    html.Div(
                                        className="Container_timeline_right_content",
                                        children=[
                                            html.H2(children="This is the title of event2",
                                                    className="Timeline3_event2_title"),
                                            html.P(
                                                children=" Lorem ipsum dolor sit amet elit. Aliquam odio dolor, id luctus erat sagittis non. Ut blandit semper pretium.",
                                                className="Timeline3_event2_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_right_time",
                                        children="Year 2"
                                    )

                                ]
                            ),
                            html.Div(
                                className="Container_timeline_right",
                                children=[
                                    html.Div(
                                        className="Container_timeline_right_content",
                                        children=[
                                            html.H2(children="This is the title of event3",
                                                    className="Timeline3_event3_title"),
                                            html.P(
                                                children=" Lorem ipsum dolor sit amet elit. Aliquam odio dolor, id luctus erat sagittis non. Ut blandit semper pretium.",
                                                className="Timeline3_event3_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_right_time",
                                        children="Year 3"
                                    )

                                ]
                            ),
                            html.Div(
                                className="Container_timeline_right",
                                children=[
                                    html.Div(
                                        className="Container_timeline_right_content",
                                        children=[
                                            html.H2(children="This is the title of event4",
                                                    className="Timeline3_event4_title"),
                                            html.P(
                                                children=" Lorem ipsum dolor sit amet elit. Aliquam odio dolor, id luctus erat sagittis non. Ut blandit semper pretium.",
                                                className="Timeline3_event4_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_right_time",
                                        children="Year 4"
                                    )
                                ]
                            ),
                            html.Div(
                                className="Indice_Timeline3",
                                children="End Year"
                            ),
                        ]
                    )
                ]
            )
        ]
    ),

    html.Div(
        className="Timeline_board4",
        children=[
            html.Div(
                className="Timeline4_title",
                children=[
                    html.H2(children="Modern Age (1996 - now)", className="Timeline4_title")
                ]
            ),
            html.Div(
                className="Timeline4",
                children=[
                    html.Div(
                        className="TimeLine_pannel_left",
                        children=[
                            html.Div(
                                className="Indice_Timeline4",
                                children="Start Year"
                            ),
                            html.Div(
                                className="Container_timeline_left",
                                children=[
                                    html.Div(
                                        className="Container_timeline_left_content",
                                        children=[
                                            html.H2(children="This is the title of event1",
                                                    className="Timeline4_event1_title"),
                                            html.P(
                                                children=" Lorem ipsum dolor sit amet elit. Aliquam odio dolor, id luctus erat sagittis non. Ut blandit semper pretium.",
                                                className="Timeline4_event1_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_left_time",
                                        children="Year 1"
                                    )

                                ]
                            ),
                            html.Div(
                                className="Container_timeline_left",
                                children=[
                                    html.Div(
                                        className="Container_timeline_left_content",
                                        children=[
                                            html.H2(children="This is the title of event2",
                                                    className="Timeline4_event2_title"),
                                            html.P(
                                                children=" Lorem ipsum dolor sit amet elit. Aliquam odio dolor, id luctus erat sagittis non. Ut blandit semper pretium.",
                                                className="Timeline4_event2_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_left_time",
                                        children="Year 2"
                                    )

                                ]
                            ),
                            html.Div(
                                className="Container_timeline_left",
                                children=[
                                    html.Div(
                                        className="Container_timeline_left_content",
                                        children=[
                                            html.H2(children="This is the title of event3",
                                                    className="Timeline4_event3_title"),
                                            html.P(
                                                children=" Lorem ipsum dolor sit amet elit. Aliquam odio dolor, id luctus erat sagittis non. Ut blandit semper pretium.",
                                                className="Timeline4_event3_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_left_time",
                                        children="Year 3"
                                    )

                                ]
                            ),
                            html.Div(
                                className="Container_timeline_left",
                                children=[
                                    html.Div(
                                        className="Container_timeline_left_content",
                                        children=[
                                            html.H2(children="This is the title of event4",
                                                    className="Timeline4_event4_title"),
                                            html.P(
                                                children=" Lorem ipsum dolor sit amet elit. Aliquam odio dolor, id luctus erat sagittis non. Ut blandit semper pretium.",
                                                className="Timeline4_event4_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_left_time",
                                        children="Year 4"
                                    )
                                ]
                            ),
                            html.Div(
                                className="Indice_Timeline4",
                                children="End Year"
                            ),
                        ]
                    ),
                    html.Div(
                        className="Graph_Timeline4",
                        children=[
                            html.Div(
                                className="Sticky_graph_Timeline4",
                                children=[
                                    dcc.Graph(
                                        id="example_timeline4",
                                        figure=fig_pie_list[3]
                                    ),
                                    html.P(
                                        className="explaination_examlpe_timeline4",
                                        children=" Lorem ipsum dolor sit amet elit. Aliquam odio dolor, id luctus erat sagittis non. Ut blandit semper pretium."
                                    )
                                ]
                            )
                        ]
                    ),
                ]
            )
        ]
    ),






])
print(u'当前进程的内存使用：%.4f GB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024 / 1024) )
if __name__ == '__main__':
    app.run_server(debug=True)
