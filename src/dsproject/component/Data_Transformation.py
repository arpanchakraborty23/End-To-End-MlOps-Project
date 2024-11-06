import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler,OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from src.dsproject.utils.utils import save_obj
from src.dsproject.entity.config_entity import DataTransformationConfig
from src.dsproject import logging

class DataTransformation:
   def __init__(self,config:DataTransformationConfig) -> None:
         self.config=config
   def get_preprocess_obj(self):
      try:
         num_col=['ssc_percentage', 'hsc_percentage', 'degree_percentage','emp_test_percentage', 'mba_percent']
         cate_cols=['gender', 'ssc_board', 'hsc_board', 'hsc_subject', 'undergrad_degree','work_experience', 'specialisation']
         gender_cate = ['M', 'F']
         ssc_board_cate = ['Central', 'Others']
         hsc_board_cate = ['Others', 'Central']
         hsc_subject_cate = ['Commerce', 'Science', 'Arts']
         undergrad_degree_cate = ['Comm&Mgmt', 'Sci&Tech', 'Others']
         work_experience_cate = ['No', 'Yes']
         specialisation_cate = ['Mkt&Fin', 'Mkt&HR']

         num_col_pipline=Pipeline(
				steps=[
					('Impute',SimpleImputer(strategy='mean')),
					('scaling',RobustScaler())
				]
			)
         
         cate_cols_pipline = Pipeline(
				steps=[
					('Impute', SimpleImputer(strategy='most_frequent')),
					('encoding', OneHotEncoder(categories=[
						gender_cate, ssc_board_cate, hsc_board_cate, hsc_subject_cate,
						undergrad_degree_cate, work_experience_cate, specialisation_cate
					], handle_unknown='ignore'))
				]
			)
         
         preprocess=ColumnTransformer([
				('num_col_pipline',num_col_pipline,num_col),
				('cate_cols_pipline',cate_cols_pipline,cate_cols)
			])
         
         logging.info('Data transformation preprocess obj created')

         return preprocess
      except Exception as e:
         logging.info(f'Error in Transformation preprocess obj: {str(e)}')
         raise e
   def transforming_data(self):
      try:
         data=pd.read_csv(self.config.unzip_dir)

         print(data.head())

         logging.info('data retrive successfully')

         x=data.drop(self.config.target_col,axis=1)
         y=data[self.config.target_col]

         y=y.map({'Placed':1,'Not Placed':0})

         x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.26,random_state=50)

         logging.info('y_train',y_train.head())

         preprocess_obj=self.get_preprocess_obj()

         x_train=preprocess_obj.fit_transform(x_train)
         x_test=preprocess_obj.transform(x_test)


         logging.info('data preprocess completed')

         train_arr=np.c_[x_train,np.array(y_train)]
         test_arr=np.c_[x_test,np.array(y_test)]

         np.save(self.config.train_arr,train_arr)

      
         np.save(self.config.test_arr,test_arr)
         logging.info('preprocess data save completed')

         save_obj(
                            file_path=self.config.preprocess_obj,
                            obj=preprocess_obj
			)
         logging.info('preprocess object save completed')

         return (
                train_arr,
                test_arr
               )
      except Exception as e:
         logging.info(f'Error in Data Transformation : {str(e)}')
         raise e
          