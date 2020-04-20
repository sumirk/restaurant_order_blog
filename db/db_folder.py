import os
import sys

def get_full_path(db_name):
    return os.path.join(os.path.dirname(__file__), db_name)
