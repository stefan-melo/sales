import pandas as pd
import numpy as np
import dash
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.DataFrame(
    {
        'France': [47384, 58409, 78142],
        'Germany': [12374, 18409, 24673],
    }
)

table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)

app.layout = dbc.Container([
    dbc.Alert("Hello SEE Territory", color='success', className='p-5'),
    table
]
)


if __name__ == '__main__':
    app.run_server()
    