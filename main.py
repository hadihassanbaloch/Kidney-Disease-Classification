from kdClassifier import logger
from kdClassifier.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"====> Started {STAGE_NAME} <==== ")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"====> Finished {STAGE_NAME} <==== ")
except Exception as e:
        raise e 