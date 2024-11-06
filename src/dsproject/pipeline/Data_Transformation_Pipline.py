import os,sys
from src.dsproject import logging
from src.dsproject.config.config_manager import ConfigManager
from src.dsproject.component.Data_Transformation import DataTransformation


class DataTransformationTrainPipline:
    def __init__(self) -> None:
       pass

    def TransformationPipline(self):
        
        try:
            config=ConfigManager()
            data_transformation_config=config.get_transformation_config()
            data_transformation=DataTransformation(config=data_transformation_config)
            data_transformation.transforming_data()
            
            
            
        except Exception as e:
            logging.info(f' Error occured {str(e)}')
            raise e
        
if __name__=='__main__':
    try:
        logging.info(f'<<<<<<<<<<<<<<<< Data Transformation Started >>>>>>>>>>>>>>>>>')
        object=DataTransformationTrainPipline()
        object.TransformationPipline()
        logging.info(f'<<<<<<<<<<<<<<<<<<<<<<< Data Transformation completed >>>>>>>>>>>>>>>>>>')
    except Exception as e:
            logging.info(f' Error occured {str(e)}')
            raise e