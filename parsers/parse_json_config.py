import json
import logging

logger = logging.getLogger(__name__)

def parse_json_config_file(path: str) -> dict | None:
    try:
        with open(path, 'r') as file:
            json_string = file.read()
        data = json.loads(json_string)

        return data
    except Exception as e:
        logger.error(f"Error reading or parsing JSON config file: {e}")
        return None
