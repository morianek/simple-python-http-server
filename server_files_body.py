import os
import re
from functools import wraps

from config import get_response_config

config = get_response_config()

VALID_FILENAME_REGEX = re.compile(r'^[\w\-. ]+$')

def verify_path(func):
    @wraps(func)
    def wrapper(file_path, *args, **kwargs):
        base_path = os.path.abspath("./" + config.path_to_http_dir)
        requested_path = os.path.abspath(os.path.join(base_path, file_path))

        if not requested_path.startswith(base_path):
            return get_internal_error_body()

        if not VALID_FILENAME_REGEX.match(os.path.basename(requested_path)):
            return get_internal_error_body()

        return func(file_path, *args, **kwargs)
    return wrapper

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

@verify_path
def get_specific_file_body(file_path):
    path = "./" + config.path_to_http_dir + file_path
    if os.path.isfile(path):
        with open(path, 'r', encoding="utf-8") as f:
            file_body = f.read()
        return file_body
    else:
        return get_not_found_body()

def get_internal_error_body():
    path = "./" + config.path_to_http_dir + config.internal_error_file
    if os.path.isfile(path):
        with open(path, 'r', encoding="utf-8") as f:
            file_body = f.read()
        return file_body
    else:
        return "<h1>500 Internal Server Error</h1>"