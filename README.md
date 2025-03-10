# Simple Python HTTP Server

This project is a simple Python HTTP server designed to serve files and websites. It is lightweight and easy to use. The server can handle basic HTTP methods (GET, POST) and supports custom response headers. It also includes simple error handling for common HTTP errors.

## Features

- Serve static files and websites
- Handle basic HTTP methods (GET, POST)
- Customizable response headers
- Simple error handling (404, 400, 500)

## Requirements

- Python 3.9 or higher

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/morianek/simple-python-http-server.git
    cd simple-python-http-server
    ```

2. (Optional) Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

## Usage

To start the server, run the following command:
```sh
python server.py
```

By default, the server will start on `http://localhost:8888`. You can access your files and websites by navigating to this URL in your web browser.

## Configuration

You can configure the server by modifying either `config/server_config.py` or `config/response_config.py` file. Here are some common configurations:

- **Port**: Change the port number by modifying the `PORT` variable.
- **Document Root**: Set the directory from which files will be served by modifying the `DOCUMENT_ROOT` variable.

## Error Handling

The server includes basic error handling for common HTTP errors:
- **404 Not Found**: Returned when a requested file or page is not found.
- **400 Bad Request**: Returned when the server cannot understand the request due to malformed syntax.
- **500 Internal Server Error**: Returned when the server encounters an unexpected condition.
