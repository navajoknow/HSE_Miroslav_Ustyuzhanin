import time

class CourtCase:
    def __init__(self, case_number: str):
        self.listening_datetimes = []
    def set_a_listening_datetime(self, start: str, place: str):
        """
        set_a_listening_datetime — добавляет в список listening_datetimes судебное заседание
        """
        listening = {
            'start': time.strptime(start, '%d.%m.%Y %H:%M'),
            'place': place,
        }
        self.listening_datetimes.append(listening)


a = CourtCase('A123')
a.set_a_listening_datetime(start='15.04.2024 12:00', place='Moscow')

type(self.listening_datetimes)