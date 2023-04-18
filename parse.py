from dataclasses import dataclass
import bs4
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__)) + "//"

class Parser:
    def __init__(self, source) -> None:
        self.source: str = source
        self.json_dict: dict = {}
    
    @staticmethod
    def __read_html(filename: str):
        with open(BASE_DIR + filename, "r") as file:
            text = file.read()
        return text
    
    def parse(self):
        info = bs4.BeautifulSoup(Parser.__read_html(self.source), "html.parser")
        
        for movie in info.find_all("a", class_ = "nbl-slimPosterBlock nbl-slimPosterBlock_type_poster nbl-slimPosterBlock_iconStatus_none nbl-slimPosterBlock_available collections__nbl-slimPosterBlock"):
            rating = movie.find("div", class_ = "nbl-ratingCompact__value")
            
            sorted_rating: list = []
            sorted_rating.append(rating.find("div", class_ = "nbl-ratingCompact__valueInteger").text)
            sorted_rating.append(rating.find("div", class_ = "nbl-ratingCompact__valueFraction").text)
            
            sorted_rating: str = "".join(sorted_rating)
            
            name = movie.find("span", class_ = "nbl-slimPosterBlock__titleText").text
            
            info_about_film = movie.find("div", class_ = 'nbl-poster__propertiesInfo')
            
            year: str= None
            country: str = None
            genre: str = None
            range_film: str = None
            for grid_data in info_about_film .find_all("div", class_ = "nbl-poster__propertiesRow"):
                if year == None:
                    year, country, genre = grid_data.text.split(", ")
                else:
                    range_film = grid_data.text
            
            self.json_dict[name] = {
                "year": year,
                "country": country,
                "genre": genre,
                "rating": sorted_rating,
                "length_film": range_film,
            }
            
    def save(self, filename:str):
        import json
        with open(BASE_DIR + filename, "w") as file:
            file.write(json.dumps(self.json_dict, ensure_ascii=False, indent=2))
        
        

if __name__ == "__main__":
    FILE_PATH = "ivi.html"
    PARSED_FILE_PATH = "ivi_data.json"
    x = Parser(FILE_PATH)
    x.parse()
    x.save(PARSED_FILE_PATH)
