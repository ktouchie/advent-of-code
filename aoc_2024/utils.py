import os


def get_input_file_path(filename):
    return os.path.join(os.path.dirname(__file__), "tests/inputs", filename)
