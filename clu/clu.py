import logging
import os
import sys

from enum import Enum


class LogLevels(Enum):
    levels = {
        '50': 'CRITICAL',
        '40': 'ERROR',
        '30': 'WARNING',
        '20': 'INFO',
        '10': 'DEBUG'
    }


class SystemLogFilter(logging.Filter):
    def filter(self, record):
        if not hasattr(record, 'id'):
            record.id = 'N/A'

        return True


class CLU(logging.Logger):
    def __init__(
        self,
        name: str = 'default',
        log_level: str = 'INFO',
        log_to_stdout: bool = True,
        log_to_file: bool = False,
        file_mode: str = 'a+',
        log_file_name: str = 'app.log',
        log_file_path: str = 'logs',
        date_format: str = '%m-%d-%Y-%H:%M:%S',
        log_format: str = '%(process)d - %(asctime)s - %(filename)s - %(funcName)s - '
                          '%(id)s - %(levelname)s: %(message)s',
    ):
        """
        Custom Logging Utility (CLU)

        :param name: <string> Name of the logger object.
        :param log_level: <string> Log level.
        :param log_to_stdout: <bool> Log to standard output.
        :param log_to_file: <bool> Log to a file
        :param file_mode: <string> file mode - default is append | 'a+'
        :param log_file_name: <string> - file name
        :param log_file_path: <string> - file path excluding the file name.
        :param date_format: <string> - date format - default is '%m-%d-%Y-%H:%M:%S'
        :param log_format: <log format> - granularity is customizable.
        """

        super().__init__(name)

        self.name = name
        self.log_level = log_level.upper()

        self.log_to_stdout = log_to_stdout

        self.log_to_file = log_to_file
        self.file_mode = file_mode
        self.log_file_name = log_file_name
        self.log_file_path = log_file_path

        self.log_format = log_format
        self.date_format = date_format

        self.validate_log_level()

        logging.basicConfig(
            datefmt=self.date_format,
            format=self.log_format,
            level=logging.getLevelName(self.log_level)
        )

        self.log = logging.getLogger(self.name)
        self.log.name = self.name

        self.create_log_dir_if_not_exists()
        self.configure_handlers()

    def __str__(self):
        return self.__dict__

    def get_logger(self):
        return self.log

    def validate_log_level(self):
        if self.log_level not in LogLevels.levels.value.values():
            logging.error(f'Invalid log level: {self.log_level}. Exiting.')
            sys.exit(1)

    def create_log_dir_if_not_exists(self):
        if self.log_to_file:
            if not os.path.exists(self.log_file_path):
                if self.log_to_file:
                    os.makedirs(self.log_file_path)

    def configure_handlers(self):
        if not self.log.handlers:
            if self.log_to_file:
                file_handler = logging.FileHandler(
                    os.path.join(self.log_file_path, self.log_file_name),
                    self.file_mode,
                    'utf-8'
                )

                file_handler.setFormatter(logging.Formatter(self.log_format))
                self.log.addHandler(file_handler)

            if self.log_to_stdout:
                stream_handler = logging.StreamHandler(sys.stdout)
                stream_handler.setFormatter(logging.Formatter(self.log_format, self.date_format))

        for handler in self.log.handlers:
            handler.addFilter(SystemLogFilter())



