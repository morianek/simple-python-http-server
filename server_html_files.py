import os
from dataclasses import dataclass

from config import get_response_config

config = get_response_config()

def get_default_file_body():
    for file in config.default_files:
        file_path = "./" + config.path_to_http_dir + file
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding="utf-8") as f:
                file_body = f.read()
            return file_body
    return None

def get_not_found_body():
    path = "./" + config.path_to_http_dir + config.not_found_file
    if os.path.isfile(path):
        with open(path, 'r', encoding="utf-8") as f:
            file_body = f.read()
        return file_body
    else:
        return "<h1>404 Not found</h1>"
