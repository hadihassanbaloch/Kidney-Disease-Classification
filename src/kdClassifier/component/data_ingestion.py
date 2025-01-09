import os
import zipfile
import gdown
from kdClassifier import logger
from kdClassifier.utils.common import get_size
from kdClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self) ->str:
        try:
            dataset_url = self.config.source_url
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion",exist_ok=True)
            logger.info(f" Downloading data from {dataset_url} into file {zip_download_dir}")
            
            file_id = dataset_url.split('/')[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id, zip_download_dir)
            logger.info(f"Downloaded the dataset from {dataset_url} into {zip_download_dir}")
            
        except Exception as e:
            raise e
    def extract_zip(self):
        try:
            unzip_path = self.config.unzip_file
            os.makedirs(unzip_path, exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
        except Exception as e:
            raise e