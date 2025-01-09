from kdClassifier import logger
from kdClassifier.component.prepare_base_model import PrepareBaseModel
from kdClassifier.config.configuration import ConfigurationManager

STAGE_NAME = "Prepare Base Model"

class PrepareBaseModelPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
        
if __name__ == '__main__':
    try:
        logger.info(f'Starting {STAGE_NAME} =====>')
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f'Finished {STAGE_NAME} =====>')
    except Exception as e:
        raise e