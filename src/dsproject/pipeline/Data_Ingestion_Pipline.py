import os,sys
from src.dsproject import logging
from src.dsproject.config.config_manager import ConfigManager
from src.dsproject.component.Data_Ingestion import DataIngestion

class DataIngestionTrainPipline:
    def __init__(self) -> None:
       pass

    def IngestionPipline(self):
        
        try:
            config=ConfigManager()
            data_ingestion_config=config.get_data_ingestion_config()
            data_ingestion=DataIngestion(config=data_ingestion_config)
            data_ingestion.download_data()
            data_ingestion.extract_data()
            
            
        except Exception as e:
            logging.info(f' Error occured {str(e)}')
            raise e
        
if __name__=='__main__':
    try:
        logging.info(f'<<<<<<<<<<<<<<<< Data Ingestion Started >>>>>>>>>>>>>>>>>')
        object=DataIngestionTrainPipline()
        object.IngestionPipline()
        logging.info(f'<<<<<<<<<<<<<<<<<<<<<<< Data Ingestion completed >>>>>>>>>>>>>>>>>>')
    except Exception as e:
            logging.info(f' Error occured {str(e)}')
            raise e