import requests

def get_updates_json(request):
	response = requests.get(request+"getUpdates")
	return response

def last_update(data):
	result = data['result']
	total_update = len(result)-1
	return result[total_update]

def get_chat_id(update):  
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat,text):
	params = {'chat_id': chat, 'text': text}
	response = requests.post(url + 'sendMessage', data=params)
	return response

chat_id = get_chat_id(last_update(get_updates_json(url)))
#send_mess(chat_id,"Priveeeeet")


