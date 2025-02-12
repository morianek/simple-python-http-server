class Request:
    def __init__(self, method, path, headers, body, get_params):
        self.method = method
        self.path = path
        self.headers = headers
        self.body = body
        self.get_params = get_params

    def __str__(self):
        return f"{self.method} {self.path} {self.get_params}\n{self.headers} {f"\n{self.body}" if self.body else ""}"

def parse_request(data):
    lines = data.split("\r\n")
    method, path, _ = lines[0].split(" ")
    headers = {}
    body = ""
    cur_line = 0
    for line in lines[1:]:
        cur_line += 1
        if line == "":
            break
        key, value = line.split(": ")
        headers[key] = value
    if cur_line < len(lines):
        body = lines[cur_line]
    if method == "GET":
        get_params = parse_get_params(path)
        if path.find("?") != -1:
            path = path[:path.find("?")]
    else:
        get_params = None

    return Request(method, path, headers, body, get_params)

def parse_get_params(path):
    start_index = path.find("?")
    if start_index == -1:
        return None
    get_attribs = path[start_index+1:]
    get_attribs = get_attribs.split("&")

    attribs = {}
    for attrib in get_attribs:
        attrib = attrib.split("=")
        attribs[attrib[0]] = attrib[1]

    return attribs

