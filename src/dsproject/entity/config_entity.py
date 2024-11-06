from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    dir: Path
    url: Path
    local_dir: Path
    unzip_dir: Path

@dataclass
class DataValidationConfig:
   dir: Path
   unzip_dir: Path
   status: str
   all_schema: dict

@dataclass
class DataTransformationConfig:
   dir: Path
   unzip_dir: Path
   train_arr: Path
   test_arr: Path
   target_col: str
   preprocess_obj: Path

@dataclass
class ModelTrainConfig:
   dir:Path
   train_arr: Path
   test_arr: Path
   model:  Path
   n_estimators: int
   max_depth: int
   min_samples_split:int
   min_samples_leaf:int