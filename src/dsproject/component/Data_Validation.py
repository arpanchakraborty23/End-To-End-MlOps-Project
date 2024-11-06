import os
import pandas as pd
from src.dsproject import logging
from src.dsproject.entity.config_entity import DataValidationConfig

class DataValidation:
   def __init__(self,config:DataValidationConfig) -> None:
      self.config=config
      
   def validate_all_columns(self) -> bool:
      try:
         validation_status=None
         data_path=self.config.unzip_dir
         print(data_path)
         data=pd.read_csv(self.config.unzip_dir)
      
         all_cols=list(data.columns)
         print(all_cols)
         all_schema=self.config.all_schema.keys()
         print(f'all schema: {all_schema}')
         for col in all_cols:
            if col not in all_schema:
               validation_status=False
               with open(self.config.status,'w') as f:
                  f.write(f' Validation Status : {validation_status}')
            else:
               validation_status= True
               with open(self.config.status,'w') as f:
                  f.write(f' Validation Status : {validation_status}')
                  
         return validation_status
      except Exception as e:
         logging.info(f'error in validation {str(e)}')
         raise e