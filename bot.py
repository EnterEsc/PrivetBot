#-*- coding: utf-8 -*-    
#PROSTO TAK
import requests
import random
from time import sleep

def get_updates_json(request):
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates',data=params)
    print(response)
    return response.json()

def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    print(results[total_updates])
    return results[total_updates]

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    print(chat_id)
    return chat_id

def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

def main():
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
	if update_id == last_update(get_updates_json(url))['update_id']:
	    aa = random.randint(0,7)
	    if aa == 0:
	        send_mess(get_chat_id(last_update(get_updates_json(url))), 'Привет')
	    if aa == 1:
                send_mess(get_chat_id(last_update(get_updates_json(url))), 'Приветули')
	    if aa == 2:
                send_mess(get_chat_id(last_update(get_updates_json(url))), 'Приветик')
	    if aa == 3:
                send_mess(get_chat_id(last_update(get_updates_json(url))), 'Салют!')
	    if aa == 4:
                send_mess(get_chat_id(last_update(get_updates_json(url))), 'Приветствую')
	    if aa == 5:
                send_mess(get_chat_id(last_update(get_updates_json(url))), 'Здравствуй')
	    if aa == 6:
                send_mess(get_chat_id(last_update(get_updates_json(url))), 'Ghbdtn')
	    if aa == 7:
                send_mess(get_chat_id(last_update(get_updates_json(url))), 'Добрового времени суток')
	    update_id += 1
	sleep(1)
	   
if __name__ == '__main__':
    main()

