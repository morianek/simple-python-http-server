from server_html_files import get_default_file_body, get_not_found_body
from html_response_builder import built_response

def handle_request(request):
    if request.path == "/":
        return built_response(code = 200, body = get_default_file_body())
        # TODO zrobienie wyszukiwarki plików jeżeli nie ma default body
    elif request.path == "/test":
        return built_response(code = 200, body = "<h1>test<h1>")
    else:
        # TODO zrobienie że można dać nazwy plików
        return built_response(code = 404, body = get_not_found_body())
