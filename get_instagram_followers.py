# Foxter @ 29/10/2017 - 1:15AM
# Получаем число фолловеров из instagram указывая username
# https://www.instagram.com/username/?__a=1

import requests
import json
    

def coll():
    USR = input("Введите Username: ")
    URL = 'https://www.instagram.com/'
    URL_END = '/?__a=1'
    FULL_URL = URL+USR+URL_END
    try:
        r = requests.get(FULL_URL)
        return r.json()
    except:
        print('Что-то пошло не так...')


def get_calls():
    try:
        data = coll()
        followers = data['user']['followed_by']['count']
        print('Подписчиков:',followers)
    except:
        print('Некорректный Username')


def main():
    get_calls()


if __name__ == '__main__':
    main()
