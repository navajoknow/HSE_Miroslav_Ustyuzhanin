from datetime import datetime

"""
Домашнее задание №7

Задание

Реализуйте класс CourtCase.

При вызове метода конструктора экземпляра (__init__) должны создаваться следующие атрибуты экземпляра:
● case_number (строка с номером дела — обязательный параметр) передаётся в
качестве аргумента при создании экземпляра
● case_participants (список по умолчанию пустой)
● listening_datetimes (список по умолчанию пустой)
● is_finished (значение по умолчанию False)
● verdict (строка по умолчанию пустая)

У экземпляра должны быть следующие методы:
● set_a_listening_datetime — добавляет в список listening_datetimes судебное заседание (структуру можете придумать сами)
● add_participant — добавляет участника в список case_participants (можно просто ИНН)
● remove_participant — убирает участника из списка case_participants
● make_a_decision — вынести решение по делу, добавить verdict и сменить атрибут is_finished на True
"""

class CourtCase:
    def __init__(self, case_number: str):
        self.case_number = case_number
        self.case_participants = []
        self.listening_datetimes = []
        self.is_finished = False
        self.verdict = ""

    def set_a_listening_datetime(self, start_time: str, place: str):
        """
        set_a_listening_datetime — добавляет в список listening_datetimes судебное заседание
        """
        listening = {
            "start_time": datetime.strptime(start_time, '%d.%m.%Y %H:%M'),
            "place": place,
        }
        self.listening_datetimes.append(listening)

    def add_participant(self, inn: str):
        """
        добавляет участника в список case_participants
        """
        if inn in self.case_participants:
            print("Указанный участник уже есть в деле")
        else:
            self.case_participants.append(inn)

    def remove_participant(self, inn: str):
        """
        убирает участника из списка case_participants
        """
        if inn not in self.case_participants:
            print("Указанный участник отсутствует в деле")
        else:
            self.case_participants.remove(inn)

    def make_a_decision(self, verdict: str):
        """
        вынести решение по делу, добавить verdict и сменить атрибут is_finished на True
        """
        self.verdict = verdict
        self.is_finished = True


# ТЕСТИРУЕМ

testcase = CourtCase(case_number='А40-132541/2023')
testcase.set_a_listening_datetime(start_time='12.04.2024 17:00', place='Арбитражный суд города Москвы, Зал № 555')
testcase.add_participant('7707083893')
testcase.add_participant('7706107510')
testcase.add_participant('5504036333')
testcase.add_participant('5911029807')
testcase.remove_participant('5911029807')
testcase.make_a_decision(verdict='Иск удовлетворить полностью')

print(f'Номер дела: {testcase.case_number}')
print('Участники:')
for i in testcase.case_participants:
    print(f'  ИНН {i}')
for i in testcase.listening_datetimes:
    print(f'Дата и время судебного заседания: {i['start_time'].strftime('%d.%m.%Y, %H:%M')}')
    print(f'Место судебного заседания: {i['place']}')
print(f'Суд вынес решение: {testcase.verdict}')
print(f'Дело завершено: {testcase.is_finished}')

