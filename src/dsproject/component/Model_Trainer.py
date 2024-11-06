import joblib
import numpy as np
from src.dsproject import logging
from src.dsproject.utils.utils import model_evaluatuion,save_obj
from src.dsproject.entity.config_entity import ModelTrainConfig
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report

class ModelTrainer:
    def __init__(self, config):
        self.config = config

    def initiate_model_training(self):
        try:
            # Load data
            train_array = np.load(self.config.train_arr,allow_pickle=True)
            test_array = np.load(self.config.test_arr,allow_pickle=True)
            logging.info('Array data loaded')

            # Split data into features and target
            x_train, y_train = train_array[:, :-1], train_array[:, -1]
            x_test, y_test = test_array[:, :-1], test_array[:, -1]

            # Initialize and train model
            model = RandomForestClassifier(
                n_estimators=self.config.n_estimators,
                min_samples_leaf=self.config.min_samples_leaf,
                max_depth=self.config.max_depth,
                min_samples_split=self.config.min_samples_split
            )
            model.fit(x_train, y_train)

            # Predict and calculate accuracy
            y_pred = model.predict(x_test)
            accuracy = accuracy_score(y_test, y_pred)
            print(f'{model} model accuracy: {accuracy}')

            # Save the model
            save_obj(
                file_path=self.config.model,
                obj=model
				)
            logging.info('Model saved successfully')

        except Exception as e:
            logging.info(f'Error in model training: {str(e)}')
            raise e