def get_basic_headers():
    return {"content-type": "text/html; charset=utf-8"}


def built_response(code, headers = None, body = ""):
    if headers is None:
        headers = get_basic_headers()

    response = f"HTTP/1.1 {code} "

    if code == 200:
        response += "OK\n"
    elif code == 404:
        response += "Not Found\n"

    for key, val in headers.items():
        response += f"{key}: {val}\n"
    response += "\n"

    response+=body

    return response.encode()
