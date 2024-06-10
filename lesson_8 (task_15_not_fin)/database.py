# импортируем встроенную в Python базу данных SQLite
import sqlite3


class DB:
    db_path = 'Bot.db'

    def __init__(self):
        # чтобы подключится к базе данных, нам необходимо использовать ее метод .connect() и передать в него путь до файла с БД
        self.con = sqlite3.connect(self.db_path)
        # чтобы совершать операции с БД, нам необходим курсор, который можно вызвать через метод .cursor()
        self.cur = self.con.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # коммитим изменения
        self.con.commit()
        # закрываем базу данных
        self.con.close()

    # если бы таблиц не было, встроили бы методы по по их созданию в БД:
    # cur.execute("CREATE TABLE IF NOT EXISTS users(tgid, username, fullname, reg_timestamp)")
    # cur.execute("CREATE TABLE IF NOT EXISTS users_answers(tgid, questions, answers)")

    def insert_user(self, tgid, username, fullname, reg_timestamp):
        self.cur.execute(f"INSERT INTO users VALUES({tgid}, {username}, {fullname}, {reg_timestamp})")

    def select_user(self, tgid):
        r = self.cur.execute(f"SELECT * FROM users WHERE tgid = {tgid}")
        return r.fetchone()


def handle_user(tgid):
    with DB() as db:
        user = db.select_user(tgid)
        if not user:
            db.insert_user()
    return user


















    def insert_poll(self, tgid):
        self.cur.execute(f"INSERT INTO polls VALUES({tgid}, 'Нет ответа', 'Нет ответа', 'Нет ответа')")

    def select_poll(self, tgid):
        r = self.cur.execute(f"SELECT * FROM polls WHERE tgid = {tgid}")
        return r.fetchone()

    def update_poll(self, tgid, question_number, answer):
        self.cur.execute(f"UPDATE polls SET question_{question_number} = '{answer}' WHERE tgid = {tgid}")



def save_user(tgid, nickname):
    with DB() as db:
        db.insert_user(tgid, nickname)


def get_poll(tgid):
    with DB() as db:
        result = db.select_poll(tgid)
    return result


def create_poll(tgid):
    with DB() as db:
        db.insert_poll(tgid)


def save_answer(tgid, question_number, answer):
    with DB() as db:
        db.update_poll(tgid, question_number, answer)


if __name__ == "__main__":
    pass

