# eeuta template matra ho, for pipeline
from info.dataframe import dataframe
from info.pipeline import info
from cleaning.pipeline import standarize, missing, duplicates, invalid, ohlcviolation, sort
from cleaning.export import export_cleaned_data

DATA_DIR = "data"
CLEANED_DIR = "cleaned"


class NEPSEAI:
    def __init__(self, dataset: str, cleaned_dir: str = CLEANED_DIR):
        self.dataset = dataset
        self.cleaned_dir = cleaned_dir
        self.df = None
        self.clean_df = None

    def load(self):
        self.df = dataframe(self.dataset)
        return self.df

    def cleaning(self):
        clean_df = standarize(self.df)
        clean_df = missing(clean_df)
        clean_df = duplicates(clean_df)
        clean_df = invalid(clean_df)
        clean_df = ohlcviolation(clean_df)
        self.clean_df = sort(clean_df)
        return self.clean_df

    def save(self):
        return export_cleaned_data(self.clean_df, self.cleaned_dir)

    def run(self):
        self.load()
        info(self.df)
        self.cleaning()
        info(self.clean_df)
        self.save()


pipeline = NEPSEAI(DATA_DIR)
pipeline.run()