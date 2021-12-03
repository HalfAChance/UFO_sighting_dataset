import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from Graphes import Graphess
import json
import psutil
import os

with open("data/Texts.json","rb") as f:
    content = f.read()
    texts = json.loads(content)
    f.close()



Shape_ = pd.read_csv("data/ShapesByYear.csv")
#fig_racebar = get_racebar(Shape_)

data = pd.read_csv("data/Cleaned_with_continent.csv")

graphes = Graphess(data,Shape_)

fig_map = graphes.get_map()
fig_pie_list = graphes.get_pies()
fig_racebar = graphes.get_racebar()

#fig_map = get_map(data)
#fig_pie_list=get_pies(data)


app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(className="Body",children = [
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
                    html.H3(children="-----------------------------------------------------------------", className="Intro_title1"),
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
                    html.H3(children="-----------------------------------------------------------------", className="Intro_title1"),
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
                className="Period_Intro1",
                children=[
                    html.H3(children="-----------------------------------------------------------------", className="Intro_title"),
                    html.P(children=texts["Classic_SF"]["0_"], className="Period_intro_content"),
                    html.P(children=texts["Classic_SF"]["1_"], className="Period_intro_content"),
                    html.P(children=texts["Classic_SF"]["2_"], className="Period_intro_content"),
                    html.P(children=texts["Classic_SF"]["3_"], className="Period_intro_content"),
                    html.H3(children="-----------------------------------------------------------------",
                            className="Intro_title"),
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
                                        className="explaination_examlpe_timeline",
                                        children=[texts["Timeline1"]["graph_left"]["1_"],html.Br(),html.Br(),texts["Timeline1"]["graph_left"]["2_"]]
                                    ),
                                ]
                            )
                        ]
                    ),
                    html.Div(
                        className="TimeLine_pannel_right",
                        children=[
                            html.Div(
                                className="Container_timeline_right",
                                children=[
                                    html.Div(
                                        className="Container_timeline_right_content",
                                        children=[
                                            html.Img(
                                                className="Container_timeline_right_content_image",
                                                src="assets/the_war_of_worlds.jpg",
                                                width="150px"
                                            ),
                                            html.H2(children=texts["Timeline1"]["(1898)"]["0_"],
                                                    className="Timeline_event_title"),
                                            html.P(
                                                children=texts["Timeline1"]["(1898)"]["1_"],
                                                className="Timeline_event_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_right_time",
                                        children="1898"
                                    )

                                ]
                            ),
                            html.Div(
                                className="Indice_Timeline1",
                                children="1906: Where the data set begin...."
                            ),
                            html.Div(
                                className="Container_timeline_right",
                                children=[
                                    html.Div(
                                        className="Container_timeline_right_content",
                                        children=[
                                            html.Img(
                                                className="Container_timeline_right_content_image",
                                                src="/assets/1902.jpg",
                                                width="250px"
                                            ),
                                            html.H2(children=texts["Timeline1"]["(1902)"]["0_"],
                                                    className="Timeline_event_title"),
                                            html.P(
                                                children=texts["Timeline1"]["(1902)"]["1_"],
                                                className="Timeline_event_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_right_time",
                                        children="1902"
                                    )

                                ]
                            ),
                            html.Div(
                                className="Container_timeline_right",
                                children=[
                                    html.Div(
                                        className="Container_timeline_right_content",
                                        children=[
                                            html.Img(
                                                className="Container_timeline_right_content_image",
                                                src="assets/1910.png",
                                                width="250px"
                                            ),
                                            html.H2(children=texts["Timeline1"]["(1910)"]["0_"],
                                                    className="Timeline_event_title"),
                                            html.P(
                                                children=texts["Timeline1"]["(1910)"]["1_"],
                                                className="Timeline_event_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_right_time",
                                        children="1910"
                                    )
                                ]
                            ),
                            html.Div(
                                className="Container_timeline_right",
                                children=[
                                    html.Div(
                                        className="Container_timeline_right_content",
                                        children=[
                                            html.Img(
                                                className="Container_timeline_right_content_image",
                                                src="/assets/1922.jpg",
                                                width="250px"
                                            ),
                                            html.H2(children=texts["Timeline1"]["(1922)"]["0_"],
                                                    className="Timeline_event_title"),
                                            html.P(
                                                children=texts["Timeline1"]["(1922)"]["1_"],
                                                className="Timeline_event_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_right_time",
                                        children="1922"
                                    )

                                ]
                            ),
                            html.Div(
                                className="Indice_Timeline1",
                                children="1938"
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
                className="Period_Intro2",
                children=[
                    html.H3(children="-----------------------------------------------------------------",
                            className="Intro_title"),
                    html.P(children=texts["Golden_age"]["0_"], className="Period_intro_content"),
                    html.P(children=texts["Golden_age"]["1_"], className="Period_intro_content"),
                    html.P(children=texts["Golden_age"]["2_"], className="Period_intro_content"),
                    html.H3(children="-----------------------------------------------------------------",
                            className="Intro_title"),
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
                                children="1938"
                            ),
                            html.Div(
                                className="Container_timeline_left",
                                children=[
                                    html.Div(
                                        className="Container_timeline_left_content",
                                        children=[
                                            html.Img(
                                                className="Container_timeline_right_content_image",
                                                src="assets/1951.png",
                                                width="250px"
                                            ),
                                            html.H2(children=texts["Timeline2"]["(1951)"]["0_"],
                                                    className="Timeline_event_title"),
                                            html.P(
                                                children=texts["Timeline2"]["(1951)"]["1_"],
                                                className="Timeline_event_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_left_time",
                                        children="1951"
                                    )

                                ]
                            ),
                            html.Div(
                                className="Container_timeline_left",
                                children=[
                                    html.Div(
                                        className="Container_timeline_left_content",
                                        children=[
                                            html.Img(
                                                className="Container_timeline_right_content_image",
                                                src="assets/1953.png",
                                                width="250px"
                                            ),
                                            html.H2(children=texts["Timeline2"]["(1953)"]["0_"],
                                                    className="Timeline_event_title"),
                                            html.P(
                                                children=texts["Timeline2"]["(1953)"]["1_"],
                                                className="Timeline_event_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_left_time",
                                        children="1953"
                                    )

                                ]
                            ),
                            html.Div(
                                className="Container_timeline_left",
                                children=[
                                    html.Div(
                                        className="Container_timeline_left_content",
                                        children=[
                                            html.Img(
                                                className="Container_timeline_right_content_image",
                                                src="assets/1958.png",
                                                width="250px"
                                            ),
                                            html.H2(children=texts["Timeline2"]["(1958)"]["0_"],
                                                    className="Timeline_event_title"),
                                            html.P(
                                                children=texts["Timeline2"]["(1958)"]["1_"],
                                                className="Timeline_event_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_left_time",
                                        children="1958"
                                    )

                                ]
                            ),
                            html.Div(
                                className="Indice_Timeline2",
                                children="1960"
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
                                        className="explaination_examlpe_timeline",
                                        children=texts["Timeline2"]["graph_on_the_right"]["1_"]
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
                className="Period_Intro3",
                children=[
                    html.H3(children="-----------------------------------------------------------------",
                            className="Intro_title"),
                    html.P(children=texts["New_wave"]["0_"], className="Period_intro_content"),
                    html.P(children=texts["New_wave"]["1_"], className="Period_intro_content"),
                    html.P(children=texts["New_wave"]["2_"], className="Period_intro_content"),
                    html.H3(children="-----------------------------------------------------------------",
                            className="Intro_title"),
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
                                        className="explaination_examlpe_timeline",
                                        children=texts["Timeline3"]["graph_on_the_left"]["1_"]
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
                                children="1960"
                            ),
                            html.Div(
                                className="Container_timeline_right",
                                children=[
                                    html.Div(
                                        className="Container_timeline_right_content",
                                        children=[
                                            html.Img(
                                                className="Container_timeline_right_content_image",
                                                src="assets/1968.png",
                                                width="250px"
                                            ),
                                            html.H2(children=texts["Timeline3"]["(1968)"]["0_"],
                                                    className="Timeline_event_title"),
                                            html.P(
                                                children=texts["Timeline3"]["(1968)"]["1_"],
                                                className="Timeline_event_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_right_time",
                                        children="1968"
                                    )

                                ]
                            ),
                            html.Div(
                                className="Container_timeline_right",
                                children=[
                                    html.Div(
                                        className="Container_timeline_right_content",
                                        children=[
                                            html.Img(
                                                className="Container_timeline_right_content_image",
                                                src="assets/1977.jpg",
                                                width="250px"
                                            ),
                                            html.H2(children=texts["Timeline3"]["(1977)"]["0_"],
                                                    className="Timeline_event_title"),
                                            html.P(
                                                children=texts["Timeline3"]["(1977)"]["1_"],
                                                className="Timeline_event_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_right_time",
                                        children="1977"
                                    )

                                ]
                            ),
                            html.Div(
                                className="Container_timeline_right",
                                children=[
                                    html.Div(
                                        className="Container_timeline_right_content",
                                        children=[
                                            html.Img(
                                                className="Container_timeline_right_content_image",
                                                src="assets/1977_.png",
                                                width="150px"
                                            ),
                                            html.H2(children=texts["Timeline3"]["(1977)_"]["0_"],
                                                    className="Timeline_event_title"),
                                            html.P(
                                                children=texts["Timeline3"]["(1977)_"]["1_"],
                                                className="Timeline_event_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_right_time",
                                        children="1977"
                                    )

                                ]
                            ),
                            html.Div(
                                className="Container_timeline_right",
                                children=[
                                    html.Div(
                                        className="Container_timeline_right_content",
                                        children=[
                                            html.Img(
                                                className="Container_timeline_right_content_image",
                                                src="assets/1986.png",
                                                width="250px"
                                            ),
                                            html.H2(children=texts["Timeline3"]["(1986)"]["0_"],
                                                    className="Timeline_event_title"),
                                            html.P(
                                                children=texts["Timeline3"]["(1986)"]["1_"],
                                                className="Timeline_event_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_right_time",
                                        children="1986"
                                    )
                                ]
                            ),
                            html.Div(
                                className="Indice_Timeline3",
                                children="1996"
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
                className="Period_Intro4",
                children=[
                    html.H3(children="-----------------------------------------------------------------",
                            className="Intro_title"),
                    html.P(children=texts["Modern_age"]["0_"], className="Period_intro_content"),
                    html.P(children=texts["Modern_age"]["1_"], className="Period_intro_content"),
                    html.P(children=texts["Modern_age"]["2_"], className="Period_intro_content"),
                    html.H3(children="-----------------------------------------------------------------",
                            className="Intro_title"),
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
                                children="1996"
                            ),
                            html.Div(
                                className="Container_timeline_left",
                                children=[
                                    html.Div(
                                        className="Container_timeline_left_content",
                                        children=[
                                            html.Img(
                                                className="Container_timeline_right_content_image",
                                                src="assets/1997.png",
                                                width="250px"
                                            ),
                                            html.H2(children=texts["Timeline4"]["(1997)"]["0_"],
                                                    className="Timeline_event_title"),
                                            html.P(
                                                children=texts["Timeline4"]["(1997)"]["1_"],
                                                className="Timeline_event_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_left_time",
                                        children="1997"
                                    )

                                ]
                            ),
                            html.Div(
                                className="Container_timeline_left",
                                children=[
                                    html.Div(
                                        className="Container_timeline_left_content",
                                        children=[
                                            html.Img(
                                                className="Container_timeline_right_content_image",
                                                src="assets/2005.png",
                                                width="250px"
                                            ),
                                            html.H2(children=texts["Timeline4"]["(2005)"]["0_"],
                                                    className="Timeline_event_title"),
                                            html.P(
                                                children=texts["Timeline4"]["(2005)"]["1_"],
                                                className="Timeline_event_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_left_time",
                                        children="2005"
                                    )

                                ]
                            ),
                            html.Div(
                                className="Container_timeline_left",
                                children=[
                                    html.Div(
                                        className="Container_timeline_left_content",
                                        children=[
                                            html.Img(
                                                className="Container_timeline_right_content_image",
                                                src="assets/2011.png",
                                                width="250px"
                                            ),
                                            html.H2(children=texts["Timeline4"]["(2011)"]["0_"],
                                                    className="Timeline_event_title"),
                                            html.P(
                                                children=texts["Timeline4"]["(2011)"]["1_"],
                                                className="Timeline_event_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_left_time",
                                        children="2011"
                                    )

                                ]
                            ),
                            html.Div(
                                className="Container_timeline_left",
                                children=[
                                    html.Div(
                                        className="Container_timeline_left_content",
                                        children=[
                                            html.Img(
                                                className="Container_timeline_right_content_image",
                                                src="assets/2014.png",
                                                width="250px"
                                            ),
                                            html.H2(children=texts["Timeline4"]["(2014)"]["0_"],
                                                    className="Timeline_event_title"),
                                            html.P(
                                                children=texts["Timeline4"]["(2014)"]["1_"],
                                                className="Timeline_event_content")
                                        ]
                                    ),
                                    html.Div(
                                        className="Container_timeline_left_time",
                                        children="2014"
                                    )
                                ]
                            ),
                            html.Div(
                                className="Indice_Timeline4",
                                children="Now"
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
                                        className="explaination_examlpe_timeline",
                                        children=texts["Timeline4"]["graph_on_the_right"]["1_"]
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
print(u'RAM ：%.4f GB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024 / 1024) )
if __name__ == '__main__':
    app.run_server(debug=True)
