class Request:
    def __init__(self, data: str):
        self.method = ""
        self.path = ""
        self.headers = {}
        self.body = ""
        self.get_params = None
        self.parse_request(data)

    def __str__(self):
        return f"{self.method} {self.path} {self.get_params}\n{self.headers} {f"\n{self.body}" if self.body else ""}"

    def parse_request(self, data: str):
        try:
            lines = data.split("\r\n")
            self.method, self.path, _ = lines[0].split(" ")
            self.headers = {}
            self.body = ""
            cur_line = 0
            for line in lines[1:]:
                cur_line += 1
                if line == "":
                    break
                key, value = line.split(": ")
                self.headers[key] = value
            if cur_line < len(lines):
                self.body = lines[cur_line]
            if self.method == "GET":
                self.get_params = self.parse_get_params(self.path)
                if self.path.find("?") != -1:
                    self.path = self.path[:self.path.find("?")]
            else:
                self.get_params = None

        except Exception as e:
            print(f"Exception {e} occurred")
            return None

    @staticmethod
    def parse_get_params(path: str) -> dict | None:
        start_index = path.find("?")
        if start_index == -1:
            return None
        get_attribs = path[start_index + 1:]
        get_attribs = get_attribs.split("&")

        attribs = {}
        for attrib in get_attribs:
            attrib = attrib.split("=")
            attribs[attrib[0]] = attrib[1]

        return attribs
