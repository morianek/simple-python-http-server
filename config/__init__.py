import logging

config = None

from parsers import parse_json_config_file

from .server_config import get_config as get_server_config
from .response_config import get_config as get_response_config
from .logging_config import setup_logging

class Config:
    def __init__(self, server_config, response_config):
        self.server = server_config
        self.response = response_config

def setup(config_file_path: str):
    global config

    json_config = parse_json_config_file(config_file_path)
    if json_config is None:
        logging.exception('Could not parse config file')
        raise Exception('Could not parse config file')
    try:
        setup_logging(json_config)
        config = Config(
            server_config=get_server_config(json_config),
            response_config=get_response_config(json_config)
        )
    except Exception as e:
        logging.exception(f'Error setting up configuration: {e}')
        raise e
    logging.info('Configuration successfully loaded')