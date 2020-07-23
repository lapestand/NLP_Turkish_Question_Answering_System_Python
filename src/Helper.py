import os
import shutil
import http.client as httplib
from os.path import join
from urllib.parse import urlparse


class Properties:
    debug = True

    supported_file_types = [
        "pdf", "html", "txt"
    ]

    error_messages = {
        "unsupported_file_type": "\nError: Unsupported file type! Please enter a valid file type!"
    }

    referance_url = "www.google.com"

    zemberek_path: str = join('Dependencies', 'Zemberek-Python', 'bin', 'zemberek-full.jar')

    error_file_name = "Errors.txt"

    def __init__(self):
        pass

    def __del__(self):
        pass


def rm_r(self, path):
    if os.path.isdir(path) and not os.path.islink(path):
        shutil.rmtree(path)
    elif os.path.exists(path):
        os.remove(path)


def chunk_size(self):
    return 8192
