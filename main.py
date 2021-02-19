# -*- coding: utf-8 -*-
import requests
import config
from time import sleep

token = config.token
URL = 'https://api.telegram.org/bot' + token + '/'
global last_update_id
last_update_id = 0

def get_updates():
    url = URL + 'getupdates'
    # вызываем урл и полученное сохраняем в переменную r
    r = requests.get(url)
    # возвращает контент, проблемы с рус кодировкой
    # print(r.content)
    # возвращает json объект, нет проблем с кодировкой
    # print(r.json())
    return r.json() # возвращаем json

def get_message():
    data = get_updates()
    current_update_id = data['result'][-1]['update_id']

    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id
        # -1 последнее сообщение, тк последий элт словаря
        chat_id = data['result'][-1]['message']['chat']['id']
        message_text = data['result'][-1]['message']['text']
        message = {'chat_id': chat_id, 'text': message_text}
        return message
    return None

def send_message(chat_id, text='Wait a second, please...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)

def main():
    while True:
        answer = get_message()
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']
            if 'кашу' in text:
                send_message(chat_id, 'Which one?')
        else:
            continue
        sleep(2)


if __name__ == "__main__":
    main()
