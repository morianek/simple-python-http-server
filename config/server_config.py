from dataclasses import dataclass

@dataclass
class Config:
    HOST: str
    PORT: int

def get_config():
    return Config(HOST='localhost', PORT=8888)

