from server_files_body import get_default_file_body, get_not_found_body, get_bad_request_body, get_specific_file_body
from html_response_builder import built_response
from parsers import Request
import logging

logger = logging.getLogger(__name__)

def handle_request(request: Request) -> bytes:
    response_data = None

    if request is None:
        response_data = get_bad_request_body()

    elif request.path == "/":
        response_data = get_default_file_body()

        # TODO zrobienie wyszukiwarki plików jeżeli nie ma default body
    elif request.path.startswith("/"):
        response_data = get_specific_file_body(request.path[1:])

    else:
        response_data = get_not_found_body()

    logger.debug(response_data)
    return built_response(code=response_data.code, body=response_data.body, headers=response_data.body_type_header)

