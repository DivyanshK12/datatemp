import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pickle
import pandas as pd
import plotly.express as px

app = dash.Dash(
    __name__,
    requests_pathname_prefix='/app1/',
    external_stylesheets=[dbc.themes.DARKLY]
)
data = []
with open('picklefile','rb') as pf:
    data = pickle.load(pf)
df = pd.DataFrame(data[1:11],columns = data[0])
dfint = df.copy()
for column in dfint.columns:
    dfint[column] = pd.to_numeric(dfint[column],errors = 'coerce')
dfint.dropna(axis=1, how='all',inplace = True)

df2 = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df2, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    dbc.Container(
    dbc.Alert("Hello Bootstrap!", color="success"),
    className="p-5",
)
])