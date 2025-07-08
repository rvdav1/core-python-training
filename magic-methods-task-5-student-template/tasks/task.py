import os
import shutil
import uuid

class TempDir:
    def __enter__(self):
        self.original_dir = os.getcwd()
        self.temp_dir = os.path.join(self.original_dir, str(uuid.uuid4()))
        os.mkdir(self.temp_dir)
        os.chdir(self.temp_dir)
        return self.temp_dir

    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.original_dir)
        shutil.rmtree(self.temp_dir)