import json
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.cbr.ru'


def get_currency_page_soup(to_date=None):
    """
    забираем данные с курсами валют к рублю на указанную в качестве аргумента дату со страницы сайта ЦБ РФ
    и отдаем soup-объект
    """
    params = f"?UniDbQuery.Posted=True" \
             f"&UniDbQuery.To=05.06.2024"
    # две строки ниже - конструирование URL
    url = f"{BASE_URL}/currency_base/daily/"
    r = requests.get(url)
    # строка ниже - проверка на 200-й код (если что-то другое, то код будет "падать")
    r.raise_for_status()
    # строка ниже - создание soup-объекта с аргументом text (атрибутом html страницы,
    # содержащим ее текстовое представление) и аргументом, указывающим,
    # что необходимо распарсить переданные текстовые данные как html страницу
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def parse_currency_page_soup(soup: BeautifulSoup):
    """
    достаем интересующую нас информацию из soup-объекта
    """
    # пропускаем заголовок таблицы
    table_rows = soup.find('table').findAll('tr')[1:]
    # используем list comprehension для создания списков с данными колонок таблицы
    digit_codes = [row.findAll('td')[0].text.strip() for row in table_rows]
    letter_codes = [row.findAll('td')[1].text.strip() for row in table_rows]
    units = [row.findAll('td')[2].text.strip() for row in table_rows]
    currencies = [row.findAll('td')[3].text.strip() for row in table_rows]
    currency_rates = [row.findAll('td')[4].text.strip() for row in table_rows]

    # формируем словарь
    data = {
        "digit_codes": digit_codes,
        "letter_codes": letter_codes,
        "units": units,
        "currencies": currencies,
        "currency_rates": currency_rates
    }
    # возвращаем строку из json-объекта
    return json.dumps(data)


def main():
    currency_page_soup = get_currency_page_soup()
    parsed_data = parse_currency_page_soup(currency_page_soup)
    print(parsed_data)


main()
