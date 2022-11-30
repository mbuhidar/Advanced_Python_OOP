# You will need to create a config.py file in same directory with contents:
# filestack_api_key = "YOUR API KEY HERE"
import config
from filestack import Client


class FileSharer:
    def __init__(self, filepath, api_key=config.filestack_api_key):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
