import requests
import pprint
import json


class ImgDownloader:

    def __init__(self, json_file):
        self.json_file = json_file
        self.data = []

    def json_decoder(self):
        with open(self.json_file, 'r') as json_file:
            self.data = json.load(json_file)
            return self.data

    @staticmethod
    def img_binary_writer(url, name):
        with open(name, 'wb') as img:
            img.write(requests.get(url).content)

    def img_creator(self):
        for data_ in self.json_decoder():
            self.img_binary_writer(data_["img_url"], data_["img_name"])


a = ImgDownloader('json_file.json')
a.img_creator()

