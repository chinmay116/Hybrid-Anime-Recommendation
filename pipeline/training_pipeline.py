from src.data_processing import DataProcessor
from src.model_training import ModelTraning
from utils.common_functions import read_yaml
from config.paths_config import *

if __name__ == "__main__":
    # Data Processing
    data_processor =  DataProcessor(ANIME_LIST_CSV, PROCESSED_DIR)
    data_processor.run()

    # Model Training
    model_training = ModelTraning(PROCESSED_DIR)
    model_training.train_model()