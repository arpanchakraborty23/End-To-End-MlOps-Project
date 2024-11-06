from src.dsproject.config.config_manager import ConfigManager
from src.dsproject.entity.config_entity import DataValidationConfig
from src.dsproject.component.Data_Validation import DataValidation
from src.dsproject import logging

class DataValidationTrainPipline:
    def __init__(self) -> None:
        pass
    def ValidationPipline(self):
        try:
            config=ConfigManager()
            data_validation_config=config.get_data_val_config()

            data_validation=DataValidation(config=data_validation_config)

            data_validation.validate_all_columns()
            

        except Exception as e:
                logging.info('error in data validation',str(e))
                raise e
        
if __name__=='__main__':
    try:
        logging.info(f'<<<<<<<<<<<<<<<< Data Validation Started >>>>>>>>>>>>>>>>>')
        object=DataValidationTrainPipline()
        object.ValidationPipline()
        logging.info(f'<<<<<<<<<<<<<<<< Data Validation completed >>>>>>>>>>>>>>>>>>')
    except Exception as e:
            logging.info(f' Error occured {str(e)}')
            raise e