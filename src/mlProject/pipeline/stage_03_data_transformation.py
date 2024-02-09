from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.data_transformation import DataTransformation

STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.train_test_spliting()
        except Exception as e:
            raise e
