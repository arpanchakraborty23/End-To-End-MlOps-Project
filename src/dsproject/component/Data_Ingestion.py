import os
import requests
import zipfile
from src.dsproject.entity.config_entity import DataIngestionConfig
from src.dsproject import logging

class DataIngestion:
    def __init__(self, config=DataIngestionConfig) -> None:
        """
        Initializes the DataIngestion class with configuration settings.
        """
        self.config = config
        

    def download_data(self):
        """
        Downloads data from the specified URL in the config and saves it locally.
        """
        try:
            data_url = self.config.url
            download_file_path = os.path.join(self.config.local_dir, 'data.zip')
            
            # Create a local data folder if it doesn't exist
            os.makedirs(self.config.local_dir, exist_ok=True)
            
            # Download the data
            response = requests.get(data_url)
            if response.status_code == 200:
                logging.info('Data download completed')
            else:
                logging.error('Failed to download data: Status code {}'.format(response.status_code))
                return

            # Save data to file
            with open(download_file_path, 'wb') as f:
                f.write(response.content)
            logging.info("Data saved successfully at {}".format(download_file_path))
        
        except Exception as e:
            logging.error('Error in data ingestion during download: {}'.format(str(e)))
            raise e

    def extract_data(self):
        """
        Extracts the downloaded ZIP data file into the specified directory.
        """
        try:
            download_file_path = os.path.join(self.config.local_dir, 'data.zip')
            unzip_dir = self.config.unzip_dir

            # Create an unzip directory if it doesn't exist
            os.makedirs(unzip_dir, exist_ok=True)

            # Unzip the downloaded file
            with zipfile.ZipFile(download_file_path, 'r') as zip_ref:
                zip_ref.extractall(unzip_dir)
            logging.info('Data unzip completed in {}'.format(unzip_dir))

            

        except zipfile.BadZipFile:
            logging.error('Failed to unzip file: BadZipFile error')
            raise
        except Exception as e:
            logging.error('Error in data ingestion during extraction: {}'.format(str(e)))
            raise e
