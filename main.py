from kdClassifier import logger
from kdClassifier.pipeline.base_model_pipeline import PrepareBaseModelPipeline
from kdClassifier.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from kdClassifier.pipeline.training_pipeline import TrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"====> Started {STAGE_NAME} <==== ")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"====> Finished {STAGE_NAME} <==== ")
except Exception as e:
        raise e 
    
STAGE_NAME = "Prepare Base Model"

try:
    logger.info(f'Starting {STAGE_NAME} =====>')
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(f'Finished {STAGE_NAME} =====>')
except Exception as e:
    raise e

STAGE_NAME = "Training Model"

try:
    logger.info(f"Started {STAGE_NAME}")
    obj = TrainingPipeline()
    obj.main()
    logger.info(f"Completed {STAGE_NAME}")
    
except Exception as e:
    raise e