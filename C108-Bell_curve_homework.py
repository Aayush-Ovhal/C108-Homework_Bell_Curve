import pandas as pd
import csv
import plotly.express as px
import plotly.figure_factory as pff

df = pd.read_csv("MName vs Avg Rating.csv")

listdf = df["Avg Rating"].tolist()

fig = pff.create_distplot([listdf], ["Avg Rating"])
fig.show()


