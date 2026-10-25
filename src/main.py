# eeuta template matra ho, for pipeline
from info.dataframe import dataframe
from info.dimension import dimension
from info.null import null
from info.duplicates import duplcates

DATA_DIR = "data"

class NEPSEAI:
    def __init__(self, dataset: str):
        self.dataset = dataset
        self.df = None

    def load(self):
        self.df = dataframe(self.dataset)
        print(self.df)
        return self.df
        
    def info(self):
        null_info = null(self.df)
        duplicates_info = duplcates(self.df)
        dimension_info = dimension(self.df)
        print(null_info)
        print(duplicates_info)
        print(dimension_info)
        
    def run(self):
        self.load()
        # report = self.info()
        # return report


pipeline = NEPSEAI(DATA_DIR)
pipeline.run()