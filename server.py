import socket

from parsers.html_req_parser import parse_request
from config import get_server_config
from request_handler import handle_request

config = get_server_config()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((config.HOST, config.PORT))
s.listen(5)

while True:
    client_socket, address = s.accept()

    print(f"Connected to {address[0]} on port {address[1]}\n")

    request_data_str = client_socket.recv(2048).decode()
    print(request_data_str)

    parsed_request_data = parse_request(request_data_str)
    print(parsed_request_data)

    server_response = handle_request(parsed_request_data)

    client_socket.send(server_response)
    client_socket.close()