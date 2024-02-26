from random import randint

from lesson_2_data import courts, respondents

"""
Создайте ряд функций для проведения математических вычислений:
● Функция вычисления факториала числа (произведение натуральных чисел от 1 до n).
Принимает в качестве аргумента число, возвращает его факториал.

● Поиск наибольшего числа из трёх.
Принимает в качестве аргумента кортеж из трёх чисел, возвращает наибольшее из них.

● Расчёт площади прямоугольного треугольника.
Принимает в качестве аргумента размер двух катетов треугольника. Возвращает площадь треугольника.
"""


def func_1_factorial(number: int) -> int | float:
    start = 1
    result = 1
    for i in range(number):
        result = result * start
        start += 1
    return result


def func_2_max_number(*args) -> int | float:
    max_ = 0
    for i in args:
        if i > max_:
            max_ = i
    return max_


def func_3_triangle_square(leg_1: int, leg_2: int) -> int | float:
    return (leg_1 * leg_2) / 2


def task_1():
    a, b, c = 15, randint(1, 99), randint(1, 99)
    print(f"Факториал числа a({a}) - {func_1_factorial(a)}")
    print(f"Из чисел a = {a}, b = {b}, c = {c} самое большое - {func_2_max_number(a, b, c)}")
    print(f"Из чисел a = {a}, b = {b}, c = {c} самое большое - {max((a, b, c))}")
    print(f"Катет a = {a} см, катет b = {b} см, площадь треугольника равна - {func_3_triangle_square(a, b)}")


"""
Создайте функцию для генерации текста с адресом суда.
Функция должна по шаблону генерировать шапку для процессуальных документов с
реквизитами сторон для отправки.

Пример работы функции:
В арбитражный суд города Москвы
Адрес: 115225, г. Москва, ул. Б. Тульская, 17
Истец: Пупкин Василий Геннадьевич
ИНН 1236182357 ОГРНИП 218431927812733
Адрес: 123534, г. Москва, ул. Опущенных водников, 13
Ответчик: ООО “Кооператив Озеро”
ИНН 1231231231 ОГРН 123124129312941
Адрес: 123534, г. Москва, ул. Красивых молдавских партизан, 69
Номер дела А40-123456/2023

Функция должна принимать в качестве аргумента словарь с данными ответчика и
номером дела (ссылка на файл с данными).
● На основании номера дела из списка судов должен быть выбран корректный
суд для отправки (данные по арбитражным судам также имеются в указанном
выше файле). Используйте код суда из дела
● С помощью f-string создайте шаблон для заполнения
● В качестве истца укажите свои данные (данные студента)
● В данные по ответчику подставьте данные, переданные в функцию в качестве
аргумента
● В конце шапки подставьте номер дела
Функция должна возвращать готовую шапку в виде строки.
Создайте ещё одну функцию, которая принимает в себя список словарей с данными
ответчика. Используйте цикл for для генерации всех возможных вариантов данной
шапки с вызовом первой функции внутри тела цикла for и выводом данных. которые
она возвращает в консоль.
"""


def make_court_nominative_case(court_name: str) -> str:
    """

    :param court_name:
    :return:
    """
    words = court_name.split(" ")[2::]
    text = "Арбитражный суд"
    for i in words:
        text += f" {i}"
    return text


def make_a_header(court, plaintiff, respondent):
    text = f"-------------------------------\n" \
           f"В {make_court_nominative_case(court['court_name'])}\n" \
           f"Адрес: {court['court_address']}\n\n" \
           f"" \
           f"Истец: {plaintiff['name']}" \
           f"ИНН {plaintiff['inn']} ОГРНИП {plaintiff['ogrnip']}\n" \
           f"Адрес: {plaintiff['address']}\n\n" \
           f"" \
           f"Ответчик: {respondent['short_name']}”\n" \
           f"ИНН {respondent['inn']} ОГРН {respondent['ogrn']}\n" \
           f"Адрес: {respondent['address']}\n\n" \
           f"" \
           f"Номер дела {respondent['case_number']}\n"
    return text


def task_2():
    plaintiff = {
        "name": "Сиротинский Кирилл Александрович",
        "inn": "1236182357",
        "ogrnip": "218431927812733",
        "address": "123534, г. Москва, ул. Красивых молдавских партизан, 69"
    }
    cleaned_respondents = [i for i in respondents if i.get("case_number")]
    for respondent in cleaned_respondents:
        court_code = respondent["case_number"].split("-")[0]
        court = courts[court_code]
        result = make_a_header(court, plaintiff, respondent)
        print(result)

def main():
     task_1()
     task_2()

if __name__ == "__main__":
    main()
    print("stop")