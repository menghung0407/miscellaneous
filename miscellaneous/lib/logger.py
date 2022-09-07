import logging.handlers
import time
from pathlib import Path

from flask import has_request_context, request

LOG_PATH = Path(Path(__file__).parents[2], 'log')
LOG_PATH.mkdir(exist_ok=True)

THIS_LOGGER = logging.getLogger(__name__)
THIS_LOGGER.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

ui_ux_concept_log = LOG_PATH.joinpath('miscellaneous.log')
debug_file_handler = logging.FileHandler(filename=str(ui_ux_concept_log),
                                         encoding='utf-8')
debug_file_handler.setLevel(logging.DEBUG)


class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None

        try:
            if record.log_ip is None:
                record.log_ip = 'xxx.xxx.xxx.xxx'
        except AttributeError:
            record.log_ip = 'xxx.xxx.xxx.xxx'

        return super().format(record)


FORMATTER = RequestFormatter(
    '%(asctime)s %(remote_addr)-15s > %(thread)d: %(url)s [%(log_ip)-15s] -%(levelname)s- %(message)s ',
    datefmt='%Y-%m-%d %H:%M:%S')

console_handler.setFormatter(FORMATTER)
debug_file_handler.setFormatter(FORMATTER)

THIS_LOGGER.addHandler(console_handler)
THIS_LOGGER.addHandler(debug_file_handler)


def debug(message, *args, **kwargs):
    THIS_LOGGER.debug(message, *args, **kwargs)


def info(message, *args, **kwargs):
    THIS_LOGGER.info(message, *args, **kwargs)


def warning(message, *args, **kwargs):
    THIS_LOGGER.warning(message, *args, **kwargs)


def exception(message: str = 'N/A', *args, exc_info=True, **kwargs):
    THIS_LOGGER.exception(f'Customize Message: {message}',
                          *args,
                          exc_info=exc_info,
                          **kwargs)


def time_sleep(seconds: int, *args, **kwargs):
    THIS_LOGGER.info(f'time sleep: {seconds}', *args, **kwargs)
    time.sleep(seconds)
