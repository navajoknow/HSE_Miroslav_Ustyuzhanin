import requests
from bs4 import BeautifulSoup
import json


class ParserCBRF:
    """
    Класс для парсинга данных с курсами валют на заданную дату,
    страница: https://www.cbr.ru/currency_base/daily/
    """
    BASE_URL = 'https://www.cbr.ru'

    def __init__(self, to_date: str):
        self.to_date = to_date
        # создаем пустой словарь, в который в дальнейшем положим данные и который будем использовать
        # для формирования файла в json формате
        self.data = {}

    def start(self):
        soup = self.__get_currency_page_soup()
        self.data = self.__parse_currency_page_soup(soup)
        self.__save_parsed_data()

    def __get_currency_page_soup(self) -> BeautifulSoup:
        """
        забираем данные с курсами валют к рублю на заданную дату
        :return: возвращаем soup-объект
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

    def __parse_currency_page_soup(self, soup: BeautifulSoup) -> dict:
        """
        достаем данные из таблицы с курсами валют soup-объекта
        :return: словарь
        """
        # находим строки таблицы (tr), пропуская заголовок, и создаем из них общий список
        table_rows = soup.find('table').findAll('tr')[1:]
        # используем list comprehension для создания отдельных списков из колонок таблицы:
        # делаем это, выдергивая ячейки (td), занимающие определенные позиции в каждой строке (tr),
        # и создаем словарь (справочник), в качестве ключей которого указываем названия столбцов таблицы, а в качестве
        # значений - полученные списки
        data = {
            "digit_codes": [row.findAll('td')[0].text.strip() for row in table_rows],
            "letter_codes": [row.findAll('td')[1].text.strip() for row in table_rows],
            "units": [row.findAll('td')[2].text.strip() for row in table_rows],
            "currencies": [row.findAll('td')[3].text.strip() for row in table_rows],
            "currency_rates": [row.findAll('td')[4].text.strip() for row in table_rows]
        }
        return data

    def __save_parsed_data(self):
        """
        сохраняем данные словаря в файл формата json, при этом устнавливаем кодировку
        и параметр ensure_ascii=False, чтобы в файле json отображались символы кириллицы
        """
        filename = f"{self.to_date}.json"
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(self.data, json_file, ensure_ascii=False, indent=4)
        print(f"\nДанные сохранены в файл {filename}\n")


class ConvertingCurrenciesFromFile:
    """
    Класс для выборочной конвертации валют на основе данных из файла json
    """
    def __init__(self, to_date: str):
        self.filename = f"{to_date}.json"
        self.data = self.__load_data_from_file()

    def __load_data_from_file(self) -> dict:
        with open(self.filename, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data

    def list_available_currencies(self):
        """
        выводим пользователю список доступных валют
        """
        print("Доступные валюты:")
        for currency in self.data["currencies"]:
            print(currency)

    def currency_to_rub_converter(self, from_currency_name: str, currency_amount: float):
        """
        :param from_currency_name: название валюты для конвертации в рубли
        :param currency_amount: количество такой валюты
        :return: количество рублей в результате конвертации
        """
        if from_currency_name in self.data["currencies"]:
            index = self.data["currencies"].index(from_currency_name)
            rate = float(self.data["currency_rates"][index].replace(',', '.'))
            units = int(self.data["units"][index])
            amount_in_rub = currency_amount * (rate / units)
            print(f"\n{currency_amount} {from_currency_name} = {amount_in_rub:.2f} рублей")
        else:
            print(f"\nВалюта '{from_currency_name}' не найдена в данных")

    def rub_to_currency_converter(self, to_currency_name: str, rub_amount: float):
        """
        :param to_currency_name: название валюты для конвертации из рублей
        :param rub_amount: количество рублей
        :return: количество валюты в результате конвертации
        """
        if to_currency_name in self.data["currencies"]:
            index = self.data["currencies"].index(to_currency_name)
            rate = float(self.data["currency_rates"][index].replace(',', '.'))
            units = int(self.data["units"][index])
            amount_in_currency = rub_amount / (rate / units)
            print(f"\n{rub_amount} рублей = {amount_in_currency:.2f} {to_currency_name}")
        else:
            print(f"\nВалюта '{to_currency_name}' не найдена в данных")


def main():

    to_date = input("Укажите дату (дд.мм.гггг) для выгрузки информации о соответствующих курсах валют: ")

    parser = ParserCBRF(to_date)
    parser.start()

    converter = ConvertingCurrenciesFromFile(to_date)
    converter.list_available_currencies()

    from_currency_name = input("\nУкажите название валюты из списка выше для конвертации в рубли: ")
    currency_amount = float(input("Укажите количество валюты для конвертации в рубли: "))
    converter.currency_to_rub_converter(from_currency_name, currency_amount)

    rub_amount = float(input("\nУкажите количество рублей для конвертации в валюту: "))
    to_currency_name = input("Укажите название валюты из списка выше для конвертации из рублей: ")
    converter.rub_to_currency_converter(to_currency_name, rub_amount)


if __name__ == '__main__':
    main()
