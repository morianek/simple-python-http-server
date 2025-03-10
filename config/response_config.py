from dataclasses import dataclass

PATH_TO_HTTP = "tests/default_html/"
DEFAULT_FILES = ["index.html", "lol.html"]
NOT_FOUND_FILE = "error_404.html"
INTERNAL_ERROR_FILE = "error_500.html"
BAD_REQUEST_FILE = "error_400.html"

@dataclass
class ResponseConfig:
    path_to_http_dir: str
    default_files: list[str]
    not_found_file: str
    internal_error_file: str
    bad_request_file: str

def get_config():
    return ResponseConfig(PATH_TO_HTTP, DEFAULT_FILES, NOT_FOUND_FILE, INTERNAL_ERROR_FILE, BAD_REQUEST_FILE)