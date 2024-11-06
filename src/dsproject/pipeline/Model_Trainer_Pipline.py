from src.dsproject.config.config_manager import ConfigManager
from src.dsproject.component.Model_Trainer import ModelTrainer
from src.dsproject import logging

class ModelTrainPipline:
    def __init__(self) -> None:
        pass
    def ModelPipline(self):
        try:
            config=ConfigManager()
            model_trainer_config=config.get_model_trainer_config()

            model_trainer=ModelTrainer(config=model_trainer_config)

            model_trainer.initiate_model_training()
            

        except Exception as e:
                logging.info('error in data Model',str(e))
                raise e
        
if __name__=='__main__':
    try:
        logging.info(f'<<<<<<<<<<<<<<<<  Model Train Started >>>>>>>>>>>>>>>>>')
        object=ModelTrainPipline()
        object.ModelPipline()
        logging.info(f'<<<<<<<<<<<<<<<< Model Train completed >>>>>>>>>>>>>>>>>>')
    except Exception as e:
            logging.info(f' Error occured {str(e)}')
            raise e