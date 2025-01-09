from kdClassifier.config.configuration import ConfigurationManager
from kdClassifier.component.data_ingestion import DataIngestion
from kdClassifier import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config =ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_zip()
        
        
if __name__ == '__main__':
    try:
        logger.info(f"====> Started {STAGE_NAME} <==== ")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"====> Finished {STAGE_NAME} <==== ")
    except Exception as e:
        raise e    