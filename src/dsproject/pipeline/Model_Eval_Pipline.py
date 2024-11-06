import os,sys
from src.dsproject import logging
from src.dsproject.config.config_manager import ConfigManager
from src.dsproject.component.Model_Eval import ModelEval


class ModelEvalTrainPipline:
    def __init__(self) -> None:
       pass

    def EvalPipline(self):
        
        try:
            config=ConfigManager()
            model_eval_config=config.get_model_eval_config()
            model_eval=ModelEval(config=model_eval_config)
            model_eval.initiating_model_eval()
            
            
            
        except Exception as e:
            logging.info(f' Error occured {str(e)}')
            raise e
        
if __name__=='__main__':
    try:
        logging.info(f'<<<<<<<<<<<<<<<< Model Eval Started >>>>>>>>>>>>>>>>>')
        object=ModelEvalTrainPipline()
        object.EvalPipline()
        logging.info(f'<<<<<<<<<<<<<<<<<<<<<<< Model Eval completed >>>>>>>>>>>>>>>>>>')
    except Exception as e:
            logging.info(f' Error occured {str(e)}')
            raise e