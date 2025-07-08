import os

class Cd:
    def __init__(self, path):
        if not os.path.isdir(path):
            raise ValueError("The specified path is not a valid directory.")
        self.new_dir = path

    def __enter__(self):
        self.original_dir = os.getcwd()
        os.chdir(self.new_dir)

    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.original_dir)