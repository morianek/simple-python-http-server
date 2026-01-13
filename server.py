import socket
import logging

from parsers import parse_request
from config import setup, server_config
from request_handler import handle_request

setup('sites/default')
from config import config

logger = logging.getLogger(__name__)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((config.server.HOST, config.server.PORT))
s.listen(5)

logger.info(f"Listening on http://{config.server.HOST}:{config.server.PORT}\n")

while True:
    client_socket, address = s.accept()

    logger.info("-" * 40 + "\n")
    logger.info(f"Connected to {address[0]} on port {address[1]}")

    try:
        request_data_str = client_socket.recv(2048).decode()
    except Exception as e:
        logger.error(f"Error receiving data: {e} \n")
        client_socket.close()
        continue

    logger.info(f"request: {request_data_str.split('\r\n')[0]}")

    parsed_request_data = parse_request(request_data_str)

    logger.debug(f"parsed request: {parsed_request_data}")

    server_response = handle_request(parsed_request_data)


    client_socket.send(server_response)
    client_socket.close()