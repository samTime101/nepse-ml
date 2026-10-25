# eeuta template matra ho, for pipeline

from info.dimension import dimension
from info.null import null
from info.duplicates import duplcates

class AIML:
    def __init__(self, dataset: str):
        self.dataset = dataset
        
    def info(self):
        null_info = null(self.dataset)
        duplicates_info = duplcates(self.dataset)
        dimension_info = dimension(self.dataset)
        
        print(null_info)
        print(duplicates_info)
        print(dimension_info)


aiml = AIML("DATA")
aiml.info()