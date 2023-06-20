import os


def read_file():
    file_path = os.path.dirname(__file__)
    file_ = os.path.join(file_path, "books (1).db")
    if not os.path.exists(file_):
        raise Exception("file not exits")
    return file_


def image_file():
    file_path = os.path.dirname(__file__)
    file_ = os.path.join(file_path, "images")
    if not os.path.exists(file_):
        raise Exception("file not exits")
    return file_


def download_location():
    file_path = os.path.dirname(__file__)
    file = os.path.join(file_path, "Download")
    return file