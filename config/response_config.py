from dataclasses import dataclass

@dataclass
class ResponseConfig:
    path_to_http_dir: str
    default_files: list[str]
    not_found_file: str
    internal_error_file: str
    bad_request_file: str

def get_config(config: dict | None = None) -> ResponseConfig:
    if config is None:
        raise ValueError("Config files dictionary cannot be None")

    responses_config = config.get('files', {})
    path_to_http_dir = config.get('root_directory')
    default_files = responses_config.get('dafault_pages', ['index.html'])
    not_found_file = responses_config.get('not_found_page')
    internal_error_file = responses_config.get('internal_error_page')
    bad_request_file = responses_config.get('bad_request_page')

    if path_to_http_dir is None:
        raise ValueError("root_directory must be specified in the configuration")

    return ResponseConfig(
        path_to_http_dir=path_to_http_dir,
        default_files=default_files,
        not_found_file=not_found_file,
        internal_error_file=internal_error_file,
        bad_request_file=bad_request_file
    )