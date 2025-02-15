def get_basic_headers(body_len):
    return {
        "Server": "Kox server",
        "Connection": "close",
        "Content-Length": body_len,
    }


def built_response(code, headers = None, body = ""):
    if headers is None:
        headers = get_basic_headers(len(body))
    else:
        headers.update(get_basic_headers(len(body)))

    response = f"HTTP/1.1 {code} "

    if code == 200:
        response += "OK\n"
    elif code == 404:
        response += "Not Found\n"
    elif code == 400:
        response += "Bad Request"

    for key, val in headers.items():
        response += f"{key}: {val}\n"
    response += "\n"

    response += body

    return response.encode()
