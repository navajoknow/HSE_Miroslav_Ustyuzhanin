from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup

# токен предоставляет bot father при создании бота
BOT_TOKEN = '7230509682:AAFrWLgfxJZGfaiFJAIl4qV9M8j2jDjg-L8'

updater = Updater(BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# определяем состав кнопок для взаимодействия пользователя с ботом
button_1 = KeyboardButton("О проекте")
button_2 = KeyboardButton("Опрос")
button_3 = KeyboardButton("Автор")
button_4 = KeyboardButton("Назад")
button_5 = KeyboardButton("Вопрос 1")
button_6 = KeyboardButton("Вопрос 2")
button_7 = KeyboardButton("Вопрос 3")
button_8 = KeyboardButton("Результаты опроса")

# конструируем в каких разделах бота какие кнопки находятся
main_menu = [[button_1, button_2, button_3]]
about_the_project = [button_4]
author = [button_4]
back = [[button_4]]
feedback = [[button_5, button_6, button_7],
            [button_8, button_4]]

# здесь и далее - функция, которые активируются при нажатии кнопки (соответствующего текстового сообщения)
# пользователем
def start_command(update, context):
    tgid = update.effective_user.id
    nickname = update.effective_user.username
    update.message.reply_text("Привет, я тестовый бот",
                              reply_markup=ReplyKeyboardMarkup(main_menu, one_time_keyboard=True))
#reply_markup... - это клавиатура, которая наряду с текстом возвращается пользователю в ответ активацию функции

def help_command(update, context):
    text = f"/start - запуск бота\n" \
           f"/help - список команд"
    update.message.reply_text(text,
                              reply_markup=ReplyKeyboardMarkup(back, one_time_keyboard=True))


def about_the_project(update, context):
    text = f"Это учебный проект по созданию бота на Python"
    update.message.reply_text(text,
                              reply_markup=ReplyKeyboardMarkup(back, one_time_keyboard=True))


def author(update, context):
    text = f"Устюжанин Мирослав"
    update.message.reply_text(text,
                              reply_markup=ReplyKeyboardMarkup(back, one_time_keyboard=True))

def start_poll(update, context):
    text = f"Выберите вопрос"
    update.message.reply_text(text,
                              reply_markup=ReplyKeyboardMarkup(feedback, one_time_keyboard=True))

def question_1(update, context):
    text = f"Как вас зовут?"
    update.message.reply_text(text,
                              reply_markup=ReplyKeyboardMarkup(feedback, one_time_keyboard=True))

def question_2(update, context):
    text = f"Сколько вам лет?"
    update.message.reply_text(text,
                              reply_markup=ReplyKeyboardMarkup(feedback, one_time_keyboard=True))

def question_3(update, context):
    text = f"В каком городе вы живете?"
    update.message.reply_text(text,
                              reply_markup=ReplyKeyboardMarkup(feedback, one_time_keyboard=True))

def poll_result(update, context):
    text = f"Результаты опроса"
    update.message.reply_text(text,
                              reply_markup=ReplyKeyboardMarkup(feedback, one_time_keyboard=True))


# когда пользователь нажимает на кнопку, он по сути просто направляет текстовое сообщение боту (можно написать
# в чате указанное на кнопке и произойдет ровно тоже самое)
dispatcher.add_handler(CommandHandler("start", start_command))
dispatcher.add_handler(CommandHandler("help", help_command))

dispatcher.add_handler(MessageHandler(Filters.regex("Назад") & ~Filters.command, start_command))
dispatcher.add_handler(MessageHandler(Filters.regex("О проекте") & ~Filters.command, about_the_project))
dispatcher.add_handler(MessageHandler(Filters.regex("Автор") & ~Filters.command, author))
dispatcher.add_handler(MessageHandler(Filters.regex("Опрос") & ~Filters.command, start_poll))
dispatcher.add_handler(MessageHandler(Filters.regex("Вопрос 1") & ~Filters.command, question_1))
dispatcher.add_handler(MessageHandler(Filters.regex("Вопрос 2") & ~Filters.command, question_2))
dispatcher.add_handler(MessageHandler(Filters.regex("Вопрос 3") & ~Filters.command, question_3))
dispatcher.add_handler(MessageHandler(Filters.regex("Результаты опроса") & ~Filters.command, poll_result))


if __name__ == '__main__':
    updater.start_polling()
    updater.idle()
