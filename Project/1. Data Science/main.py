from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingsPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initial_data_ingestion()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=================x")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_validation = DataValidationTrainingsPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=================x")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=================x")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
    model_training = ModelTrainerTrainingPipeline()
    model_training.initiate_model_training()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=================x")

except Exception as e:
    logger.exception(e)
    raise e