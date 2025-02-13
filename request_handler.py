from get_server_files_body import get_default_file_body, get_not_found_body, get_specific_file_body
from html_response_builder import built_response

def handle_request(request):
    if request is None:
        return built_response(code=400, body="<h1>400 bad request</h1>")

    elif request.path == "/":
        return built_response(code = 200, body = get_default_file_body())

        # TODO zrobienie wyszukiwarki plików jeżeli nie ma default body
    elif request.path == "/test":
        return built_response(code = 200, body = "<h1>test<h1>")

    elif request.path.startswith("/"):
        return built_response(code=200, body=get_specific_file_body(request.path[1:]))

    else:
        return built_response(code = 404, body = get_not_found_body())
