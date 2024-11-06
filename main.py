from src.ds import logging
from src.ds.pipeline.Data_Ingestion_Pipline import DataIngestionTrainPipline
from src.ds.pipeline.Data_Validation_Pipline import DataValidationTrainPipline
from src.ds.pipeline.Data_Transformation_Pipline import DataTransformationTrainPipline

logging.info('Welcome to Data Science Project')

# Data Ingestion
logging.info('<=========================== Traning Pipline Started =============================>')

logging.info('************************* Data Ingestion **************************')
ingestion_obj=DataIngestionTrainPipline()
ingestion_obj.IngestionPipline()
logging.info('************************* Data Ingestion Completed **************************')


# Data Validation
logging.info('************************* Data Validation **************************')

validation_obj=DataValidationTrainPipline()
validation_obj.ValidationPipline()

logging.info('************************* Data Validation Completed **************************')

# Data Transformation
logging.info('************************* Data Transformation **************************')

transform_obj=DataTransformationTrainPipline()
transform_obj.TransformationPipline()

logging.info('************************* Data Transformation Completed **************************')