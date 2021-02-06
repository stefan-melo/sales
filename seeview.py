import dash
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

class ViewBase(object):

    def __init__(self) -> None:
        super().__init__()

    # Table
    
    def toTable(self, df: DataFrame):
        """
        Transfer DataFrame to HTML tbale
        """
        return html.Table(
            #Header
            [html.Tr([
                html.Th(col) 
                for col in df.columns
            ])] +

            #Body
            [html.Tr([
                html.Td(df.iloc[i][col])
                for col in df.columns
                for i in range(0, len(df))
            ])]
        )





""" money = Format(symbol=Symbol.yes, symbol_suffix=' €', precision=2, scheme=Scheme.fixed, group_delimiter=' ', group=Group.yes, groups=[3])
percentage = FormatTemplate.percentage(2)

cols = []
for i in df.columns:
    if ('Revenue' in i) or ('Target' in i):
        cols.append(dict(id=i, name=i, type='numeric', format=money))
    elif 'Percent' in i:
        cols.append(dict(id=i, name=i, type='numeric', format=percentage))
    else:
        cols.append(dict(id=i, name=i))


table = DataTable(
    id='table',
    columns=cols,
    data=df.to_dict('records'),
    cell_selectable=False,
    style_cell={'font-family': 'Helvetica, sans-serif'}
)

fig = {
        'data': [
            {'x': df['Month'], 'y': df['Revenue Amount Cum'], 'text': df['Revenue Amount Cum'], 'textposition': 'auto', 'type': 'bar', 'name': 'Revenue Cum'},
            {'x': df['Month'], 'y': df['Target Cum'], 'text': df['Target Cum'], 'textposition': 'auto', 'type': 'bar', 'name': 'Target Cum'}            
        ]
    }

chart = dcc.Graph(
    figure=fig,
    id='Sales-Chart',
    config={'displayModeBar': False}
    )

# Page
app.layout = dbc.Container([
    html.H1(children='Region Sales Analysis'),
    html.Div([
        html.Label(children='Business Type: '),
        dcc.Dropdown(
            id='Business-Filter',
            options=[
                {'label': b_type, 'value': b_type}
                for b_type in np.sort(df['Business Type'].unique())
            ],
            placeholder='Select Business Type',
            style={'width': '50%'}
        )
    ],
    className='filters',
    style={'margin-bottom': '20px'}),
    table,
    chart
    ]
) """