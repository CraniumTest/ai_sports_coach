import pandas as pd

class DataIntegrator:
    def __init__(self):
        self.data_sources = []

    def add_data_source(self, data_df):
        self.data_sources.append(data_df)

    def consolidate_data(self):
        return pd.concat(self.data_sources, ignore_index=True)
