import logging
import logging.config

logging_default_conf = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "stream": "ext://sys.stdout"
        },
        "file": {
            "class": "logging.FileHandler",
            "formatter": "standard",
            "filename": "server.log",
            "level": "INFO",
        },
    },
    "root": {
        "handlers": ["console", "file"],
        "level": "INFO",
    },
}


def setup_logging(config: dict | None = None):
    logging_conf = logging_default_conf.copy()
    if config and config.get("logging"):
        if config["logging"].get("output_file"):
            logging_conf['handlers']['file']['filename'] = config["logging"]["output_file"]
        if config["logging"].get("level"):
            logging_conf['root']['level'] = config["logging"]["level"]

    logging.config.dictConfig(logging_conf)
