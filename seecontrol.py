import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
from pandas.core.frame import DataFrame
from abc import ABC
import seemodel, seeview

class ControlBase(object):

    def __init__(self, model, view) -> None:
        super().__init__()

        self.model = model
        self.view = view

        self.app = dash.Dash(__name__)
        self.app.layout = view.toTable(model.df_data)
    
    def showTable(df: DataFrame):
        pass



if __name__ == '__main__':
    app = ControlBase(seemodel.ModelBase(), seeview.ViewBase())
    app.app.run_server(debug=True)
    
