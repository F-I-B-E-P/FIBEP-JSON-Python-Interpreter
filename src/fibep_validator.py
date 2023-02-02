import json
import time
import os
import sys
import logging
import logging.handlers as handlers
from fibep_interpreter import fibep_decode

config_dir = os.path.dirname(os.path.realpath(__file__))
config_file = os.path.join(config_dir, "test.json")
news=fibep_decode(config_file)

def load_config():
    try:
        config_dir = os.path.dirname(os.path.realpath(__file__))
        config_file = os.path.join(config_dir,'config', 'config.yaml')
        config= open(config_file, 'r')
        logging.info(f'Opening the following file: {config_file}')
       # config = yaml.safe_load(configuration)
        return config
    except Exception as exception:
        logging.critical(f"There's an error accessing your config.yml file, the error is the following: {exception}")
        print("There's no config yaml file in the program's folder, please check the logs.")
        sys.exit()

