# -*- coding: utf-8 -*-
import json


def json_write(data):
    with open('updates.json', 'w') as f: #в переменной f открытый для записи объект json
        # делаем запись в фаил (что, куда, ,выключить замену кирилицы)
        r = json.dump(data, f, indent=2, ensure_ascii=False)

def main():
    pass

if __name__ == '__main__':
    main()
