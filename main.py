from src.mlProject import logger
from src.mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.mlProject.pipeline.stage_04_train_model import ModelTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f"Running {STAGE_NAME} !")
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()
    logger.info(f"{STAGE_NAME} completed !")
except Exception as e:
    logger.error(e)
    raise e

STAGE_NAME = "Data Validation stage"

try:
    logger.info(f"Running {STAGE_NAME} !")
    pipeline = DataValidationTrainingPipeline()
    pipeline.main()
    logger.info(f"{STAGE_NAME} completed !")
except Exception as e:
    logger.error(e)
    raise e

STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f"Running {STAGE_NAME} !")
    pipeline = DataTransformationTrainingPipeline()
    pipeline.main()
    logger.info(f"{STAGE_NAME} completed !")
except Exception as e:
    logger.error(e)
    raise e

STAGE_NAME = "Model Training stage"

try:
    logger.info(f"Running {STAGE_NAME} !")
    pipeline = ModelTrainingPipeline()
    pipeline.main()
    logger.info(f"{STAGE_NAME} completed !")
except Exception as e:
    logger.error(e)
    raise e