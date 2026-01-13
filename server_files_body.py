import os
import re
from functools import wraps
from dataclasses import dataclass

import config
from data_handling_funcs import get_content_type_header

VALID_FILENAME_REGEX = re.compile(r'^[\w\-. ]+$')

@dataclass
class ResponseData:
    body: bytes
    body_type_header: dict
    code: int

    def __str__(self):
        return f"code: {self.code} headers: {self.body_type_header} body length: {len(self.body)}"

def verify_path(func):
    @wraps(func)
    def wrapper(file_path: str, *args, **kwargs):
        base_path = os.path.abspath("./" + config.config.response.path_to_http_dir)
        requested_path = os.path.abspath(os.path.join(base_path, file_path))

        if not requested_path.startswith(base_path):
            return get_internal_error_body()

        if not VALID_FILENAME_REGEX.match(os.path.basename(requested_path)):
            return get_internal_error_body()

        return func(file_path, *args, **kwargs)
    return wrapper

@verify_path
def get_specific_file_body(file_path: str) -> ResponseData | None:
    path = "./" + config.config.response.path_to_http_dir + file_path
    if os.path.isfile(path):
        with open(path, 'rb') as f:
            file_body = f.read()
        return ResponseData(file_body, get_content_type_header(file_path), 200)
    else:
        return get_not_found_body()


def get_default_file_body() -> ResponseData | None:
    for file in config.config.response.default_files:
        file_path = "./" + config.config.response.path_to_http_dir + file
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                file_body = f.read()
            return ResponseData(file_body, get_content_type_header(file), 200)
    return get_not_found_body()

def get_not_found_body() -> ResponseData:
    path = "./" + config.config.response.path_to_http_dir + config.config.response.not_found_file
    if os.path.isfile(path):
        with open(path, 'rb') as f:
            file_body = f.read()
        return ResponseData(file_body, get_content_type_header(config.config.response.not_found_file), 404)
    else:
        return ResponseData(b"<h1>404 Not Found</h1>", {"Content-Type":"text/html; charset=utf-8"}, 404)

def get_internal_error_body() -> ResponseData:
    path = "./" + config.config.response.path_to_http_dir + config.config.response.internal_error_file
    if os.path.isfile(path):
        with open(path, 'rb') as f:
            file_body = f.read()
        return ResponseData(file_body, get_content_type_header(config.config.response.internal_error_file), 500)
    else:
        return ResponseData(b"<h1>500 Internal Server Error</hjson>", {"Content-Type":"text/html; charset=utf-8"}, 500)

def get_bad_request_body() -> ResponseData:
    path = "./" + config.config.response.path_to_http_dir + config.config.response.bad_request_file
    if os.path.isfile(path):
        with open(path, 'rb') as f:
            file_body = f.read()
        return ResponseData(file_body, get_content_type_header(config.config.response.bad_request_file), 400)
    else:
        return ResponseData(b"<h1>400 Bad Request</h1>", {"Content-Type":"text/html; charset=utf-8"}, 400)