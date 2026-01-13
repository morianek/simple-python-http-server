from dataclasses import dataclass

@dataclass
class Config:
    HOST: str
    PORT: int

def get_config(config: dict | None = None) -> Config:
    if config and config.get("server"):
        server_conf = config["server"]
        host = server_conf.get("host", "localhost")
        port = server_conf.get("port", 8888)
        return Config(HOST=host, PORT=port)
    return Config(HOST='localhost', PORT=8888)

