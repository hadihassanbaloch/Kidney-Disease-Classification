from kdClassifier import logger
from kdClassifier.component.model_training import Training
from kdClassifier.config.configuration import ConfigurationManager

STAGE_NAME = 'Training Model'

class TrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()
        
        
if __name__ == '__main__':
    logger.info(f"Started {STAGE_NAME}")
    obj = TrainingPipeline()
    obj.main()
    logger.info(f"Completed {STAGE_NAME}")
    