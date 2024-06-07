import requests
from bs4 import BeautifulSoup
import json

class ParserCBRF:
    BASE_URL = 'https://www.cbr.ru'

    def __init__(self, to_date: str):
        self.to_date = to_date
        # создаем пустой словарь, в который в дальнейшем положим данные после обработки парсером
        self.data = {}

    def start(self):
        soup = self.__get_currency_page_soup()
        self.data = self.__parse_currency_page_soup(soup)
        self.__save_parsed_data()

    def __get_currency_page_soup(self) -> BeautifulSoup:
        """
        забираем данные с курсами валют к рублю на указанную в качестве аргумента дату со страницы сайта ЦБ РФ
        и возвращаем soup-объект
        """
        # две строки ниже - конструирование URL
        url = f"{self.BASE_URL}/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To={self.to_date}"
        r = requests.get(url)
        # строка ниже - проверка на 200-й код (если что-то другое, то код будет "падать")
        r.raise_for_status()
        # строка ниже - создание soup-объекта с аргументом text (атрибутом html страницы,
        # содержащим ее текстовое представление) и аргументом, указывающим,
        # что необходимо распарсить переданные текстовые данные как html страницу
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup

    def __parse_currency_page_soup(self, soup: BeautifulSoup):
        """
        достаем данные таблицы с курсами валют из soup-объекта, заполняем словарь
        и возвращаем его
        """
        # находим строки таблицы, пропуская заголовок
        table_rows = soup.find('table').findAll('tr')[1:]
        # используем list comprehension для создания списков на каждую колонку таблицы
        digit_codes = [row.findAll('td')[0].text.strip() for row in table_rows]
        letter_codes = [row.findAll('td')[1].text.strip() for row in table_rows]
        units = [row.findAll('td')[2].text.strip() for row in table_rows]
        currencies = [row.findAll('td')[3].text.strip() for row in table_rows]
        currency_rates = [row.findAll('td')[4].text.strip() for row in table_rows]
        # создаем словарь, в который в качестве значений передаем полученные списки
        data = {
            "digit_codes": digit_codes,
            "letter_codes": letter_codes,
            "units": units,
            "currencies": currencies,
            "currency_rates": currency_rates
        }
        return data

    def __save_parsed_data(self):
        """
        сохраняем словарь в файл формата json
        """
        filename = f"currency_data_{self.to_date}.json"
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(self.data, json_file, ensure_ascii=False, indent=4)
        print(f"Данные сохранены в файл {filename}")

def main():
    parser = ParserCBRF('07.06.2024')
    # запускаем парсер и сохраняем данные в JSON
    parser.start()


main()

