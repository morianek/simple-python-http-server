from server_files_body import get_default_file_body, get_not_found_body, get_bad_request_body, get_specific_file_body
from html_response_builder import built_response
from parsers.html_req_parser import Request


def handle_request(request: Request) -> bytes:
    if request is None:
        file_body = get_bad_request_body()
        return built_response(code=400, body=file_body.body, headers=file_body.body_type_header)

    elif request.path == "/":
        file_body = get_default_file_body()
        return built_response(code=200, body=file_body.body, headers=file_body.body_type_header)

        # TODO zrobienie wyszukiwarki plików jeżeli nie ma default body
    elif request.path.startswith("/"):
        file_body = get_specific_file_body(request.path[1:])
        return built_response(code=200, body=file_body.body, headers=file_body.body_type_header)

    else:
        file_body = get_not_found_body()
        return built_response(code=404, body=file_body.body, headers=file_body.body_type_header)
