import telebot
import random

import requests
import datetime


class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=5):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = None

        return last_update


token = '544229282:AAEWTO2eKAqGhfUF4QTq6vvSMIUKmHeQJcU'
bot = telebot.TeleBot(token)
mat = ['Тобi пiзда', 'Пашел нахой', 'Закрой ебало', 'Я тебя найду и выебу', 'Чтоб тебя черти ебали', 'Уебись об стену',
       'Распиздапрёбищное хуебланище', 'Ты чмошник и рукоблуд ебанный', 'ШНУРОК ХУСОИНОВСКИЙ',
       'У тебя пизда такая что ведро со свистом пролетает', 'Я твой рот калиткой хлопал ', 'Ебись 17ым апостолом',
       'Пьяная баба, пизде не хозяйка', 'Переебись к хуям собачим']
random_message = lambda: random.choice(mat)  # команда для рандома списка
mat2 = ['трахни себя', 'не еби биван', 'уебывай на хуй', 'отсоси', 'сядь на бутылку', 'продолбись', 'ИДИ НННАХОЙ',
        'ебать тебя ирландским долгом', 'свинья хуями воняешь', 'твоя дыра как водопроводная труба',
        'разпизди тебя тройным членом ,членосос ебучий !', 'чихуахуа абосротое будешь у серьки в сумочке сидеть',
        'пробудоблядская пиздохлоёбина']
friend = lambda: random.choice(mat2)


@bot.message_handler(commands=['start'])  # Сообщения которые отправляются при вводе пользователем команды /start
def start(message):
    sent = bot.send_message(message.chat.id, 'Привет, как тебя зовут?')  # Бот отправляет сообщение
    bot.register_next_step_handler(sent, hello)  # создание цепочки из сообщений, следующее сообщение : "hello"


def hello(message):
    bot.send_message(message.chat.id, 'Иди нахуй {name}.'.format(name=message.text))


# вормат имени -предыдущее сообщения пользователя


@bot.message_handler(content_types=['text'])  # обычные текстовые сообщения
def attack(message):
    if message.text == 'Обматери приятеля':
        sent = bot.send_message(message.chat.id, 'Как завут этого пездюка?')
        bot.register_next_step_handler(sent, attack2)
    elif message.text == 'Где живешь?':
        bot.send_message(message.chat.id, 'Мухосранск')
    elif message.text == 'Спасибо':
        bot.send_message(message.chat.id, 'Незашто (Иди на хуй пидор)')
    else:
        bot.send_message(message.chat.id, random_message())  # рандомные сообщеня из списка


def attack2(message):
    bot.send_message(message.chat.id, '{name}' ' {matt}'.format(name=message.text, matt=friend()))


if __name__ == '__main__':
    bot.polling(none_stop=True)
