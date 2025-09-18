import os
import re
from functools import wraps
from dataclasses import dataclass

from config import get_response_config
from data_handling_funcs import get_content_type_header

config = get_response_config()

VALID_FILENAME_REGEX = re.compile(r'^[\w\-. ]+$')

@dataclass
class FileBody:
    body: bytes
    body_type_header: dict

def verify_path(func):
    @wraps(func)
    def wrapper(file_path: str, *args, **kwargs):
        base_path = os.path.abspath("./" + config.path_to_http_dir)
        requested_path = os.path.abspath(os.path.join(base_path, file_path))

        if not requested_path.startswith(base_path):
            return get_internal_error_body()

        if not VALID_FILENAME_REGEX.match(os.path.basename(requested_path)):
            return get_internal_error_body()

        return func(file_path, *args, **kwargs)
    return wrapper

@verify_path
def get_specific_file_body(file_path: str) -> FileBody | None:
    path = "./" + config.path_to_http_dir + file_path
    if os.path.isfile(path):
        with open(path, 'rb') as f:
            file_body = f.read()

        return FileBody(file_body, get_content_type_header(file_path))
    else:
        return None


def get_default_file_body() -> FileBody | None:
    for file in config.default_files:
        file_path = "./" + config.path_to_http_dir + file
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                file_body = f.read()
            return FileBody(file_body, get_content_type_header(file))
    return None

def get_not_found_body() -> FileBody:
    path = "./" + config.path_to_http_dir + config.not_found_file
    if os.path.isfile(path):
        with open(path, 'rb') as f:
            file_body = f.read()
        return FileBody(file_body, get_content_type_header(config.not_found_file))
    else:
        return FileBody(b"<h1>404 Not Found</h1>", {"Content-Type":"text/html; charset=utf-8"})

def get_internal_error_body() -> FileBody:
    path = "./" + config.path_to_http_dir + config.internal_error_file
    if os.path.isfile(path):
        with open(path, 'rb') as f:
            file_body = f.read()
        return FileBody(file_body, get_content_type_header(config.internal_error_file))
    else:
        return FileBody(b"<h1>500 Internal Server Error</hjson>", {"Content-Type":"text/html; charset=utf-8"})

def get_bad_request_body() -> FileBody:
    path = "./" + config.path_to_http_dir + config.bad_request_file
    if os.path.isfile(path):
        with open(path, 'rb') as f:
            file_body = f.read()
        return FileBody(file_body, get_content_type_header(config.bad_request_file))
    else:
        return FileBody(b"<h1>400 Bad Request</h1>", {"Content-Type":"text/html; charset=utf-8"})