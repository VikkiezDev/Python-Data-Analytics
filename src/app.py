import pandas as pd
import dash
import dash_bootstrap_components as dbc
from dash import dcc, Input, Output, html
import plotly.express as px

df = pd.read_csv('/home/vignesh-nadar/Desktop/sixtyDays/sprint2/Project1/data/ds_salaries.csv')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("My Dashboard"), width = 15, className= "text-center my-5")
    ])
])

if __name__ == "__main__":
    app.run_server(debug=True)
