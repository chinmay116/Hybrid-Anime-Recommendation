import os
import pandas as pd
from google.cloud import storage
from src.custom_exception import CustomException
from src.logger import get_logger
from config.paths_config import *
from utils.common_functions import read_yaml

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self, config):
        self.config = config["data_ingestion"]
        self.bucket_name = self.config["bucket_name"]
        self.file_names = self.config["bucket_file_names"]

        os.makedirs(RAW_DIR, exist_ok=True)

        logger.info(f"Data Ingestion started with {self.bucket_name} and file is {self.file_names}")

    def download_csv_from_gcp(self):
        try:
            logger.info(f"Connecting to bucket: '{self.bucket_name}'")  # Log quotes to catch leading/trailing spaces
            client = storage.Client()
            bucket = client.bucket(self.bucket_name)

            for file_name in self.file_names:
                file_path = os.path.join(RAW_DIR, file_name)

                if file_name == "animelist.csv":
                    blob = bucket.blob(file_name)
                    blob.download_to_filename(file_path)

                    data = pd.read_csv(file_path, nrows=5000000)
                    data.to_csv(file_path, index=False)

                    logger.info("Large File detected Downloading only 5M rows")
                else:
                    blob = bucket.blob(file_name)
                    blob.download_to_filename(file_path)

                    logger.info("Downloading Smaller files i.e. anime and anime_with_synopsis")

        except Exception as e:
            logger.error(f"Error while downloading the csv file:")
            raise CustomException("Failed to download csv file", e)
        
    def run(self):
        try:
            logger.info("Starting Data Ingestion Process")

            self.download_csv_from_gcp()

            logger.info("Data Ingestion Completed Successfully")

        except CustomException as ce:
            logger.error(f"Custom Exception : {str(ce)}")

        finally:
            logger.info("Data Ingestion Completed")

if __name__ == "__main__":
    data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()