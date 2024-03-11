import os
import sys
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from src.exception import CustomException
from src.logger import logging

from src.components.data_transformation import DataTransformation, DataTransformationConfig

class DataIngestionConfig:
    def __init__(self) -> None:
        self.train_data_path = os.path.join("artifacts", "train.csv")
        self.test_data_path = os.path.join("artifacts", "test.csv")
        self.raw_data_path = os.path.join("artifacts", "data.csv")


class DataIngestion:
    def __init__(self) -> None:
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        """
        Function to ingest data into the pipeline.
         - Train test split

         Args:
          - None
        
        Returns:
         - train_data_path: str 
         - test_data_path: str 
        """
        try:
            df = pd.read_csv("notebook\data\stud.csv")
            logging.info("Read the dataset as dataframe")

            os.makedirs(
                os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True
            )

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(
                self.ingestion_config.train_data_path, index=False, header=True
            )

            test_set.to_csv(
                self.ingestion_config.test_data_path, index=False, header=True
            )

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()

    data_transformation_obj = DataTransformation()
    data_transformation_obj.initiate_data_transformation(train_path=train_data_path, test_path=test_data_path)
