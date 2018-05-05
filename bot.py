import requests

url = "https://api.telegram.org/bot576459441:AAEDwRC3FX8SRSM7q-PMaWeuVRZL4u664tM/"

def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
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

chat_id = get_chat_id(last_update(get_updates_json(url)))
send_mess(chat_id, 'Your message goes here')
