from ChickenDiseaseClassification import logger
from ChickenDiseaseClassification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} Started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> {STAGE_NAME} Completed <<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e   