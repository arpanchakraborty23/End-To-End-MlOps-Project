import os,sys
import yaml
from src.dsproject import logging

from src.dsproject.utils.utils import read_yaml,create_dir
from src.dsproject.constants.yaml_path import *
from src.dsproject.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainConfig

class ConfigManager:
    def __init__(self,config_file_path=Config_file_path,prams_file_path=Param_file_path,schema_file_path=Schema_file_path) -> None:
        self.config=read_yaml(config_file_path)
        self.params=read_yaml(prams_file_path)
        self.schema=read_yaml(schema_file_path)

        create_dir([self.config.artifacts_root])
    
    def get_data_ingestion_config(self):
        try:
            config = self.config.Data_Ingestion
            data_ingestion_config = DataIngestionConfig(
                dir=config.dir,
                url=config.url,
                local_dir=config.local_dir,
                unzip_dir=config.unzip_dir
            )
            return data_ingestion_config
        except Exception as e:
            logging.info('error in data ingestion config', str(e))
            raise e
        
    def get_data_val_config(self):
      try:
         config=self.config.Data_Validation
         create_dir([config.dir])
         data_val_config=DataValidationConfig(
               dir=config.dir,
               unzip_dir=config.unzip_dir,
               status=config.status,
               all_schema=self.schema.COLUMNNS
			)
         return data_val_config
      except Exception as e:
         logging.info(f'error in validation config {str(e)}')
         raise e
    
    def get_transformation_config(self) -> DataTransformationConfig:
      try:
            config=self.config.Data_Transformation
            create_dir([config.dir])

            transformation_config=DataTransformationConfig(
                dir=config.dir,
                unzip_dir=config.unzip_dir,
                train_arr=config.train_arr,
                test_arr=config.test_arr,
                target_col=self.schema.TARGET_COLUMN,
                preprocess_obj=config.preprocess_obj
				)	
            
            return transformation_config
      except Exception as e:
         logging.info(f'Error in Transformation config: {str(e)}')
         raise e
    
    def get_model_trainer_config(self):
      try:
         config=self.config.Model_Trainer
         params=self.params.RandomForestClassifier
         create_dir([config.dir])
         model_train_config=ModelTrainConfig(
               dir=config.dir,
               train_arr=config.train_arr,
               test_arr=config.test_arr,
               model=config.model,
               n_estimators=params.n_estimators,
               max_depth=params.max_depth,
               min_samples_leaf=params.min_samples_leaf,
               min_samples_split=params.min_samples_split
			)
         return model_train_config
      except Exception as e:
         logging.info(f'error in MODEL TRAIN config {str(e)}')
         raise e