import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__)) + "//"

class Data:
    def __init__(self) -> None:
        self.dct: dict = {}
    
    def __read_data(self, filename: str):
        import json
        with open(BASE_DIR + filename) as json_file:
            self.dct = json.load(json_file)
    
    @staticmethod
    def stat(filename: str):
        x = Data()
        x.__read_data(filename)
        country_stat = x.__country_data()
        genre_stat = x.__genre_data()
        time_stat = x.__middle_time()
        rating_stat = x.__rating()
        print(country_stat, end="\n\n")
        print(genre_stat)
        print(time_stat)
        print(rating_stat)
        
    def __country_data(self):
        dct: dict = {}
        for film_name, data in self.dct.items():
            country = data['country']
            if dct.get(country):
                dct[country] += 1
            else:
                dct[country] = 1
        dct = {k: v for k, v in sorted(dct.items(), key=lambda item: item[1], reverse=True)}
        
        output:str = "По статистике лучших фильмов по версии IVI:\n\n"
        for country, value in dct.items():
            output += f"{country} выпустила {f'{value} фильм' if int(value) == 1 else f'{value} фильмом'}\n"
        return output
    
    def __genre_data(self):
        dct: dict = {}
        for film_name, data in self.dct.items():
            genre = data['genre']
            if dct.get(genre):
                dct[genre] += 1
            else:
                dct[genre] = 1
        dct = {k: v for k, v in sorted(dct.items(), key=lambda item: item[1], reverse=True)}
        
        output:str = ""
        for genre, value in dct.items():
            output += f"Количество фильмов с жанром '{genre}' составляет: {value}\n"
        return output
    
    def __middle_time(self):
        lst: list = []
        for film_name, data in self.dct.items():
            lst.append(int(data['length_film'].split(' ')[0]))
        from math import floor
        output = f"Средняя продолжительность фильмов в минутах: {floor(sum(lst) / len(lst))}\n"
        return output
    
    def __rating(self):
        lst: list = []
        for film_name, data in self.dct.items():
            lst.append(float(data['rating'].replace(",", ".")))
        output = f"Средняя оценка фильма: {round(sum(lst) / len(lst), 1)}\n"
        return output
    
if __name__ == "__main__":
    PARSED_FILE_PATH = "ivi_data.json"
    Data.stat(PARSED_FILE_PATH)
    