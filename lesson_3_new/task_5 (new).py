import json
import csv
import re


def get_inn_from_txt(path_to_traders_txt: str) -> list:
    """
    1.1. получаем список ИНН организаций из файла traders.txt
    """
    inn_from_txt = []
    with open(path_to_traders_txt, 'r') as f:
        for i in f:
            inn = i.strip()
            inn_from_txt.append(inn)
    return inn_from_txt


def get_data_from_json(path_to_traders_json: str, inn_from_txt: list) -> list:
    """
    1.2. получаем список с информациоей о таких организациях (ИНН, ОГРН, адрес) из файла traders.json
    """
    with open(path_to_traders_json, 'r') as f:
        traders_json = json.load(f)
    data_from_json = []
    for i in traders_json:
        if i['inn'] in inn_from_txt:
            trader = {'inn': i.get('inn'), 'ogrn': i.get('ogrn'), 'address': i.get('address')}
            data_from_json.append(trader)
    return data_from_json


def save_json_data_to_csv(data_from_json):
    """
    1.3. сохраняем такую информацию об организациях в файле traders.csv
    """
    filename = 'traders.csv'
    fieldnames = ['inn', 'ogrn', 'address']
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for i in data_from_json:
            writer.writerow(i)


def find_emails(text: str) -> list:
    """
    2.2. ищем адреса эл. почты
    """
    email_pattern = re.compile(r'\b[0-9a-zA-Z._-]+@[0-9a-zA-Z._-]+\.[a-zA-Z]+\b')
    return re.findall(email_pattern, text)


def get_emails_from_json(path_to_efrsb_json) -> dict:
    """
    2.1. запускаем функцию для поиска адресов эл. почты и создаем из них словарь
    """
    with open(path_to_efrsb_json, 'r') as f:
        efrsb_messages_json = json.load(f)
    emails = {}
    for i in efrsb_messages_json:
        temp_emails = find_emails(i.__str__())
        if i.get('publisher_inn') in emails:
            emails[i['publisher_inn']].update(temp_emails)
        else:
            emails[i['publisher_inn']] = set(temp_emails)
    return emails


def save_emails_to_json(emails):
    """
    2.3. сохраняем словарь с адресами эл. почты в файл emails.json, при этом:
    - устнавливаем кодировку и параметр ensure_ascii=False, чтобы в файле отображались символы кириллицы
    - преобразовываем значения словаря из множеств в списки (последние поддерживаются форматом json)
    """
    filename = 'emails.json'
    to_lists = {k: list(v) for k, v in emails.items()}
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(to_lists, json_file, ensure_ascii=False, indent=4)


def main():
    path_to_traders_txt = 'data_sources/traders.txt'
    path_to_traders_json = 'data_sources/traders.json'
    path_to_efrsb_json = 'data_sources/10000_efrsb_messages.json'

    inn_from_txt = get_inn_from_txt(path_to_traders_txt)
    data_from_json = get_data_from_json(path_to_traders_json, inn_from_txt)
    save_json_data_to_csv(data_from_json)
    emails = get_emails_from_json(path_to_efrsb_json)
    save_emails_to_json(emails)


if __name__ == '__main__':
    main()
