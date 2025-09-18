import socket
import logging

from parsers.html_req_parser import parse_request
from config import get_server_config, setup_logging
from request_handler import handle_request

setup_logging()
logger = logging.getLogger(__name__)

config = get_server_config()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((config.HOST, config.PORT))
s.listen(5)

logger.info(f"Listening on http://{config.HOST}:{config.PORT}\n")

while True:
    client_socket, address = s.accept()

    logger.info(f"Connected to {address[0]} on port {address[1]}")

    try:
        request_data_str = client_socket.recv(2048).decode()
    except Exception as e:
        logger.error(f"Error receiving data: {e} \n")
        client_socket.close()
        continue

    parsed_request_data = parse_request(request_data_str)

    if parsed_request_data is None:
        logger.info("Bad Request\n")
    else:
        logger.info(request_data_str.split("\r\n")[0] + "\n")

    logger.debug(parsed_request_data)

    server_response = handle_request(parsed_request_data)

    client_socket.send(server_response)
    client_socket.close()