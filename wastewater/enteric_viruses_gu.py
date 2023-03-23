import pandas as pd
import datetime
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime as dt
from plotly.io import write_image

# # Knivsta, Vaxholm and Österåker.
# Göteborg, Malmö and Stockholm-Käppala

wastewater_data = pd.read_excel(
    "https://blobserver.dckube.scilifelab.se/blob/wastewater_data_gu_allviruses.xlsx",
    sheet_name="all_viruses",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)
# Convert the dates
wastewater_data["year"] = (wastewater_data["week"].str[:4]).astype(int)
wastewater_data["week_no"] = wastewater_data["week"].str[-3:]
wastewater_data["week_no"] = (
    wastewater_data["week_no"].str.replace("-", "", regex=True)
).astype(int)
# set the date to the start of the week (Monday)
wastewater_data["day"] = 1
wastewater_data["date"] = wastewater_data.apply(
    lambda row: dt.fromisocalendar(row["year"], row["week_no"], row["day"]), axis=1
)
wastewater_data = wastewater_data[(wastewater_data["date"] >= "2023-01-16")]


fig = go.Figure(
    data=[
        go.Scatter(
            name="Enterovirus",
            x=wastewater_data.date,
            y=wastewater_data.enterovirus,
            mode="lines+markers",
            marker=dict(color=px.colors.diverging.RdBu[0], size=7),
            marker_symbol="square",
            line=dict(color=px.colors.diverging.RdBu[0], width=2),
            visible=True,
        ),
        go.Scatter(
            name="PMMoV",
            x=wastewater_data.date,
            y=wastewater_data.PMMoV,
            mode="lines+markers",
            marker=dict(color=px.colors.diverging.RdBu[1], size=7),
            marker_symbol="cross",
            line=dict(color=px.colors.diverging.RdBu[1], width=2),
            visible=False,
        ),
        go.Scatter(
            name="Adenovirus",
            x=wastewater_data.date,
            y=wastewater_data.adenovirus,
            mode="lines+markers",
            marker=dict(color=px.colors.diverging.RdBu[2], size=7),
            marker_symbol="hourglass",
            line=dict(color=px.colors.diverging.RdBu[2], width=2),
            visible=False,
        ),
        go.Scatter(
            name="GG2",
            x=wastewater_data.date,
            y=wastewater_data.GG2,
            mode="lines+markers",
            marker=dict(color=px.colors.diverging.RdBu[3], size=7),
            marker_symbol="cross",
            line=dict(color=px.colors.diverging.RdBu[3], width=2),
            visible=False,
        ),
        go.Scatter(
            name="Astrovirus",
            x=wastewater_data.date,
            y=wastewater_data.astrovirus,
            mode="lines+markers",
            marker=dict(color=px.colors.diverging.RdBu[8], size=7),
            marker_symbol="square",
            line=dict(color=px.colors.diverging.RdBu[8], width=2),
            visible=False,
        ),
        go.Scatter(
            name="Sapovirus",
            x=wastewater_data.date,
            y=wastewater_data.sapovirus,
            mode="lines+markers",
            marker=dict(color=px.colors.diverging.RdBu[9], size=7),
            marker_symbol="cross",
            line=dict(color=px.colors.diverging.RdBu[9], width=2),
            visible=False,
        ),
    ]
)
fig.update_layout(
    plot_bgcolor="white",
    autosize=True,
    font=dict(size=14),
    margin=dict(r=150, t=65, b=0, l=0),
    # width=900,
    # height=500,
    legend=dict(yanchor="top", y=0.95, xanchor="left", x=0.99, font=dict(size=14)),
    hovermode="x unified",
    hoverdistance=1,
)
fig.update_xaxes(
    title="<br><b>Date (Week Commencing)</b>",
    showgrid=True,
    linecolor="black",
    tickangle=45,
)
fig.update_yaxes(
    title="<b>Relative amount of virus</b>",
    showgrid=True,
    gridcolor="lightgrey",
    linecolor="black",
    # below ensures a zeroline on Y axis. Made it black to be clear it's different from other lines
    rangemode="tozero"
    # range=[0, max(wastewater_data["relative_copy_number"] * 1.15)],
)

# select viruses

button_layer_1_height = 1.26
fig.update_layout(
    updatemenus=[
        dict(
            buttons=list(
                [
                    dict(
                        method="update",
                        args=[
                            {
                                "visible": [
                                    True,
                                    False,
                                    False,
                                    False,
                                    False,
                                    False,
                                ]
                            }
                        ],
                        label="Enterovirus",
                    ),
                    dict(
                        method="update",
                        args=[
                            {
                                "visible": [
                                    False,
                                    True,
                                    False,
                                    False,
                                    False,
                                    False,
                                ]
                            }
                        ],
                        label="PMMoV",
                    ),
                    dict(
                        method="update",
                        args=[
                            {
                                "visible": [
                                    False,
                                    False,
                                    True,
                                    False,
                                    False,
                                    False,
                                ]
                            }
                        ],
                        label="Adenovirus",
                    ),
                    dict(
                        method="update",
                        args=[
                            {
                                "visible": [
                                    False,
                                    False,
                                    False,
                                    True,
                                    False,
                                    False,
                                ]
                            }
                        ],
                        label="GG2",
                    ),
                    dict(
                        method="update",
                        args=[
                            {
                                "visible": [
                                    False,
                                    False,
                                    False,
                                    False,
                                    True,
                                    False,
                                ]
                            }
                        ],
                        label="Astrovirus",
                    ),
                    dict(
                        method="update",
                        args=[
                            {
                                "visible": [
                                    False,
                                    False,
                                    False,
                                    False,
                                    False,
                                    True,
                                ]
                            }
                        ],
                        label="Sapovirus",
                    ),
                ]
            ),
            type="buttons",
            direction="right",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.1,
            xanchor="left",
            y=button_layer_1_height,
            yanchor="top",
        ),
    ]
)


# fig.update_layout(
#     updatemenus=[
#         dict(
#             type="buttons",
#             direction="right",
#             active=0,
#             x=1.1,
#             y=1.1,
#             xanchor="right",
#             yanchor="top",
#             buttons=list(
#                 [
#                     dict(
#                         label="Reselect all areas",
#                         method="update",
#                         args=[
#                             {"visible": [True]},
#                         ],
#                     ),
#                     dict(
#                         label="Deselect all areas",
#                         method="update",
#                         args=[
#                             {"visible": "legendonly"},
#                         ],
#                     ),
#                 ]
#             ),
#         )
#     ]
# )
# # Below can show figure locally in tests
# # fig.show()

# # Below prints as html
# # fig.write_html(
# #    "wastewater_combined_slu_regular.html", include_plotlyjs=True, full_html=True
# # )

# # Prints as a json file
# # fig.write_json("wastewater_combined_slu_regular.json")

# # Below can produce a static image
# # fig.write_image("wastewater_combined_graph.png")

# print(fig.to_json())
fig.show()