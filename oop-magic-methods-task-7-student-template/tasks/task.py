from contextlib import ContextDecorator
from datetime import datetime
import time


class LogFile(ContextDecorator):
    def __init__(self, log_file):
        self.log_file = log_file

    def __enter__(self):
        self.start_time = datetime.now()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = datetime.now()
        execution_time = end_time - self.start_time
        error_message = str(exc_value) if exc_value else "None"
        log_entry = f"Start: {self.start_time} | Run: {execution_time} | An error occurred: {error_message}\n"
        with open(self.log_file, "a") as file:
            file.write(log_entry)
        if exc_type:
            return False  # Reraise the exception