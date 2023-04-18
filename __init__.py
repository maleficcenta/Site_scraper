from download import Downloader
from parse import Parser
from data import Data
    
def process(url, web_page_path=None, data_path=None):
    PARAMS = {}
    downloader = Downloader(url=url, params=PARAMS, method="GET")
    downloader.get_html()
    downloader.save(web_page_path)
    print("Информация с сайта скачена")
    x = Parser(web_page_path)
    x.parse()
    x.save(data_path)
    print("Информация с сайта обработана и записана в JSON формате")
    return Data.stat(data_path)

if __name__ == "__main__":
    URL = "https://www.ivi.ru/collections/best-movies"
    FILE_PATH = "ivi.html"
    PARSED_FILE_PATH = "ivi_data.json"
    process(URL,FILE_PATH, PARSED_FILE_PATH)