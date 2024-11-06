import logging
import os
from pathlib import Path

project_name = 'dsproject'

list_of_files = [
    '.github/workflows/.gitkeep',
    'experiment/experiment.ipynb',  # Corrected typo here
    'data/data.csv',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/component/__init__.py',
    f'src/{project_name}/pipeline/__init__.py',  # Corrected typo in 'pipeline'
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/exception/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'schema.yaml',
    'Dockerfile',
    'setup.py',
    'requirements.txt',
    'templates/index.html',
    'app.py'
]

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    if file_dir != '':
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f'Creating directory {file_dir} for file {file_name}')

    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        with open(file_path, 'w') as f:
            pass
        logging.info(f'Creating empty file {file_path}')
    else:
        logging.info(f'{file_name} already exists')
