from settings.conf import BASE_DIR
import os

# Create logs folder if it doesn't exist
LOGS_DIR = BASE_DIR / "logs"
os.makedirs(LOGS_DIR, exist_ok=True)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} - {asctime} - {name} - {message}",
            "style": "{",
        },
    },
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "debug.log",
            "formatter": "verbose",
            "maxBytes": 1024 * 1024 * 5,
            "backupCount": 3,
        },
        "aboutme_file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": BASE_DIR / "logs" / "aboutme.log",
            "formatter": "verbose",
            "maxBytes": 1024 * 1024 * 5,
            "backupCount": 3,
        },
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console", "file"],
        "level": "INFO",
    },
    "loggers": {
        "aboutme": {
            "handlers": ["aboutme_file"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
