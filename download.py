import requests
import os
from dataclasses import dataclass

# Ссылка на папку src
BASE_DIR = os.path.dirname(os.path.realpath(__file__)) + "//"

@dataclass
class Downloader:
    url: str
    params: dict
    method: str = "GET"
    html_text: str = None
    
    def get_html(self) -> None:
        result = requests.request(url=self.url, params=self.params, method=self.method)
        self.html_text = result.text
        return None
    
    def save(self, filename: str) -> None:
        with open(BASE_DIR + filename, "w") as file:
            file.write(self.html_text)

if __name__ == "__main__":
    URL = "https://www.ivi.ru/collections/best-movies"
    PARAMS = {}
    FILE_PATH = "ivi.html"
    downloader = Downloader(url=URL, params=PARAMS, method="GET")
    downloader.get_html()
    downloader.save(FILE_PATH)
        
    
    