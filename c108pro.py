import plotly.figure_factory as px
import csv
import pandas as pd

df=pd.read_csv("amazon.csv")

fig=px.create_distplot([df["Avg Rating"].tolist()], ["Avg Rating"])
fig.show()