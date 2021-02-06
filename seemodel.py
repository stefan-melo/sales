from os import path, listdir
import configparser
import pandas as pd
from pandas.core.frame import DataFrame


def join_path(dir, files):
        """
        Create full path strings: "dir" + [files].\n\n
        dir:    static path string\n
        files:  list of file name strings
        """
        complete = []
        for f in files:
            complete.append(path.join(dir, f))
        return complete


class ModelBase(object):

    def __init__(self) -> None:
        super().__init__()

        config = configparser.ConfigParser()
        config.read('config.ini')
        self.datafolder = config['SOURCE']['DataFolder']
        self.targetfile = config['SOURCE']['TargetFile']
        self.df_data = self.readData(self.datafolder, 'folder')
        self.df_targets = self.readData(self.targetfolder, 'file')


    def readData(self, source, type):

        """
        Read data from SOURCE folder or file into DataFrame
        (CSV from folder, file Excel for the moment)
        """

        if type == 'folder':
            files = [f for f in listdir(source) if f.endswith('.csv')] 
            file_paths = join_path(source, files)
            df = pd.concat(map(pd.read_csv, file_paths))
        else:
            df = pd.read_excel(self.targetfile)
        return df

    def getMonths(self, col):

        """
        Get month numbers.\n
        col: Column 'name' with date
        """
        
        months = list(pd.to_datetime(self.df_targets[col].sort_values(ascending=True)))
        return months

    def getFYMonths(self, m: list, fy_start: int):
        """
        Get month numbers based on FY start month

        """
        delta_if_true = fy_start - 2 * fy_start + 1
        delta_if_false = fy_start - 2 + fy_start + 13
        fy_months = []
        for x in m:
            if x >= fy_start and x <= 12:
                fy_months.append(x - abs(delta_if_true))
            else: 
                fy_months.append(x + abs(delta_if_false))
        return fy_months

    def dropNaN(self, df):
        """
        Drop NaN values in DataFrame or Series
        """

        if isinstance(df, (pd.DataFrame, pd.Series)):
            df = df.dropna()
        else:
            pass
        return df

    def getBusinessType(self):

        pass
